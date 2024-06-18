def factorial(value):
    if value <= 1:
        return value
    else:
        return value * factorial(value - 1)

def nat_sum(value):
    if value == 0:
        return value
    else:
        return value + nat_sum(value - 1)

def fibonacci(value):
    if value <= 0:
        return []
    elif value == 1:
        return 0
    elif value == 2:
        return [0, 1]
    else:
        fib = fibonacci(value - 1)
        fib.append(fib[-1] + fib[-2])
        return fib

# Uncomment the code below to run the functions
'''
fac = factorial(5)
print(fac)

nat = nat_sum(10)
print(nat)

fib = fibonacci(10)
print(fib)
'''