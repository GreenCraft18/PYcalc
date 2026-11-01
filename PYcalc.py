import math

print("Welcome to PYcalc")
print("Supported operations:")
print("+, -, *, /, ^ or **")
print("sqrt(x) or √, sin(x), cos(x), tan(x)")
print("π or pi")
print("Note: Math functions (sqrt, sin, etc.) require parenthesis around the argument, e.g., sqrt(4), sin(0.5)")
print("Note: sin, cos, and tan use radians, not degrees")
print("Type 'exit' to exit the calculator")

while True:

    problem = input("Enter your expression here: ")
    
    problem_literal = problem

    problem_literal = problem_literal.replace("sqrt", "math.sqrt")
    problem_literal = problem_literal.replace("sin", "math.sin")
    problem_literal = problem_literal.replace("cos", "math.cos")
    problem_literal = problem_literal.replace("tan", "math.tan")
    problem_literal = problem_literal.replace("√", "math.sqrt")
    problem_literal = problem_literal.replace("^", "**")
    problem_literal = problem_literal.replace("pi", "math.pi")
    problem_literal = problem_literal.replace("π", "math.pi")
    
    if problem.lower() == "exit": 
            print("Exiting PYcalc") 
            break
    
    try:
        print(f"{problem} = {eval(problem_literal)}")
    except Exception as error:
        print(f"Error: {error}") 
        
        
        