"""
Abduljabbar Said
BMI tester
"""

def main():
    a = eval(input("What is your weight in pounds? "))
    b = eval(input("What is your heightin inches? "))
    c = a * 720
    d = b**2
    e = c/d

    if (e < 19):
        print("Your weight is below average")
    elif (19 <= e <=25):
        print("Your weight is average")
    else:
        print("Your weight is above average")

    
main()
    
