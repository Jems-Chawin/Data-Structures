def find_min(l,i):
    if i == 0:
        return l[0]
    else:
        return min(l[i], find_min(l, i - 1))

inp = [int(x) for x in input('Enter Input : ').split()]
print(f'Min : {find_min(inp,len(inp)-1)}')

'''
example test cases

Enter Input : 8 7 10 1 5 4 2 6 3 9
Min : 1

Enter Input : -84 -230 -54845 -6 -1
Min : -54845
'''
