"""
Application Name: Lab1.py
Developer: Alfred Varghese Jose
Date: 09/08/2023

An application program that reads five positive numeric values and determines their average and standard deviation and displays as output.
"""

def lab1():

    # accept user input
    first_number = float(input("Enter first number:\t"))
    second_number = float(input("Enter second number:\t"))
    third_number = float(input("Enter third number:\t"))
    fourth_number = float(input("Enter fourth number:\t"))
    fifth_number = float(input("Enter fifth number:\t"))

    # calculate average of five numbers
    average = (first_number + second_number + third_number + fourth_number + fifth_number)/5

    # calculate standard deviation of five numbers
    standard_deviation = (((first_number - average)**2 + (second_number - average)**2 + (third_number - average)**2 + (fourth_number - average)**2 + (fifth_number - average)**2)/5)**0.5

    # output formatting
    author_first_name = "Alfred Varghese"
    author_last_name = "Jose"
    author_student_number = "N01619463"
    author = "%120s\n%120s" % (author_first_name + " " + author_last_name, author_student_number)

    header = "%16s%16s%16s%16s%16s%15s%25s" % ("First Number", "Second Number", "Third Number", "Fourth Number", "Fifth Number", "Average", "Standard Deviation")

    data = "%16.2f%16.2f%16.2f%16.2f%16.2f%15.2f%25.2f" % (first_number, second_number, third_number, fourth_number, fifth_number, average, standard_deviation)

    print("\n%s\n%s\n%s\n%s\n%s\n" % ("*"*120, author, "#*"*60, header, data))


if __name__=='__main__':

    print(__doc__)
    lab1()