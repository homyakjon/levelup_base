
# Lists

A = [1, 2, 3, 10, 20, 50, 65]
i = 0
sum = 0
while i < len(A):
    sum = sum + A[i]
    i += 1
    break
    print('sum =', sum)

a = float(input('input value a = '))
n = 2
b = 1 + 1/n
while b > a:
    print(f'number {str(b)} not lower number a = {str(a)}')
    n += 1
    b = 1 + 1/n

a = 'Star'
b = 'Work'
c = 'Water'
print(f"{a.count('a')}  {b.count('o')}  {c.count('t')}")


numbers = ['10', '14', '15', '17', '20', '-5']
num = str(input('Input num: '))
for i in numbers:
    if i == num:
        print('Yes!')
    else:
        print('No value')

# Tuple

list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
print(list(zip(list_a, list_b)))

aria = ["bar", "baz", "qux", "etc"]
aria.insert(0, "foo")
print(tuple(aria))

my_list = (1, 2, 3, 4, 5)
num = 6 in my_list
print(num)

# Home Work N 5

from random import random
a = int(random() * 100)
b = int(random() * 100)
if a%2 and b%2 or a%2==0 and b%2==0:
    a -= 1
print(a, b)
if a%2:
    print(a)
else:
    print(b)


a, b, c = int(input()), int(input()), int(input())
n = a
if b > n:
    n = b
if c > n:
    n = c
    print(n)


from random import choice
numbers = [0, 1, 2, 'A', 3, 4, 'B', 6, 9, 'C', 'E', 5, 'T']
def num(*args):
    number = str(choice(args))
    return number
value = num(*numbers) + num(*numbers)
print(f'Number: {value}')

