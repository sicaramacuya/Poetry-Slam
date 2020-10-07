from random import choice


def get_file_lines(filename):
    """Returns a list of strings which are the lines of the file passed a the parameter."""
   
    infile = open(filename, "r")
    file_lines = infile.readlines()

    # this will get rid of \n in every element of the list
    clean_file_lines = []
    for lines in file_lines:
        clean_file_lines.append(lines.strip())

    infile.close()
    return clean_file_lines

def  lines_printed_backwards(lines_list):
    """Prints the list passed as a paamentrs backwards."""

    # .reverse() will reverse the list
    lines_list.reverse()
    # len() will return an integer equaling the length of the list
    lines_list_length = len(lines_list)

    for index in range(lines_list_length):
        line = lines_list[index]
        line_num = lines_list_length - index
        print(f'{line_num} {line}')

def lines_printed_random(lines_list):
    for lines in lines_list:
        print(choice(lines_list))

# ------------------------------------------------

woman_works_lines = get_file_lines("Woman Work by Maya Angelou.txt")

# Test
lines_printed_backwards(woman_works_lines)
print("\n\n\n\n")
lines_printed_random(woman_works_lines)