def print_file_content():
    with open("./fun.txt") as f:
        print(f.read())


def print_file_content_readlines():
    with open("./fun.txt", "r") as f:
        lines = f.readlines()
        print(lines[0])


def print_file_content_one_line_at_a_time():
    with open("./fun.txt", "r") as f:
        line = f.readline()
        while line != '':
            print(line)
            line = f.readline()


if __name__ == "__main__":
    # print_file_content()
    # print_file_content_readlines()
    print_file_content_one_line_at_a_time()