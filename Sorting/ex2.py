def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

inp = [int(x) for x in input("Enter Input : ").split()]
data = list()
for i, e in enumerate(inp):
    if e >= 0:
        data.append(e)
        inp[i] = "x"
# print(inp)
sorted_data = quick_sort(data)
# print(sorted_data)
for i, e in enumerate(inp):
    if e == "x":
        inp[i] = sorted_data[0]
        sorted_data.pop(0)
print(*inp, sep=" ")

'''
example test cases

Enter Input : 6 3 -2 5 -8 2 -2
2 3 -2 5 -8 6 -2

Enter Input : 6 5 4 -1 3 0 2 -99 1
0 1 2 -1 3 4 5 -99 6
'''
