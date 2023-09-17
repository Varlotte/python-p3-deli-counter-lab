katz_deli = []


def line(katz_deli):

    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        linestr = "The line is currently:"
        for index, name in enumerate(katz_deli):
            linestr += (f" {index+1}. {name}")
        print(linestr)
    # shows everyone their current place in the line
    # if line is empty, should say "The line is currently empty."
    # "The line is currently: 1. Ada 2. Grace 3. Kent"


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")
    # print new person's name and number in line
    # start at 1 for position in line, not 0 index (index +1)


def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)
    # print the next person in the front of the line
    # then remove them from the line
    # If nobody in line print "There is nobody waiting to be served!"
