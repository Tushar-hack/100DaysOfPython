import os
from pathlib import Path


def count_files(directory):
    total = 0
    for dirpath, dirnames, files in os.walk(directory):
        for file in files:
            total += 1
    return total


def count_files_second(path):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += 1
        else:
            total += count_files_second(entry)
    return total


def count_files_pathlib(path):
    total = 0
    for entry in Path(path).iterdir():
        if entry.is_file():
            total += 1
        else:
            total += count_files_pathlib(entry)
    return total


print(count_files("./"))
print(count_files_second("./"))
print(count_files_pathlib("./"))
