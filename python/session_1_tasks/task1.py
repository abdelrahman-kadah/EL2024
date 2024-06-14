def countNumberFour(listOfNumbers):
    numberFourCount = 0
    for number in listOfNumbers:
        if number == 4:
            numberFourCount += 1
    return numberFourCount

print(countNumberFour([1, 2, 3, 4, 4, 4]))

