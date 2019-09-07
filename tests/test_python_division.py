from unittest.mock import patch
from solutions.python_division import division_demo
import pytest
import sys
import io


test_data = [
    (['4', '3'], '1\n1.3333333333333333'),
    ([2, 2], '1\n1.0'),
    ([50, 4], '12\n12.5'),
    ([-4, 2], '-2\n-2.0'),
]


@pytest.mark.parametrize("test_input, expected_output", test_data)
def test_if_else(test_input, expected_output):
    with patch('builtins.input', side_effect=test_input):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        division_demo()
        output = sys.stdout.getvalue().strip()
        sys.stdout = stdout
        assert output == expected_output
