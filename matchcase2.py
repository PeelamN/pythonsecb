num = input('enter a number1:- ')
num =input ('enter a number2:-')
num =input('enter a operator')
match num:
    case '0':
        print('a+b')
    case '1':
        print('a-b')
    case '2':
        print('a*b')
    case  '3':
        print('a**b')
    case '4':
        print('a/b')
    case '5':
        print('a//b')
    case '6':
        print('a%b')
    case _:
        print('enter valid input')                          