#https://docs.python.org/3/tutorial/modules.html

# Fibonacci numbers modules
def fib(n):
    a,b = 0,1
    while a < n:
        print (a, end=' ')
        a, b = b, a+b
    print()
    
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b

#the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". That means that by adding this code at the end of your module:
#you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file:
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))