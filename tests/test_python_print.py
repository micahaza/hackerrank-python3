from unittest.mock import patch
from solutions.python_print import print_demo
import pytest
import sys
import io


test_data = [
    (['3'], '123'),
    (['1'], '1'),
    (['10'], '12345678910')
]


@pytest.mark.parametrize("test_input, expected_output", test_data)
def test_if_else(test_input, expected_output):
    with patch('builtins.input', side_effect=test_input):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        print_demo()
        output = sys.stdout.getvalue().strip()
        sys.stdout = stdout
        assert output == expected_output
