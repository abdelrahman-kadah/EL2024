# Write a Python program to count the number of words in a file.

def countWordsInFile(filename):
    with open(filename, mode="r") as f:
        words = f.read()
        listOfWords = words.split(' ')
        print(f"Number of words is: {len(listOfWords)}") 


countWordsInFile("words.txt")