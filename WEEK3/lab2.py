#created by Risid Rizal on 2023-09-12
#Q3

'''light_color = input("Enter the traffic light color (green, yellow, red): ").lower()


if light_color == "green":
    print("go")
elif light_color == "yellow":
    print("yield")
elif light_color == "red":
    print("stop")
else:
    print("Invalid color")'''


#Q4


'''age = int(input("Enter your age: "))
goal = input("Enter your athleticism goal: ").lower()


if 20 <= age <= 39:
    if goal == "above average":
        print("Your resting heart rate should be between 47–72.")
    elif goal == "below average":
        print("Your resting heart rate should be between 73–93.")
    else:
        print("Invalid athleticism goal.")
elif 40 <= age <= 59:
    if goal == "above average":
        print("Your resting heart rate should be between 46–71.")
    elif goal == "below average":
        print("Your resting heart rate should be between 72–94.")
    else:
        print("Invalid athleticism goal.")
elif 60 <= age <= 79:
    if goal == "above average":
        print("Your resting heart rate should be between 45–70.")
    elif goal == "below average":
        print("Your resting heart rate should be between 71–97.")
    else:
        print("Invalid athleticism goal.")
else:
    print("Age not in the valid range (20–79).")'''


#Q5 

'''a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print("Numbers in increasing order:", a, b, c)'''

#Q6
 
'''a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))   
c = int(input("Enter third integer: "))

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a 
if b < c:
    b, c = c, b

print("Numbers in decreasing order:", a, b, c)'''


#Q7

knuts = int(input("Enter amount in knuts: "))


knuts_in_sickle = 29
knuts_in_galleon = 17


galleons = knuts // knuts_in_galleon
knuts = knuts % knuts_in_galleon

sickles = knuts // knuts_in_sickle
knuts = knuts % knuts_in_sickle
print(f"{galleons} galleons, {sickles} sickles, {knuts} knuts")




