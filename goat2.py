__author__ = 'root'

x = int (input ('Enter the first number: '))
y = int (input('Enter the second number: '))

print

def add(x,y):
    return (x + y)

def sub (x,y):
    return  (x -y)

def div (x,y):
    return  (x / y)

def multi (x,y):
    return  (x * y)



print '%d + %d = %d' % (x,y, add (x,y))
print '%d - %d = %d' % (x,y, sub (x,y))
print '%d / %d = %d' % (x,y, div (x,y))
print '%d * %d = %d' % (x,y, multi(x,y))