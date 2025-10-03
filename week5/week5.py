#1'''
'''def pyramid_volume(b, h):
    return round((b**2 * h) / 3, 2)

print(pyramid_volume(1, 2))

#2
import math 

def cone_volume(r, h):
    return round(math.pi * (r**2 * h )/ 3)

print(cone_volume(3, 3))


#8

def pool_time(grade, time):
    if grade == 'k' or (1 <= grade <= 3):
        return "9 AM" if time == "Morning" else "1 PM"
    elif 4 <= grade <= 8:
        return "10 AM" if time == "Morning" else "2 PM"
    elif 9 <= grade <= 12:
        return "11 AM" if time == "Morning" else "3 PM"
    
print (pool_time('k', "Morning"))
print (pool_time(5, "Afternoon"))   
print (pool_time(10, "Morning"))
print (pool_time(12, "Afternoon"))



#11

def convert_knuts(knuts):
    output = ""

    galleons = knuts // 493

    remaining_knuts = knuts - (galleons * 493)

    sickles = remaining_knuts // 29

    remaining_knuts = remaining_knuts - (sickles * 29)

    if galleons > 0:
        output += f"Galleon: {galleons}, "

    if sickles > 0:
        output += f"sickles: {sickles}, "
    
    if remaining_knuts > 0:
        output += f"knuts: {remaining_knuts}"
        
        return output

input_knuts = int(input("Enter amount in knuts: "))
print(convert_knuts(input_knuts))'''


#2

def is_fever(input_temp):

    unit = input_temp[-1]

    temp = float(input_temp[:-1])

    if unit == "F":
        return temp > 98.6
    elif unit == "C":
        return temp > 37
    else:
        return "Invalid unit"
    
print(is_fever("99 F"))






