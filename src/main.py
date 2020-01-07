from sys import exit

import hcl2
import argparse

from pathlib import Path
from pytablewriter import MarkdownTableWriter
from pytablewriter.style import Style

from lark.exceptions import UnexpectedToken


__version__ = "0.0.4"


def clean_value(value):
    return_value = None

    if isinstance(value, list) and len(value) == 1:
        element = value[0]
    else:
        return str(value)

    if isinstance(element, str):
        return_value = element.replace("${", "").replace("}", "")

    else:
        if len(value) == 1:
            return_value = value[0]

    return str(return_value)


def format_type_default_columns(value, ticks=True):
    cleaned_value = clean_value(value)

    if ticks:
        return f"`{cleaned_value}`" if len(cleaned_value) > 0 else "-"

    else:
        return f"{cleaned_value}" if len(cleaned_value) > 0 else "-"


def clean_row(tf_var, ticks):
    row = []
    var_name = list(tf_var.keys())[0]
    var_details = list(tf_var.values())[0]

    row.append(var_name)

    var_type = format_type_default_columns(var_details.get("type", ""), ticks)
    var_default = format_type_default_columns(var_details.get("default", ""), ticks)
    var_description = clean_value(var_details.get("description", ""))
    var_required = "yes" if len(var_default) > 0 else "no"

    row.append(var_description if len(var_description) > 0 else "-")
    row.append(var_type)
    row.append(var_default)
    row.append(var_required)

    return row


def _parse_args():
    parser = argparse.ArgumentParser(
        description="Converts Terraform 0.12+ variables file into a Markdown table"
    )
    parser.add_argument(
        "tf_vars_file",
        help="Path to a Terraform variables file"
    )

    parser.add_argument(
        "-t", "--no-ticks",
        action="store_false",
        help="Disable backticks around values in \"Type\" and \"Default\" columns"
    )

    parser.add_argument(
        "-d", "--heading",
        default="# Inputs",
        help="Changes the default \"Inputs\" heading. Due to limitations in dependencies only heading 1 (#) is "
             "supported. "
    )

    return parser.parse_args()


def generate_table(data_matrix, heading):
    writer = MarkdownTableWriter()

    writer.margin = 1
    writer.table_name = heading
    writer.headers = ["Name", "Description", "Type", "Default", "Required"]

    writer.styles = [
        Style(),
        Style(),
        Style(align="center"),
        Style(align="center"),
        Style(align="center")
    ]

    writer.value_matrix = data_matrix

    return writer.dumps()


def load_tf_file(file_path):
    try:
        with file_path.open(mode="r") as input_file:
            data = hcl2.load(input_file)

        return data

    except FileNotFoundError:
        exit(f"File '{file_path}' does not exist")

    except UnexpectedToken as exc:
        exit(f"File '{file_path}' is malformed. {exc}")


def transform_tf_vars(tf_vars, ticks):
    variables = tf_vars.get("variable")
    output = []

    if not isinstance(variables, list):
        exit(f"Expected a list of variables, got {variables.__repr__}")

    for a_variable in variables:
        row = clean_row(a_variable, ticks)

        output.append(row)

    return output


def cli():
    args = _parse_args()
    file_path = args.tf_vars_file
    ticks = args.no_ticks
    heading = args.heading

    absolute_path = Path(file_path).absolute()

    data = load_tf_file(absolute_path)
    matrix = transform_tf_vars(data, ticks)

    print(generate_table(matrix, heading))


if __name__ == "__main__":
    cli()
