# q.1 print the cube of each value of a list

l1 = [1,2,3,4]
x = [x**3 for x in l1]
print("cube of all elements in list")
print(x)

# q.2 get all the prime numbers in a specific range

n = int(input("Enter the range"))
print("Prime numbers are: ")
x = [p for p in range(2,n) if 0 not in [p%d for d in range(2,p)]]
print(x)

# q.3 differentiate between list comprehension and generator expression

"""In terms of syntax, the only difference is that you use parenthesis instead of square brackets.
The main advantage of generator over a list is that it take much less memory."""

#LAMBDA & MAP


# q.4 convert the python list to fahrenheit

Celsius = [39.2, 36.5, 37.3, 37.8]
print("Temp Farenhite")
y=list(map(lambda x:(x * 1.8) + 32,Celsius))
print(y)

# q.5 square all the elements of a list

l = [1,2,3,4,5]
x = list(map(lambda x:x**2,l))
print(x)

#FILTER & REDUCE

# q.6 filter out all the primes from a list

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in range(2, 8): 
     p = list(filter(lambda x: x == i or x % i and x > 1, num))
print("Filtered Elements")
print(p)

# q.7 multiply all the elements of a list

from functools import reduce
l1 = [1,2,3,4,5,6]
p = reduce(lambda x, y: x*y,l1)
print(p)
