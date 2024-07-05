"""
Write a Python program to count the number of lines in a text file.

"""

def countNumberOfLinesInFile(filename):
    with open(filename, "r") as f:
        return len(f.readlines())
    

print(countNumberOfLinesInFile("words.txt"))


