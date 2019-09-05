from unittest.mock import patch
from solutions.py_if_else import if_else
import pytest
import sys
import io


test_data = [
    (['3'], 'Weird'),
    (['4'], 'Not Weird'),
    (['24'], 'Not Weird'),
    (['20'], 'Weird'),
    (['31'], 'Weird'),
    (['32'], 'Not Weird'),
    (['98'], 'Not Weird'),
    (['99'], 'Weird')
]


@pytest.mark.parametrize("test_input, expected_output", test_data)
def test_if_else(test_input, expected_output):
    with patch('builtins.input', side_effect=test_input):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        if_else()
        output = sys.stdout.getvalue().strip()
        sys.stdout = stdout
        assert output == expected_output
