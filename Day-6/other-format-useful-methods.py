import json
import csv
# import pandas as pd
import PyPDF2


def display_json():
    with open("./data.json") as f:
        content_json = json.load(f)
        print(content_json)


def display_name_from_json():
    with open("./data.json") as f:
        name = json.load(f)["name"]
        print(name)

# reader() function return each row as a list


def display_csv_reader():
    with open("./myFile0.csv") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print(row)


# DictReader() function return all the data in dictionary object


def display_csv_reader_dict():
    with open("./myFile0.csv") as f:
        data = csv.DictReader(f, delimiter=',')
        for row in data:
            print(row["firstname"] + " email is " + row["email"])


# def display_csv_pandas():
#     df = pd.read_csv('myFile0.csv')
#     print(df)


def read_pdf():
    with open("./Web Hacking 101 How to Make Money Hacking Ethically ( PDFDrive.com ).pdf", 'r+b') as f:
        reader = PyPDF2.PdfReader(f)
        print(len(reader.pages))
        print(reader.metadata)
        page_obj = reader.pages[3]
        print(page_obj.extract_text())


if __name__ == "__main__":
    # display_json()
    # display_name_from_json()
    # display_csv_reader()
    # display_csv_reader_dict()
    # display_csv_pandas()
    read_pdf()
