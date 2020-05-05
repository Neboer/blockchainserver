import sys

# n =int(input())
# sum_s =0
# for i in range(n):
#     sum_s+=int(input())
# print('The sum is %d.' % sum_s)
try:
    n = int(input())
except ValueError as error:
    print("Error: input contents invalid.")
    sys.exit(0)
else:
    sum_s = 0
    num = 0
    for i in range(n):
        inputs = input()
        if inputs == '':
            break
        else:
            try:
                value = int(inputs)
            except ValueError as error:
                print("Error: input contents invalid.")
                sys.exit(0)
            else:
                sum_s += value
                num += 1
    if n != num:
        print("Error: data quatity invalid.")
        sys.exit(0)
    print('The sum is %d.' % sum_s)
