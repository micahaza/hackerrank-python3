from unittest.mock import patch
from solutions.write_a_function import  is_leap
import pytest
import sys
import io


test_data = [
    (['1990'], 'False'),
    (['2000'], 'True'),
    (['2400'], 'True'),
    (['1800'], 'False'),
    (['1900'], 'False'),
    (['2100'], 'False'),
    (['2200'], 'False'),
    (['2300'], 'False'),
    (['2500'], 'False'),
]


@pytest.mark.parametrize("test_input, expected_output", test_data)
def test_if_else(test_input, expected_output):
    with patch('builtins.input', side_effect=test_input):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        is_leap()
        output = sys.stdout.getvalue().strip()
        print(output)
        sys.stdout = stdout
        assert output == expected_output
