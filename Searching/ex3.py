class DataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)
    
class hash:
    def __init__(self, table_size, max_collision):
        self.table_size = table_size
        self.max_collision = max_collision
        self.size = 0
        self.table = [None] * table_size

    def insert(self, data):
        if self.size == self.table_size:
            print("This table is full !!!!!!")
            exit(0)
        hash_index = sum([ord(ch) for ch in data.key]) % self.table_size
        for i in range(self.max_collision):
            index = (hash_index + pow(i, 2)) % self.table_size
            if self.table[index] is None:
                self.table[index] = data
                self.size += 1
                return

            print(f"collision number {i+1} at {index}")

        print("Max of collisionChain")

    def print_table(self):
        for idx, item in enumerate(self.table):
            print(f"#{idx+1}	{item}")
        print("---------------------------")

if __name__ == "__main__":
    print(" ***** Fun with hashing *****")
    table_input, data_input = input("Enter Input : ").split("/")
    table_size, max_collision = map(int, table_input.split())
    data_entries = data_input.split(",")

    hash_table = hash(table_size, max_collision)

    for entry in data_entries:
        key, value = entry.split()
        hash_table.insert(DataItem(key, value))
        hash_table.print_table()

'''
example test cases
 ***** Fun with hashing *****
Enter Input : 3 2/1+1 I,OnE Love,abcde I,#$ew2 KMITL,kk KMITL,z Love
#1	(1+1, I)
#2	None
#3	None
---------------------------
collision number 1 at 0
#1	(1+1, I)
#2	(OnE, Love)
#3	None
---------------------------
collision number 1 at 0
collision number 2 at 1
Max of collisionChain
#1	(1+1, I)
#2	(OnE, Love)
#3	None
---------------------------
#1	(1+1, I)
#2	(OnE, Love)
#3	(#$ew2, KMITL)
---------------------------
This table is full !!!!!!

 ***** Fun with hashing *****
Enter Input : 5 5/one Un,two Deux,three Trois,four Quatre,five Cinq,ten Dix,eleven Onze
#1	None
#2	None
#3	(one, Un)
#4	None
#5	None
---------------------------
#1	None
#2	(two, Deux)
#3	(one, Un)
#4	None
#5	None
---------------------------
collision number 1 at 1
collision number 2 at 2
#1	(three, Trois)
#2	(two, Deux)
#3	(one, Un)
#4	None
#5	None
---------------------------
#1	(three, Trois)
#2	(two, Deux)
#3	(one, Un)
#4	None
#5	(four, Quatre)
---------------------------
collision number 1 at 1
collision number 2 at 2
collision number 3 at 0
collision number 4 at 0
collision number 5 at 2
Max of collisionChain
#1	(three, Trois)
#2	(two, Deux)
#3	(one, Un)
#4	None
#5	(four, Quatre)
---------------------------
collision number 1 at 2
#1	(three, Trois)
#2	(two, Deux)
#3	(one, Un)
#4	(ten, Dix)
#5	(four, Quatre)
---------------------------
This table is full !!!!!!
'''
