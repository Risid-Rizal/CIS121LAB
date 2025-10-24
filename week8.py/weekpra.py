#Q7
'''def ascending_order(num1, num2= 5, num3=25):
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2

    return num1, num2, num3

print(ascending_order(2, 3, 1))
print(ascending_order(10, 1))  
print(ascending_order(50))

#Q15
def report_negative_odds(numbers):
    is_odds = []
    for num in numbers:
        if num < 0 and num % 2 != 0:
            is_odds.append(num)
    return is_odds

print(report_negative_odds([100,-57,12,1,-36,-15]) )
print(report_negative_odds([121,-101,36,-19,-6,0,21,-1]) )
print(report_negative_odds([-100,7,8437]) )'''

#Q14
def report_two_digit_numbers(numbers):
    two_digits = []
    for num in numbers:
        if 10 <= abs(num) <= 99:
            two_digits.append(num)
    return two_digits

print(report_two_digit_numbers([100,57,12,1]) )
print(report_two_digit_numbers([121,36,-19,-6,0,21]) )
print(report_two_digit_numbers([18547,564,1]) )