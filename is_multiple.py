n =int(input('Enter input n: '))
m =int(input('Enter input m: '))

def is_multiple(n, m):


    if (m%n == 0):
        print('divisible')
        return True
    else:
        print('not divisible')
        return False

is_multiple(n,m)