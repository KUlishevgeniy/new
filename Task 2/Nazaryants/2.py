a=input()
numbers = []
chisl = []
last_operation = None
for char in a:
    if char.isnumeric():
        chisl.append(char)
    else:
        num = int(''.join(chisl))
        chisl = []
        if last_operation:
            if last_operation == '+':
                numbers.append(num)
            elif last_operation == '-':
                numbers.append(-num)
            elif last_operation == '*':
                numbers[-1] *= num
            else:
                numbers[-1] /= num
        else:
            numbers.append(num)
        last_operation = char

num = int(''.join(chisl))
if last_operation == '+':
    numbers.append(num)
elif last_operation == '-':
    numbers.append(-num)
elif last_operation == '*':
    numbers[-1] *= num
else:
    numbers[-1] /= num
print(sum(numbers))