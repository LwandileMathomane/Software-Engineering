n=int(input("Enter a number:"))

def factorial(n):
    fa=1
    for i in range(1,n+1):
        fa=fa*i
    return fa

print("The factorial of",n,"is",factorial(n))
