# Calculator

# Variables and Operator Request
myFirstVariable = float(input("Enter your first number: "))
mySecondVariable = float(input("Enter your second number: "))
myOperator = input("Enter operator of choice: ")

if myOperator == "+":
    print(str(myFirstVariable) + " + " + str(mySecondVariable) + " = " + str(myFirstVariable + mySecondVariable))
elif myOperator == "-":
    print(str(myFirstVariable) + " - " + str(mySecondVariable) + " = " + str(myFirstVariable - mySecondVariable))
elif myOperator == "/":
    print(str(myFirstVariable) + " / " + str(mySecondVariable) + " = " + str(myFirstVariable /  mySecondVariable))
elif myOperator == "%":
    print(str(myFirstVariable) + " % " + str(mySecondVariable) + " = " + str(myFirstVariable %  mySecondVariable))
elif myOperator == "*":
    print(str(myFirstVariable) + " * " + str(mySecondVariable) + " = " + str(myFirstVariable * mySecondVariable))
else:
    print("The operator is not on the list")