from random import choice


def get_file_lines(filename):
    """Returns a list of strings which are the lines of the file passed a the parameter."""
   
    infile = open(filename, "r")
    file_lines = infile.readlines()
    infile.close()
    return file_lines


# ------------------------------------------------

woman_works_lines = get_file_lines("Woman Work by Maya Angelou.txt")

# Test
print(woman_works_lines)