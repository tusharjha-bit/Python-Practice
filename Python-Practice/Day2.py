# identify the data type
a = 3
b = 4.5
c = "hello"
d = True 
e = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# 2 questions 
a = 3
b = 4

print( a + b )
print( a - b )
print( a * b )
print( a / b )
print( a // b )
print( a % b )
print( a ** b )

# string operations
name = "tushar"

print(name)
print(name[0])
print(name[2])
print(name.upper())
print(len(name))

# list operations 
fruites = [ "apple", "banana", "mangoes" ]
print (fruites)
print(type(fruites))

fruites.append("grapes")
fruites.remove("banana")
print(fruites)

# tuple operations
numbers = (1,2,3,4,5)
print(numbers[1])
print(numbers[1]) 

#   set operations
nums = {1,2,4,4,5,6}
print(nums)

# dictionary operations
student = {"name": "tushar",
           "age": "20",
           "class": "12th"
           }
print(student)
print(student["name"])
print(student.keys())
print(student.values)
