# Write a Python program to write a list to a file

listOfWords = ["Hi,", "I", "am", "Abdelrahman"]

def writeListToFile(filename, list):
    with open(filename, 'w') as f:
        f.write(" ".join(list))

writeListToFile("listOfWords.txt", listOfWords)
