userInput = input("Problem: ")

operations = ["+", "-", "*", "/"]
parantheses = ["(", ")"]

def Spacer(userInput):
    i = 0
    while i < len(userInput):
        if userInput[i] in operations or userInput[i] in parantheses:
            userInput = userInput[:i] + " " + userInput[i] + " " + userInput[i+1:]
            i += 2
        i += 1
    print(userInput)

Spacer(userInput)