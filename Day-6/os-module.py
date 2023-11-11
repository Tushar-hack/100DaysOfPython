from datetime import datetime
import os
import glob
from pathlib import Path


def print_cwd():
    # Getting the current working Directory
    cwd = os.getcwd()
    print(f"Current working directory is {cwd}")


def up_one_director():
    # Changing the current working directory
    os.chdir("../../")


def display_entries_in_directory(directory):
    # printing all the file and folders inside the passed directory
    with os.scandir(directory) as entries:
        for entry in entries:
            print(entry.name)


print_cwd()
up_one_director()
print_cwd()
display_entries_in_directory("./")


def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formatted_datetime = utc_timestamp.strftime("%d %b %Y %H %M %S")
    return formatted_datetime


def display__entries_in_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            print("Name: ", entry.name)
            #  Getting all the information about the file
            info = entry.stat()
            #  Getting the creation time of that file
            print(f"Creation Time: {format_datetime(info.st_ctime)}")
            # Getting last access time
            print(f"Last access time: {format_datetime(info.st_atime)}")
            print(f"Size: {info.st_size}")


def display_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir():
                print(f"Directory name: {entry.name}")


# display__entries_in_directory("Error/")
display_directory("./")


def display_pngs():
    png_files = glob.glob('*.png')
    print(png_files)


def find_by_name():
    filtered_items = glob.glob('anyfilenamehere')


def find_monster_one_in_subdirs():
    for file in glob.iglob('**/*monster*', recursive=True):
        print(file)


display_pngs()


# Recursively list all files in a directory

def top_down_walk():
    for dirpath, dirnames, files in os.walk('Tushar/Books/'):
        print(f"Directory: {dirpath}")
        print("Includes these directories: ")
        for directory in dirnames:
            print(directory)
        print("Include these files: ")
        for file in files:
            print(file)


top_down_walk()


# Pathlib modules: More Efficient

def print_directory_content():
    entries = Path.cwd()
    # entries = Path('images/')
    # entries = Path.home()
    for entry in entries.iterdir():
        print(entry.name)
        print(entry.parent)
        print(entry.parent.parent)
        print(entry.stem)
        print(entry.suffix)
        print(entry.stat())


print_directory_content()

# Creating Directories


def make_logs_dir():
    try:
        os.mkdir("logs/")
    except FileExistsError as ex:
        print("Logs directory already exists")


make_logs_dir()


def make_output_directory():
    dir_path = Path("output/")
    dir_path.mkdir(exist_ok=True)


make_output_directory()
