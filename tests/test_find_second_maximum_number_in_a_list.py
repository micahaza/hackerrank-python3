from unittest.mock import patch
from solutions.find_second_maximum_number_in_a_list import find_second_max
import pytest
import sys
import io


test_data = [
    (['5', '2 3 6 6 5'], '5'),
    (['5', '0 0 0 0 0'], '0'),
    (['3', '57 -57 57'], '-57')
]


@pytest.mark.parametrize("test_input, expected_output", test_data)
def test_if_else(test_input, expected_output):
    with patch('builtins.input', side_effect=test_input):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        find_second_max()
        output = sys.stdout.getvalue().strip()
        sys.stdout = stdout
        assert output == expected_output
