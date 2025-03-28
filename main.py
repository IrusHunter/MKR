from typing import List


def read_file_lines(filename: str) -> list:
    """Зчитує рядки з файлу та повертає їх у вигляді множини."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено.")
        return []

def write_file(filename: str, lines: List[str]) -> None:
    """Записує множину рядків у файл."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(lines) if lines else "")

def compare_files(file1: str, file2: str) -> None:
    """Порівнює два файли та записує однакові та різні рядки у відповідні файли."""
    lines1 = read_file_lines(file1)
    lines2 = read_file_lines(file2)

    same_lines = []
    diff_lines = []
    for line in lines1:
        if line not in lines2:
            diff_lines.append(line)
        else:
            same_lines.append(line)
    for line in lines2:
        if line not in lines1:
            diff_lines.append(line)

    write_file("same.txt", same_lines)
    write_file("diff.txt", diff_lines)

