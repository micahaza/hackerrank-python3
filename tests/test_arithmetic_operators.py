from unittest.mock import patch
from solutions.arithmetic_operators import arithmetic_ops
import pytest
import sys
import io


test_data = [
    (['3', '2'], '5\n1\n6'),
    (['10', '10'], '20\n0\n100'),
    (['12', '-3'], '9\n15\n-36'),
    (['7', '9'], '16\n-2\n63')
]


@pytest.mark.parametrize("test_input, expected_output", test_data)
def test_if_else(test_input, expected_output):
    with patch('builtins.input', side_effect=test_input):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        arithmetic_ops()
        output = sys.stdout.getvalue().strip()
        sys.stdout = stdout
        assert output == expected_output
