def n_bought(money,price):
    return money//price

def w_exchange(n,wrap):
    sed = n%wrap
    dai = n//wrap
    x = sed + dai
    if n<wrap:
        return (0)
    else:
        return (dai,w_exchange(x,wrap))

def un_tuple(s):
    if isinstance(s,int):
        return s
    result = []
    for i in s:
        if isinstance(i,tuple):
            result.extend(un_tuple(i))
        else:
            result.append(i)
    return result

inp = [int(x) for x in input('Enter m, p, w: ').split()]
n = n_bought(inp[0],inp[1])
output = w_exchange(n,inp[2])
final = un_tuple(output)
if isinstance(final,list):
    final.append(n)
    print(sum(final))
else:
    print(final + n)

'''
example test cases

Enter m, p, w: 16 2 2
15

Enter m, p, w: 15 1 3
22

Enter m, p, w: 20 3 5
7
'''
