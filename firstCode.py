import keyword  

print"Hello WOrld!")

# displaying the complete list using "kwlist()."  

"""print("The set of keywords in this version is: ")  
print( keyword.kwlist )  

a="gaurav"
b=[1,2,34]
c=1.22
d=(1,2,"sffdf")

print(type(a))
print(type(b))
print(type(c))
print(type(d))

var1=''
var2='[1,2,3,"gdgd"]'
var3=[1,2,"fff"]
var4=1

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

print(5/2)

print(12%5)

print(5//2)

print(2**2)
"""
sum=0
for i in range(1,6):
    sum += i
print(sum)

print(list(range(1,6)))

my_list = [1,2,3,4,5]

print(my_list[1:3])

a = 4+5j

print(type(a))

#b = int(input("Enter age:"))

#print(b)

b = "Hello, World!"

print(b[7:-1])

print(b.split()[1][:-1])

#is_student = input("Enter is stutent:")
"""
if is_student.lower() == "true":
    print("Yes, This is student")
else:
    print("No, This is not student")
"""
print(4**0.5)

#Write a List Comprehension to iterate through the given string: ‘pwskills’.
print(list( x for x in 'pwskills'))

""" Write a code to print odd numbers from 1 to 100 using list comprehension.
    Note: Use a list comprehension to create a list from 1 to 100 and use another List comprehension to filter out odd numbers. """

print([x for x in [ i for i in range(1, 50)] if x %2 != 0])