import pytest
from main import count_unique_chars, main
    
@pytest.mark.parametrize("input_string, expected_output", [
    ("--string abbbccdf".split(), 4),
    ("--string abcdefghijklmnopqrstuvwxyz".split(), 26),
    ("--string --file".split()),
    ("--string --file --string".split()),
    ("".split()),
    ("--file ".split()),
    ("--file test_1.txt".split()),
    ("--file test_2.txt --string abbbccdf".split()),
    ("--file --file".split()),
    ("--file --string".split()),
    ("--file --string --file".split()),

])
def test_main(input_string, expected_output):
    assert main(input_string) == expected_output
