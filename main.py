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
