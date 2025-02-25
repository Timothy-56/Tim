1.	
python
# Question no.1
hours = int(input("Enter number of hours: "))
seconds = hours * 3600
print(f"{hours} hours is equal to {seconds} seconds.")

python
# Question no.2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
total = num1 + num2
print(f"The sum of {num1} and {num2} is {total}.")
#Compare two numbers:
python
# Question no.3
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is bigger than {num2}.")
elif num1 < num2:
    print(f"{num2} is bigger than {num1}.")
else:
    print("Both numbers are equal.")
#Replace 'a' with '0' in a string:
#python
# Question no.4
text = input("Enter a text string: ")
new_text = text.replace('a', '0')	
print(f"Modified string: {new_text}")

#python
# Question no.5
text = input("Enter a text string: ")
length = len(text)
print(f"The length of the string is {length}.")

#python
# Question no.6
for i in range(1, 6):
    print(i)

python
# Question no.7
i = 1
while i <= 5:
    print(i)
    i += 1
python
# Question no.8
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
average = (num1 + num2) / 2
print(f"The average of {num1} and {num2} is {average}.")



# Question no.9
# Assuming a pattern like:
# 1 2 3
# 4 5 6
# 7 8 9

for i in range(1, 10):
    print(i, end=' ')
    if i % 3 == 0:
        print()

python
# Question no.10
var1 = 1
var2 = 2
var3 = "3"
print(var1 + var2 + var3)
#SOLUTION: This will result in an error because you cannot concatenate an integer with a string.

python
# Question no.11
var1 = 1
var2 = 2
var3 = "3"
print(var1, var2, var3)
#SOLUTION: The output will be 1 2 3

python
# Question no.12
a = 3 + 2 * 4 + 4
print(a)
SOLUTION: The output will be 15 (2*4 is done first, followed by addition).
13.	Output of the given Python code:
python
# Question no.13
x = 8 + 8 * 9
print(x)
SOLUTION: The output will be 80 (8*9 is done first, followed by addition).

python
# Question no.14
i = 8 + 8 * 9 + 9 * (10-9)
print(i)
SOLUTION: The output will be 90 (multiplication and operations inside parentheses are performed first).

python
# Question no.15
p, q, r = 10, 20, 30
print(p, q, r)
SOLUTION: The output will be 10 20 30
16.	Print letters separately using a For loop:
python
# Question no.16
text = input("Enter a text string: ")
for letter in text:
    print(letter)

python
# Question no.17
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

python
# Question no.18
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

python
# Question no.19
rows = 3
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=' ')
    print()

python
# Question no.20
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=' ')
    print()

