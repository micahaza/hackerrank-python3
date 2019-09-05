from unittest.mock import patch
from solutions.python_loops import loops
import pytest
import sys
import io


test_data = [
    (['5'], '0\n1\n4\n9\n16'),
    ([10], '0\n1\n4\n9\n16\n25\n36\n49\n64\n81'),
    (['0'], ''),
    (['1'], '0'),
    (['2'], '0\n1') 
]


@pytest.mark.parametrize("test_input, expected_output", test_data)
def test_if_else(test_input, expected_output):
    with patch('builtins.input', side_effect=test_input):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        loops()
        output = sys.stdout.getvalue().strip()
        print(output)
        sys.stdout = stdout
        assert output == expected_output
