def partition(n, k=None):
    if n == 0:
        return [[]]
    if k is None:
        k = n
    if k == 0:
        return []

    partitions = []

    if k <= n:
        partitions += [[k] + tail for tail in partition(n - k, k)]

    partitions += partition(n, k - 1)
    return partitions

def add_tail(par,k):
    if len(par) == 0:
        return []
    else:
        return [[k] + par[0]] + add_tail(par[1:], k)
def print_partition_recursive(partitions,s, index=0):
    if index == s and index < len(partitions):
        print(". . .")
    elif index < len(partitions):
        print(" + ".join(map(str, partitions[index])))
        print_partition_recursive(partitions,s,index + 1)

def find_partitions(n,s):
    n,s = int(n.strip()), int(s.strip())
    if n<=0:
        partitions = [[n]]
    else:
        partitions = partition(n)
    print_partition_recursive(partitions,s)
    print(f"Total: {len(partitions)}")
    
n,s = input('Enter n, s: ').split()
find_partitions(n,s)

'''
example test cases

Enter n, s: 0 1
0
Total: 1

Enter n, s: 1 1
1
Total: 1

Enter n, s: 3 3
3
2 + 1
1 + 1 + 1
Total: 3

Enter n, s: 6 8
6
5 + 1
4 + 2
4 + 1 + 1
3 + 3
3 + 2 + 1
3 + 1 + 1 + 1
2 + 2 + 2
. . .
Total: 11

Enter n, s: 4 0
. . .
Total: 5
'''
