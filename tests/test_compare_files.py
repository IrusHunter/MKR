import pytest
from main import compare_files, read_file_lines, write_file


@pytest.fixture
def temp_files(tmp_path):
    """Створює тимчасові файли для тестування."""
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    same_file = tmp_path / "same.txt"
    diff_file = tmp_path / "diff.txt"
    return file1, file2, same_file, diff_file


@pytest.mark.parametrize("content1, content2, expected_same, expected_diff", [
    (["a", "b", "c"], ["b", "c", "d"], ["b", "c"], ["a", "d"]),
    (["x", "y", "z"], ["x", "y", "z"], ["x", "y", "z"], []),
    (["i", "j"], ["k", "l"], [], ["i", "j", "k", "l"]),
    ([], [], [], []),
])
def test_compare_files(temp_files, content1, content2, expected_same, expected_diff, monkeypatch):
    file1, file2, same_file, diff_file = temp_files

    write_file(str(file1), content1)
    write_file(str(file2), content2)

    results = {}
    def mock_write_file(filename, lines):
        results[filename] = lines
    monkeypatch.setattr("main.write_file", mock_write_file)

    compare_files(str(file1), str(file2))

    same_result = results["same.txt"]
    diff_result = results["diff.txt"]

    assert sorted(same_result) == sorted(expected_same)
    assert sorted(diff_result) == sorted(expected_diff)
