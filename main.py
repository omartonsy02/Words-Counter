# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
file = open("myfile", "r")
count_w = 0
count_s = 0
count_c = 0
words = ""
sen = ""
for line in file:
    words = line.split(" ")
    sen = line.split(".")
count_w = len(words)
count_s = len(sen)-1
line_char = line.replace(" ","")
line_char = line_char.replace(".","")
count_c = len(line_char)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("number of chars =", count_c)
    print("number of words =", count_w)
    print("number of sentences =", count_s)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
