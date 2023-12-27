userInput = input("Problem: ")

operationsArray = ["+", "-", "*", "/"]
parantheses = ["(", ")"]

def Spacer(userInput):
    i = 0
    while i < len(userInput):
        if(userInput[i] in operationsArray):
            userInput = userInput[:i] + " " + userInput[i] + " " + userInput[i+1:]
            i += 2
        else:
            i += 1
    print(userInput)
    
Spacer(userInput)