class DataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)
    
class Hash:
    def __init__(self, table_size, max_collision, threshold):
        self.table_size = table_size
        self.max_collision = max_collision
        self.threshold = threshold
        self.table = [None] * table_size

    def isFull(self):
        cur, des = 0, int(self.table_size * self.threshold / 100)
        for i in self.table:
            if i is not None:
                cur += 1
        if cur >= des:
            return True
        return False
    
    def insert(self, value):
        if not self.isFull():
            idx = value % self.table_size

            if self.table[idx] is None:
                self.table[idx] = value

            elif self.table[idx] is not None:
                collision = 0
                print(f'collision number {collision + 1} at {idx}')

                while self.table[idx] is not None:
                    collision += 1
                    new_idx = (idx + collision * collision) % self.table_size

                    if collision >= self.max_collision:
                        print("****** Max collision - Rehash !!! ******")
                        return False
                    
                    if self.table[new_idx] is None:
                        self.table[new_idx] = value
                        break

                    print(f'collision number {collision + 1} at {new_idx}')
            return True
        
        else:
            print('****** Data over threshold - Rehash !!! ******')
            return False

    def print_table(self):
        for i in range(len(self.table)):
            print(f'#{i+1}'+ " " * (7-len(str(i+1))) + f'{self.table[i]}')

def find_next_prime(value):
    while value:
        value += 1
        for i in range(2, value):
            if value % i == 0:
                break
            if i == value - 1:
                return value

print(' ***** Rehashing *****')
inp = input('Enter Input : ').split('/')
table_size, max_collision, threshold = map(int, inp[0].split())
data_list = list(map(int, inp[1].split()))
hash = Hash(table_size, max_collision, threshold)

print('Initial Table :')
hash.print_table()
print('----------------------------------------')

lastAdd, notAll = -1, True
while notAll:
    for i in range(len(data_list)):
        if i >= lastAdd + 1:
            print(f'Add : {data_list[i]}')
        if not hash.insert(data_list[i]):
            hash = Hash(find_next_prime(hash.table_size * 2), max_collision, threshold)
            lastAdd = i
            break
        else:
            if i >= lastAdd:
                hash.print_table()
                print('----------------------------------------')
        if i == len(data_list) - 1:
            notAll = False

'''
example test cases
 ***** Rehashing *****
Enter Input : 5 1 67/1 6
Initial Table :
#1	None
#2	None
#3	None
#4	None
#5	None
----------------------------------------
Add : 1
#1	None
#2	1
#3	None
#4	None
#5	None
----------------------------------------
Add : 6
collision number 1 at 1
****** Max collision - Rehash !!! ******
#1	None
#2	1
#3	None
#4	None
#5	None
#6	None
#7	6
#8	None
#9	None
#10	None
#11	None
----------------------------------------

 ***** Rehashing *****
Enter Input : 5 1 10/1 6
Initial Table :
#1	None
#2	None
#3	None
#4	None
#5	None
----------------------------------------
Add : 1
****** Data over threshold - Rehash !!! ******
#1	None
#2	1
#3	None
#4	None
#5	None
#6	None
#7	None
#8	None
#9	None
#10	None
#11	None
----------------------------------------
Add : 6
****** Data over threshold - Rehash !!! ******
#1	None
#2	1
#3	None
#4	None
#5	None
#6	None
#7	6
#8	None
#9	None
#10	None
#11	None
#12	None
#13	None
#14	None
#15	None
#16	None
#17	None
#18	None
#19	None
#20	None
#21	None
#22	None
#23	None
----------------------------------------

 ***** Rehashing *****
Enter Input : 5 1 10/0 1 6 20
Initial Table :
#1	None
#2	None
#3	None
#4	None
#5	None
----------------------------------------
Add : 0
****** Data over threshold - Rehash !!! ******
#1	0
#2	None
#3	None
#4	None
#5	None
#6	None
#7	None
#8	None
#9	None
#10	None
#11	None
----------------------------------------
Add : 1
****** Data over threshold - Rehash !!! ******
#1	0
#2	1
#3	None
#4	None
#5	None
#6	None
#7	None
#8	None
#9	None
#10	None
#11	None
#12	None
#13	None
#14	None
#15	None
#16	None
#17	None
#18	None
#19	None
#20	None
#21	None
#22	None
#23	None
----------------------------------------
Add : 6
****** Data over threshold - Rehash !!! ******
#1	0
#2	1
#3	None
#4	None
#5	None
#6	None
#7	6
#8	None
#9	None
#10	None
#11	None
#12	None
#13	None
#14	None
#15	None
#16	None
#17	None
#18	None
#19	None
#20	None
#21	None
#22	None
#23	None
#24	None
#25	None
#26	None
#27	None
#28	None
#29	None
#30	None
#31	None
#32	None
#33	None
#34	None
#35	None
#36	None
#37	None
#38	None
#39	None
#40	None
#41	None
#42	None
#43	None
#44	None
#45	None
#46	None
#47	None
----------------------------------------
Add : 20
#1	0
#2	1
#3	None
#4	None
#5	None
#6	None
#7	6
#8	None
#9	None
#10	None
#11	None
#12	None
#13	None
#14	None
#15	None
#16	None
#17	None
#18	None
#19	None
#20	None
#21	20
#22	None
#23	None
#24	None
#25	None
#26	None
#27	None
#28	None
#29	None
#30	None
#31	None
#32	None
#33	None
#34	None
#35	None
#36	None
#37	None
#38	None
#39	None
#40	None
#41	None
#42	None
#43	None
#44	None
#45	None
#46	None
#47	None
----------------------------------------
'''
