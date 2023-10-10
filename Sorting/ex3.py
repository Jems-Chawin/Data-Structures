ret = []

def insertion_sort(arr, i, k):
    if i>=len(arr):
        return ret
    
    if i==0:
        ret.append(arr[i])
        return insertion_sort(arr, i+1, k)

    elif i>0:
        if i-k>=0 and arr[i]<ret[i-k]:
            return insertion_sort(arr, i, k+1)
        else:
            ret.insert(i-k+1,arr[i])
            if arr[i+1:] != []:
                print(f"insert {arr[i]} at index {i-k+1} : {ret} {arr[i+1:]}")
            else:
                print(f"insert {arr[i]} at index {i-k+1} : {ret}")
            return insertion_sort(arr, i+1, 1)
    
inp = [int(x) for x in input("Enter Input : ").split()]
result = insertion_sort(inp, 0, 1)
print("sorted")
print(result)

'''
example test cases

Enter Input : 1 2 3 4
insert 2 at index 1 : [1, 2] [3, 4]
insert 3 at index 2 : [1, 2, 3] [4]
insert 4 at index 3 : [1, 2, 3, 4] 
sorted
[1, 2, 3, 4]

Enter Input : 1 3 4 2
insert 3 at index 1 : [1, 3] [4, 2]
insert 4 at index 2 : [1, 3, 4] [2]
insert 2 at index 1 : [1, 2, 3, 4] 
sorted
[1, 2, 3, 4]
'''
