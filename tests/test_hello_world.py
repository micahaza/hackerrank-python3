import sys
import io


def test_hello_world():
    stdout = sys.stdout
    sys.stdout = io.StringIO()

    import solutions.hello_world # noqa

    output = sys.stdout.getvalue().strip()
    sys.stdout = stdout
    assert output == "Hello World!"
