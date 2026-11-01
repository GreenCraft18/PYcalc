import math # Imports the python math module for more math functions

print("Welcome to PYcalc") # Prints a message to the terminal that welcomes the user to PYcalc
print("Supported operations:") # Prints the header for the supported operations
print("+, -, *, /, ^ -or- **") # Prints the supported operations
print("√(x) -or- sqrt(x), sin(x), cos(x), tan(x)") # Prints the supported math functions (referring to as operations)
print("π -or- pi") # The support mathematical constants (reffering to as operations)
print("Note: Math functions (sqrt, sin, etc.) require parenthesis around the argument, e.g., sqrt(4), sin(0.5)") # Note for math functions to tell the user that they require parenthesis around the argument
print("Note: sin, cos, and tan use radians, not degrees") # Note for all math functions except [math.sqrt()] that they use radians and not degrees
print("Type 'exit' to exit the calculator") # Tells user to type exit to exit PYcalc

while True: # A loop for the actual calculator that is broken with the [break] functions

    problem = input("Enter your expression here: ") # Asks the user to type the expression they want solved and assigns the [problem] variable to the expression the user has typed in
    
    problem_literal = problem # Assigns the [problem_literal] variable to the [problem] variable that has been assgined to the expression the user has typed in

    problem_literal = problem_literal.replace("sqrt", "math.sqrt") # Replaces any [sqrt] that has been typed in the expression the user has typed in with [math.sqrt] for proper sq. root calculation
    problem_literal = problem_literal.replace("sin", "math.sin") # Replaces any [sin] that has been typed in the expression the user has typed in with [math.sin] for proper sin calculation
    problem_literal = problem_literal.replace("cos", "math.cos") # Replaces any [cos] that has been typed in the expression the user has typed in with [math.cos] for proper cos calculation
    problem_literal = problem_literal.replace("tan", "math.tan") # Replaces any [tan] that has been typed in the expression the user has typed in with [math.tan] for proper tan calculation
    problem_literal = problem_literal.replace("√", "math.sqrt") # Replaces any [√] that has been typed in the expression the user has typed in with [math.sqrt] for proper sq. root calculation
    problem_literal = problem_literal.replace("^", "**") # Replaces any [^] that has been typed in the expression the user has typed in with [**] for proper exponent calculation
    problem_literal = problem_literal.replace("pi", "math.pi") # Replaces any [pi] that has been typed in the expression the user has typed in with [math.pi] for proper pi
    problem_literal = problem_literal.replace("π", "math.pi") # Replaces any [π] that has been typed in the expression the user has typed in with [math.pi] for proper pi
    
    if problem.lower() == "exit": # Sets an [if] statement to check if [exit] has been typed in the [problem] variable
            print("Exiting PYcalc") # Prints a message to the user that they are exiting PYcalc
            break # Breaks the [while True:] loop
            exit() # An unneccesary exit function just to make it clear in the code that the scripts stops here
            
    try: # Tries to do the code right underneath this line of code
        print(f"{problem} = {eval(problem_literal)}") # Prints to the user the problem they have typed in and the answer with the [eval()] function
    except Exception as error: # If the [eval()] function cannot evaluate the expression the user has (partially) typed in, then it will activate the code right underneath and also assigns the [error] variable to the text Python will print as the error
        print(f"Error: {error}") # Prints to the user [Error:] and then the [error] variable containing the error Python will print in it after [Error:]