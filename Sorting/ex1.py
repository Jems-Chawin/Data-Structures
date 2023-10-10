def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

data = [int(x) for x in input("Enter Input : ").split()]
sorted_data = quick_sort(data)
if sorted_data == data:
    print("Yes")
else:
    print("No")

'''
example test cases

Enter Input : -99 -1 0 1 2 3
Yes

Enter Input : 5252 -5 2630 -558
No

Enter Input : 9 10 99
Yes
'''
