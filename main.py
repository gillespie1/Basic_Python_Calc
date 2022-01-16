#Calculator


#Add
def add(n1, n2):
	return n1 + n2

#Subtract
def subtract(n1, n2):
	return n1 - n2

#Multiply
def multiply(n1, n2):
	return n1 * n2

#Divide
def divide(n1, n2):
	return n1 / n2

operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide
}

def calculator():
	"""Takes user input and calculates by selected operator."""
	num1 = float(input("What is the first number? "))
	for symbol in operations:
		print(symbol)
	finished = False

	while not finished:
		operation_symbol = input("Pick an operation: ")
		num2 = float(input("What is the next number? "))
		answer = operations[operation_symbol](num1, num2)
		print(f"{num1} {operation_symbol} {num2} = {answer}")

		go_again = input("Would you like to enter another number? Enter 'y' or type 'n' to start a new calculation: ")
		if go_again == "y":
			num1 = answer
		else:
			finished = True
			calculator()


calculator()