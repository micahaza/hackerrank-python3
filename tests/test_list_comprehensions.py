from unittest.mock import patch
from solutions.list_comprehensions import list_compr
import pytest
import sys
import io


test_data = [
    (['2', '2', '2', '2'], '[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]'),
    (['1', '1', '1', '2'], '[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]')

]


@pytest.mark.parametrize("test_input, expected_output", test_data)
def test_if_else(test_input, expected_output):
    with patch('builtins.input', side_effect=test_input):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        list_compr()
        output = sys.stdout.getvalue().strip()
        print(output)
        sys.stdout = stdout
        assert output == expected_output
