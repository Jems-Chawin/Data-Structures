def create_table(content):
    arr = []
    for i in range(int(row)):
        lst = []
        for j in range(int(col)):
            lst.append(content[j])
        del content[:int(col)]
        arr.append(lst)
    return arr

def show_table(table):
    for i in table:
        print(i)

def get_table_index_min_row(table):
    cmp_rows = []
    for i in table:
        cmp_rows.append(min(i))
    return cmp_rows.index(min(cmp_rows))

def get_row_index_max_col(table, idx):
    return table[idx].index(max(table[idx]))

def get_max_value_in_col(table):
    col = []
    for i in table:
        col.append(i[get_row_index_max_col(table, get_table_index_min_row(table))])
    return max(col)

inp = input("input : ").split(',')
row,col = inp[0].split()
content = [int(x) for x in inp[1].split()]
table = create_table(content)
# print(table)
# show_table(table)
# print(get_table_index_min_row(table) ,get_row_index_max_col(table, get_table_index_min_row(table)))
max_val = get_max_value_in_col(table)
print(max_val)

'''
example test cases

input : 3 3,2 1 3 4 2 4 5 9 2
4

input : 4 4,86 98 30 84 77 9 44 51 66 15 80 65 48 97 84 70
86

input : 5 5,6 23 56 55 50 38 98 68 73 56 79 1 21 42 37 97 10 17 4 38 42 5 32 56 80
97
'''
