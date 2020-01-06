import unittest

from parameterized import parameterized
from src.main import clean_value


class TestTFVars2Markdown(unittest.TestCase):

	@parameterized.expand([
		(["${string}"], "string"),
		(["foo"], "foo"),
		(["Some long string here with unicode ćčđš"], "Some long string here with unicode ćčđš"),
		([False], "False"),
		([1], "1"),
		([["foo", "bar"]], "['foo', 'bar']"),
		([[True, True, False]], "[True, True, False]"),
	])
	def test_clean_value(self, input_string, expected_result):
		actual_result = clean_value(input_string)

		self.assertEqual(actual_result, expected_result)
