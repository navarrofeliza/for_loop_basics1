# Basic - Print all integers from 0 to 150.
for x in range(150):
    print(x)
    
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(1000):
    print(x*5)
    
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(100):
    if x % 5 == 0:
        print("Coding")
    if x % 10 == 0:
        print("Coding Dojo")
    else:
        print(x)
        
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.  UNFINISHED
sum = 0
for num in range (0,500000,1):
    if num % 2 != 0:
        sum = sum + num
    print(sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for num in range(2018,0,-1):
    if num % 4 == 0:
        print(num)
        
# Flexible Counter 
lowNum = 5
highNum = 20
mult = 3

for num in range(lowNum,highNum, 1):
    if num % mult == 0:
        print(num)