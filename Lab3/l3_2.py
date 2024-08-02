'''Write a function called calculate_slope which return the slope of a linear equation'''
def calculate_slope(a,b,c,d):
    slope = (b-a)/(d-c)
    if (b==a):
        return (print("x1 and x2 can't be same."))
    return slope
a=float(input("Enter the value of x1 : "))
b=float(input("Enter the value of x2 : "))
c=float(input("Enter the value of y1 : "))
d=float(input("Enter the value of y2 : "))
print(calculate_slope(a,b,c,d))
