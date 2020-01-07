# tfvars2markdown

Converts Terraform 0.12+ variables file into a Markdown table

- [tfvars2markdown](#tfvars2markdown)
    + [Why tfvars2markdown](#why-tfvars2markdown)
  * [Install](#install)
  * [Usage](#usage)
    + [Options](#options)
  * [Examples](#examples)
      - [Defaults](#defaults)
      - [No backticks](#no-backticks)
      - [Different heading](#different-heading)
  * [Tests](#tests)

### Why tfvars2markdown

Friends don't let friends provide Terraform modules without READMEs containing input variables and outputs.

This Python package can generate Markdown-flavored tables  for input variables for you by reading `.tf` files in a folder.

Generated Markdown table is compatible with the following services:
* Github
* Bitbucket
* GitLab

## Install
```
pip install tfvars2markdown
```

## Usage
```
tfvars2markdown my_vars.tf
```

### Options
| Argument         | Description                                                                      | Default value | Required |
|------------------|----------------------------------------------------------------------------------|---------------|----------|
| `tf_vars_file`   | Path to the .tf file containing variables                                        |       -       |  `True`  |
| `-t/--no-ticks`  | Disable backticks around values in "Type" and "Default" columns                  |    `False`    |  `False` |
| `-d/--heading`   | Changes the default "Inputs" heading. Only first level heading (#) is supported. |    `Inputs`   |  `False` |

## Examples

#### Defaults
```
$ tfvars2markdown vars.tf
# Inputs
|    Name    |                                      Description                                      |      Type      |         Default         | Required |
|------------|---------------------------------------------------------------------------------------|:--------------:|:-----------------------:|:--------:|
| some_var_1 | Some description var_1                                                                |    `string`    |          `foo`          |   yes    |
| some_var_2 | Some description var_2                                                                |     `bool`     |         `False`         |   yes    |
| some_var_3 | Some description var_3                                                                |    `number`    |          `12`           |   yes    |
| some_var_4 | -                                                                                     | `list(string)` | `['foo', 'bar', 'baz']` |   yes    |
| some_var_5 | Some description var_5. This is a very long description with unicode characters ćšđž |  `list(bool)`  |  `[True, True, False]`  |   yes    |
| some_var_6 | Some description var_6                                                                | `list(number)` |       `[1, 2, 3]`       |   yes    |
| some_var_7 | Some description var_7. No defaults provided                                          |     `any`      |            -            |   yes    |
| some_var_8 | Some description var_8. No type or default provided                                   |       -        |            -            |   yes    |
| some_var_9 | Some description var_8. No type or default provided                                   |       -        |            -            |   yes    |
```

#### No backticks
```
$ tfvars2markdown --no-ticks vars.tf
# Inputs
|    Name    |                                      Description                                      |     Type     |        Default        | Required |
|------------|---------------------------------------------------------------------------------------|:------------:|:---------------------:|:--------:|
| some_var_1 | Some description var_1                                                                |    string    |          foo          |   yes    |
| some_var_2 | Some description var_2                                                                |     bool     |         False         |   yes    |
```

#### Different heading
```
$ tfvars2markdown --heading "my input vars" vars.tf
# my input vars
|    Name    |                                      Description                                      |      Type      |         Default         | Required |
|------------|---------------------------------------------------------------------------------------|:--------------:|:-----------------------:|:--------:|
| some_var_1 | Some description var_1                                                                |    `string`    |          `foo`          |   yes    |
| some_var_2 | Some description var_2                                                                |     `bool`     |         `False`         |   yes    |
```

Due to limitations in [pytablewriter](https://github.com/thombashi/pytablewriter) only first level heading (#) is supported.

## Tests

Install `test_requirements.txt` and run

```
python -m unittest discover
```