import pytest
from main import write_file

@pytest.mark.parametrize("lines, expected_content", [
    (["Рядок 1", "Рядок 2"], "Рядок 1\nРядок 2"),
    ([], ""),
    (["Один рядок"], "Один рядок"),
])
def test_write_file(tmp_path, lines, expected_content):
    test_file = tmp_path / "test_output.txt"
    write_file(str(test_file), lines)
    with open(test_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == expected_content