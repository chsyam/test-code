string_one = input()
string_two = input()
last_char = string_two[-1]
frequency = 0
for i in string_one:
    if i == last_char:
        frequency += 1
print(frequency)