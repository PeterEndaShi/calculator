userInput = input("Problem: ")

operations = ["+", "-", "*", "/"]
operationsArray = []

def operationsSelect():
    global operationsArray, userInput
    for i in range(len(userInput)):
        if(userInput[i] in operations):
            operationsArray.append(userInput[i])
    print("Operations: " + str(operationsArray))

def splitter(spacerInput):
    problem = spacerInput.split(" ")
    MultiplyDivideSolver(problem)

def MultiplyDivideSolver(problem):
    global operationsArray
    print(problem)
    j = 0
    while j < len(problem):
        if problem[j] in operationsArray and problem[j] == "*":
            problem[j] = float(problem[j-1]) * float(problem[j+1])
            problem.pop(j-1)
            problem.pop(j)

        elif problem[j] in operationsArray and problem[j] == "/":
            problem[j] = float(problem[j-1]) / float(problem[j+1])
            problem.pop(j-1)
            problem.pop(j)

        j += 1

    print(problem)
    AddSubtractSolver(problem)

def AddSubtractSolver(problem):
    k = 0
    while k < len(problem):
        if problem[k] in operationsArray and problem[k] == "+":
            problem[k] = float(problem[k-1]) + float(problem[k+1])
            problem.pop(k-1)
            problem.pop(k)
            continue

        elif problem[k] in operationsArray and problem[k] == "-":
            problem[k] = float(problem[k-1]) - float(problem[k+1])
            problem.pop(k-1)
            problem.pop(k)
            continue

        k += 1

    print("Answer: " + str(problem))

def spacer():
    global userInput
    i = 0
    while i < len(userInput):
        if userInput[i] in operations:
            userInput = userInput[:i] + " " + userInput[i] + " " + userInput[i+1:]
            i += 2
        i += 1
    splitter(userInput)

# RUN
operationsSelect()            
spacer()