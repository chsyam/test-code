def valid_func(number, invalid_digits):
    while(number!=0):
        # if digit in invalid numbers then return false
        if str(number%10) in invalid_digits:
            return False
        number = number//10
    return True

num = int(input())
#From problem statement valid and invalid digits are:

valid_digits = "0125689"
invalid_digits = "347"

count = 0
start = 0

while(count != num):
    if valid_func(start, invalid_digits):
        count+=1
    start += 1
print(start)