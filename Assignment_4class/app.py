##ch8
##build in module
import math
print(math.sqrt(12))
##user defind module
from Sum import add
print("Userdefinedmodule:", add(5,6))
##external module
import requests
response = requests.get("https://www.example.com")
print(response.status_code)
##basic import
import math
print(math.pi)
##import with Alias
import numpy as np
print(np.array([1, 2, 3]))
##import specific func
from math import sqrt, pi
print(sqrt(13))
print(pi)
##built in function
print("Hello World")
##user defined function
def my_function():
    print("Hello Brother")
my_function()
##fun with return value
def add(x,y):
    a = x + y
a = 20
b = 30
print("a = {} b= {} a+b = {} .format(a, b, result)")
##anonymous func
def add_two(x,y):
    return x + y
my_lambda = lambda x,y: x + y;
print(my_lambda(1,2))
#generator func
def simple_generator():
    yield 1
    yield 2
    yield 3
gen = simple_generator()
print(gen, ":", type(gen))
for value in gen:
    print(value, ":", type(gen))
 ##ch9
##try block
try:
    result = 7/0
except:
    print("An error occured")
    ##except block
try:
    result = 12/0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An unexpected error occured: {e}")
    ##else block
   
try:
    result = 12/0
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Division successful. Result: {result}")
##finally block
 
try:
    result = 12/0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Thi will always execute")
    #ch10
    ##w and a mode
file = open("example.py", "r")
content = file.read()
print("Before writting:")
print(content)
file.close()
##write
file = open("example.py", "w")
##write(string)
file = open("myfile.txt", "w")
file.write("hello")
file.close()
##readlines
with open("example.py", "r") as file:
    lines = file.readlines()
for line in lines:
    print(line.strip())
##ch11
##time.time()
import time
ticks = time.time()
print("no of ticks sice 1:00pm, 1 march,1975", ticks)
##current time
import time
localtime = time.localtime(time.time())
print("Local current time :", localtime)
##local time
import time
localtime = time.localtime(time.time())
print ("Local current time :", localtime)
##calender
import calendar
cal = calendar.month(2025, 1)
print ("Here is the calendar:")
print (cal)
#date time
from datetime import date

date1 = date(2024, 7, 19)
print("Date:", date1)
#strftime method
import datetime
x = datetime.datetime(2024, 2, 1)

print(x.strftime("%f"))
