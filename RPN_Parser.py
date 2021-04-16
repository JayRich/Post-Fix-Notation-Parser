# Jason Richardson

import os

def RPN():

	temp_result  = 0	# stores result of the most recent operation

	i = 0			# increment through the expression 

	results_keeptrack = 0	# stores how many results are in the list waiting to be processed

	file = open("input_RPN.txt", "r")	# open input file for reading

	expressions = file.readlines()		# read each line into a list

	file.close()				# close the file 
				
		
	
	for expression in expressions:		# loop through each RPN expression for processing

		i = 0				# set the location in the expression to position 0

		print("Expression: ", expression)	# print the RPN expression before it's processed

		expression = list(expression.split(" "))	#convert the string into a list seperated by spaces

		# each of these if statements corrects the last symbol in the list by removing the \n 
		if( expression[len(expression)-1] == "+\n" ):

			expression.pop(len(expression)-1)

			expression.append("+")

			
			
		if( expression[len(expression)-1] == "-\n" ):

			expression.pop(len(expression)-1)

			expression.append("-")
			
			
		if( expression[len(expression)-1] == "/\n" ):

			expression.pop(len(expression)-1)

			expression.append("/")
			
			
		if( expression[len(expression)-1] == "*\n" ):

			expression.pop(len(expression)-1)

			expression.append("*")
			
				
		# to process the RPN expression each time values and operators are used they are removed from the list and the result is placed at the beginning
		while(len(expression) != 1):		# if the expression has 1 value than it has been processed and that is the result
			
			# each of these if statements determines if the symbol is an operator and then operates on the two most recent values and updates the expression
			if( expression[i] == '+' ):
				
				temp_result = int(expression[i-2]) + int(expression[i-1])	# use the two most recent values before the operator

				remove1 = expression[i]			# variable to remove the operator from expression

				remove2 = expression[i-1]		# variable to remove value from expression

				remove3 = expression[i-2]		# variable to remove value from expression

				if( i > 3 or results_keeptrack > 0 ):	# determine if there is more than one temp_result waiting to be processed in the expression

					results_keeptrack = results_keeptrack + 1	# increase the count of how many temp_results are in the expression 

					expression.insert(results_keeptrack, temp_result)	# add result to the beginning of the expression for later evaluation
				else:
					expression.insert(0, temp_result)
				
				expression.remove(remove1)	# remove the operator

				expression.remove(remove2)	# remove the value

				expression.remove(remove3)	# remove the value
				
				i = i - 2	# because we shortened the expression by removing 3 symbols the increment variable representing current location in the list must be updated
				
				
				
				
			# same algorithm but with subtraction		
			if( expression[i] == '-' ):

				temp_result = int(expression[i-2]) - int(expression[i-1])

				remove1 = expression[i]

				remove2 = expression[i-1]

				remove3 = expression[i-2]

				if( i > 3 or results_keeptrack > 0 ):

					results_keeptrack = results_keeptrack + 1

					expression.insert(results_keeptrack, temp_result)
				else:
					expression.insert(0, temp_result)

				expression.remove(remove1)

				expression.remove(remove2)

				expression.remove(remove3)

				i = i - 2
				
				
				
			# same algorithm but with division		
			if( expression[i] == '/' ):

				temp_result = int(expression[i-2]) / int(expression[i-1])

				remove1 = expression[i]

				remove2 = expression[i-1]

				remove3 = expression[i-2]

				if( i > 3 or results_keeptrack > 0 ):

					results_keeptrack = results_keeptrack + 1

					expression.insert(results_keeptrack, temp_result)

				else:
					expression.insert(0, temp_result)

				expression.remove(remove1)

				expression.remove(remove2)

				expression.remove(remove3)

				i = i - 2
			
			
				
				
			# same algorithm but with multiplication	
			if( expression[i] == '*' ):
				
				temp_result = int(expression[i-2]) * int(expression[i-1])

				remove1 = expression[i]

				remove2 = expression[i-1]

				remove3 = expression[i-2]

				if( i > 3 or results_keeptrack > 0 ):

					results_keeptrack = results_keeptrack + 1

					expression.insert(results_keeptrack, temp_result)

				else:
					expression.insert(0, temp_result)

				expression.remove(remove1)

				expression.remove(remove2)

				expression.remove(remove3)
			
				i = i - 2
				
				
			
			
			i = i + 1	# move to the next character in the expression for evaluation
			
		
		final_result = expression[0]	# if there is only one value in the list then the expression has been fully evaluated and return final result

		print("Result: ", final_result, "\n")

		temp_result = 0

		results_keeptrack = 0
		

RPN()
