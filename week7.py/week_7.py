#1
'''
def is_isogram(word):
    letters = {}
    for i in word:
        if i in letters:
            return False
        letters[i] = 1
    return True

print(is_isogram("algorism"))
print(is_isogram("password"))
print(is_isogram("Consecutive")) 

#2
def get_names(names):
    return list(names.values())
print(get_names({"01475": "steve", "87469": "Alice", "654123": "Bob"}))



#3
def find_oldest(ages):
    oldest = max(ages.values())
    for name, age in ages.items():
        if age == oldest:
            return name

print(find_oldest({"Emma": 71, "Jack": 45, "olivia": 15, "liam": 39}))



#4
def letter_count(word):
    dict = {}
    for i in word:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

print(letter_count("hello"))
print(letter_count("mississippi")) 



#Q5
receipt = {}
receipt["Side Salad"] = 6
receipt["Chicken Parm"] = 12
receipt["Cookie"] = 3

total = 0
for price in receipt.values():
    total += price
print("Total:", total)

'''
