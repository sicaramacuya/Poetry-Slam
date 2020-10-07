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
    """Prints the list passed as a paramentrs backwards."""

    # .reverse() will reverse the list
    lines_list.reverse()
    # len() will return an integer equaling the length of the list
    lines_list_length = len(lines_list)

    for index in range(lines_list_length):
        line = lines_list[index]
        line_num = lines_list_length - index
        print(f'{line_num} {line}')

def lines_printed_random(lines_list):
    """Prints the the items of the list passes as a parameters randomly."""

    for lines in lines_list:
        print(choice(lines_list))

def lines_printed_custom(lines_list):
    """Prints the poem but in a specific order. The lines with more "e" in it will go first and the ones with less "e" will go last."""

    # this is added because in this specific case we reverse the list already once using lines_printed_backwards() and we want the lines to be sorted with the correct order.
    lines_list.reverse()

    # this are the list that will store the lines with the specific amount of letters e's in it.
    lines_4e = []
    lines_3e = []
    lines_2e = []
    lines_1e = []
    lines_0e = []

    # this loop will go through every item on the poem.
    for line in lines_list:
        amount_letter_e = 0

        #  this loop will go through every character an count of many "e" this line have.
        for character in line:
            if character == "e":
                amount_letter_e += 1

        # depending on the amount of letters e's one of this if elif statement will be run
        if amount_letter_e == 4:
            lines_4e.append(line)
        
        elif amount_letter_e == 3:
            lines_3e.append(line)

        elif amount_letter_e == 2:
            lines_2e.append(line)

        elif amount_letter_e == 1:
            lines_1e.append(line)

        elif amount_letter_e == 0:
            lines_0e.append(line)
    
    # print lines that have four e's
    for line in lines_4e:
        print(line)
    # print lines that have three e's
    for line in lines_3e:
        print(line)
    # print lines that have two e's
    for line in lines_2e:
        print(line)
    # print lines that have one e's
    for line in lines_1e:
        print(line)
    # print lines that have zero e's
    for line in lines_0e:
        print(line)

# ------------------------------------------------

woman_works_lines = get_file_lines("Woman Work by Maya Angelou.txt")

print("\nThe original poem:\n")
for line in woman_works_lines:
    print(line)    
print("\n\n\n\n")

print("The poem printed backwards:\n")
lines_printed_backwards(woman_works_lines)
print("\n\n\n\n")

print("The peom printed randomly:\n")
lines_printed_random(woman_works_lines)
print("\n\n\n\n")

print("The peom reorginized by the amount of letters e's in each line.\nThe lines with the most e's will go first the one with less go last.\nHere is how it looks like: \n")
lines_printed_custom(woman_works_lines)