#Chapter 5 - Data structures
#https://docs.python.org/3/tutorial/

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)
print("Count apples")
print(fruits.count('apple'))
print("Count tangerines")
print(fruits.count('tangerine'))
print("Index of banana: ")
print(fruits.index('banana'))
print("Find next banana after 4")
print(fruits.index('banana', 4))
print("Reverse the list")
print(fruits.reverse())
print(fruits)
print("Sort the list")
print(fruits.sort())
print("Pop the list, take from the top")
print(fruits)
print(fruits.pop())
print(fruits)

print("5.1.1 Using List as Stack")
stack = [3, 4, 5]
print(stack)
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
stack.pop()
print(stack)

print("5.1.2. Using List as Queues")
from collections import deque
queue = deque(["Eric", "John", "Micheal"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)

print("5.1.3. List Comprehensions")
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
print("less memory")
squares = list(map(lambda x: x**2, range(10)))
print(squares)
print("another way, more readlable")
squares = [x**2 for x in range (10)]
print(squares)

print("List Comprehensions")
compre = [(x, y) for x in [1,2, 3] for y in [3, 1, 4] if x != y]
print (compre)
print("and the equivalent way")
combs=[]
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)

print("tuple")
vec = [-4, -2, 0, 2, 4]
print(vec)
print("create a new list with the values doubled")
print([x*2 for x in vec])
print("filter the list to exclude negative numbers")
print([x for x in vec if x >= 0])
print("apply a funciton to all the elements")
print([abs(x) for x in vec])
print("call a method on each element")
freshfruit = [' banana', " loganberry ", "passion fruit  "]
print(freshfruit)
[weapon.strip() for weapon in freshfruit]
print("strip freshfruit")
print(freshfruit)
print("# create a list of 2-tuples like(number, square)")
print([(x, x**2) for x in range(6)])
print("# paranthesized! or die")
print("# flatten  a list using a listcomp with two 'for'")
vec = [[1,2,3,], [4,5,6], [7,8,9]]
res = [num for elem in vec for num in elem]
print(res)

print("List comprehensions can contain complex expressions and nested functions")
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])






