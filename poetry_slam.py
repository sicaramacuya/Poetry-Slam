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


# ------------------------------------------------

woman_works_lines = get_file_lines("Woman Work by Maya Angelou.txt")

# Test
print(woman_works_lines)