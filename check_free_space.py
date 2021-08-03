# hi everyone
"""Hi everyone """
hello = 'Himanshu'
print(hello)

double_string = '''

WOW
O O
---
'''

print(double_string)

str1 = "Himanshu"
str2 = 'garg'
str3 = str1 + str2
print("Hello this is haimsnhu herer\n" + str3)



# type conversion and string concatination
print("hello" + '5')


a = str(100)

b = float(a)

c = type(b)

print(c)

string1 = "\tIt's a \" kind of \" day!\n"
print(string1)
name = "Mr. Sundar Pichai"
age = 50

print('hi! {name_of} You are {age_ge} year old'.format(name_of="Himanshu ",age_ge = 50))
# print(f "hi! " + name + " You are " + (str)age + " year old ")


print("\n\n")


python = 'I am PYHTON'

print(python[1:4])
print(python[1:])
print(python[:])
print(python[1:100])
print(python[-1])
print(python[-4])
print(python[:-3])
print(python[-3:])
print(python[::-1])

username = input("Enter your name")
password = input("Enter ur password")
length = len(password)
print(f'Hi {username}! Your password is ', '*' * length, f'  and is {length} characters long')


#list (data structure) works as arrays
li = [10,20,30,40,"Himanshu",True,30.343]
print(li[5])