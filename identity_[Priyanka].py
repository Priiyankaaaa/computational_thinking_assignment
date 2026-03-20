# Task 1: Identity Investigation
#Integers
a = 10
print("Before: ", id(a))
a = 20
print("After:", id(a))

#String
s = "Hii"
print("\nBefore: ", id(s))
s = "Hello"
print("After:", id(s))

#List
l = [1, 2, 3]
print("\nBefore: ", id(l))
l.append(4)
print("After:", id(l))

#Tuple
t = (1, 2, 3)
print("\nBefore: ", id(t))
t = (4, 5, 6)
print("After:", id(t))

#Float
f = 3.14
print("\nBefore: ", id(f))
f = 4.1
print("After: ", id(f))
