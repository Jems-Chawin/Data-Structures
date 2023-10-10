def get_array_sequence(inp):
    arr = []
    count = 1
    seq = []
    for i in inp:
        if len(arr) == 0:
            arr.append(i)
            print(count, arr, sep=' : ')
        else:
            if arr[-1] < i:
                count += 1
                arr.append(i)
                print(count, arr, sep=' : ')
            else:
                count += 1
                while arr[-1] >= i:
                    arr.pop()
                    if len(arr) == 0:
                        break
                arr.append(i)
                print(count, arr, sep=' : ')
        seq.append(arr.copy())
    return seq

def get_longest_length(seq):
    length = []
    for i in seq:
        length.append(len(i))
    return max(length)

inp = [int(x) for x in input("Data : ").split()]
seq = get_array_sequence(inp)
print("longest increasing subsequence :", get_longest_length(seq))

'''
example test cases

Data : 9 26 22 75 47
1 : [9]
2 : [9, 26]
3 : [9, 22]
4 : [9, 22, 75]
5 : [9, 22, 47]
longest increasing subsequence : 3

Data : 1 52 28 25 40 64 84 28 77 46
1 : [1]
2 : [1, 52]
3 : [1, 28]
4 : [1, 25]
5 : [1, 25, 40]
6 : [1, 25, 40, 64]
7 : [1, 25, 40, 64, 84]
8 : [1, 25, 28]
9 : [1, 25, 28, 77]
10 : [1, 25, 28, 46]
longest increasing subsequence : 5
'''
