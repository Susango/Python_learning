a_input = input('Please give a number:')#这种情况input输入的是字符串'1',若要更改类型加int()
if a_input == '1':
    print("This is a good one.")
elif a_input == str(2):
    print("This is a wrong number.")
else:
    print('Good luck.')