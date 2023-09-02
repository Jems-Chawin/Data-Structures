# euclidean algorithm : a = bq + r 

def find_gcd(a,b):
    if b==0:
        return a
    else:
        r = a%b
        if r==0:
            return b
        else:
            return find_gcd(b,r)

def main():
    inp = [int(x) for x in input('Enter Input : ').split()]
    inp.sort()
    a = abs(inp[1])
    b = abs(inp[0])
    if a==0 and b==0:
        print('Error! must be not all zero.')
    else:
        print(f'The gcd of {inp[1]} and {inp[0]} is : {find_gcd(a,b)}')

if __name__ == '__main__':
    main()

'''
example test cases

Enter Input : 8 4
The gcd of 8 and 4 is : 4

Enter Input : 10 20
The gcd of 20 and 10 is : 10

Enter Input : 12 18
The gcd of 18 and 12 is : 6

Enter Input : -11 -45
The gcd of -11 and -45 is : 1

Enter Input : 0 0
Error! must be not all zero.
'''
