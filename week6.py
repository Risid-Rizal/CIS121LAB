'''
def hailstone_seq(n):
    result = [n]  
    while n != 1:
        if n % 2 == 0:   
            n = n // 2
        else:           
            n = 3 * n + 1
        result.append(n)   
    return result

print(hailstone_seq(25))
print(hailstone_seq(40))'''


def is_acronymn(s , list_of_words):
    if len(s) != len(list_of_words):
        return False
    if s.upper() != s:
        return False
    
    return True

print(is_acronymn("NASA", ["National", "Aeronautics", "Space", "Administration"]))
print(is_acronymn("FBI", ["lederal", "Bureau", "Investigation"]))

