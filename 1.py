def three_base_number(number):
    base_3 = ""
    while(number!=0):
        base_3 = str(number%3) + base_3
        number = number // 3
    return base_3

number = int(input())
print(three_base_number(number))