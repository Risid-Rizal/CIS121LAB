# Lab 4: While Loops
#1
'''larger = int(input("Enter the larger integer: "))
smaller = int(input("Enter the smaller integer: "))

count = 0
while larger/2 > smaller:
        count += 1
        larger /= 2  

print("The result should be ", larger, count)

#2
user_word = input("Enter a word: ")
for i in range(1 ,len(user_word), 2):
      print(user_word[i], end="")

#3
for i in range(38, 1050, 2):
        print(i)

#4
letter = ""
word = ""
while letter != "done":
    word+= letter
    letter = input("Enter a letter: ")
print(f"You entered: {word}")

#Q5
sum = 0
for i in range(51, 518, 2):
        sum += i
print(sum)

#6
number = 0
sum = 0
while number >= 0:
        sum += number
        number = int(input("Enter a number: "))
print("The sum is:", sum)

#7
#hailstone sequence n is even divide by 2, n id odd multiply by 3 and add 1, continue until n is 1

n = int(input("Enter a positive integer: "))
print(n)
while n != 1:
        if n % 2 == 0:
                n = n // 2
        else:
                n = 3 * n + 1
        print(n)'''



import math

def pyramid_volume(b, h):
    return round((b**2 * h) / 3, 2)
print(pyramid_volume(1, 2))




