import pytest
from main import read_file_lines

def test_read_file_lines(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("Рядок 1\nРядок 2\nРядок 3", encoding="utf-8")
    lines = read_file_lines(str(test_file))
    assert lines == ["Рядок 1", "Рядок 2", "Рядок 3"]

def test_read_file_lines_file_not_found():
    lines = read_file_lines("non_existent.txt")
    assert lines == []