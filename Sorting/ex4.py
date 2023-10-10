class Monkey:
    def __init__(self, name, strength, intelligence, agility, id):
        self.name = name
        self.str = strength
        self.int = intelligence
        self.agi = agility
        self.id = id

    def __repr__(self):
        return f"{self.id - 1}-{self.name}"

def quick_sort(arr, order, attributes):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    pivot_key = custom_key(pivot, attributes)

    less = [monkey for monkey in arr if custom_key(monkey, attributes) < pivot_key]
    equal = [monkey for monkey in arr if custom_key(monkey, attributes) == pivot_key]
    greater = [monkey for monkey in arr if custom_key(monkey, attributes) > pivot_key]

    if order == 'A':
        return quick_sort(less, order, attributes) + equal + quick_sort(greater, order, attributes)
    else:
        return quick_sort(greater, order, attributes) + equal + quick_sort(less, order, attributes)

def custom_key(monkey, attributes):
    key = []
    for attr in attributes:
        value = getattr(monkey, attr, 0)
        key.append(value)
    return key

def main():
    inp = input("Enter Input: ")
    order, attr_pri, monkey_data = inp.split('/')
    attributes = attr_pri.split(',')
    monkeys = []

    monkey_data = monkey_data.split(',')
    id_counter = 0
    for data in monkey_data:
        id_counter += 1
        data_parts = data.split()
        name = data_parts[0]
        strength = int(data_parts[1]) if len(data_parts) > 1 else 0
        intelligence = int(data_parts[2]) if len(data_parts) > 2 else 0
        agility = int(data_parts[3]) if len(data_parts) > 3 else 0
        monkey = Monkey(name, strength, intelligence, agility, id_counter)
        monkeys.append(monkey)

    sorted_monkeys = quick_sort(monkeys, order, attributes)
    print(sorted_monkeys)

if __name__ == "__main__":
    main()

'''
example test cases

Enter Input: D/str,int,agi/caesar 100 10 100,kla 20 110 20,ton 20 111 10,non 20 110 20
[0-caesar, 2-ton, 1-kla, 3-non]

Enter Input: A/agi,name/future 1 99 120,gon 50 50 50,ruth 60 100 80,net 70 98 80,ruth 70 -1 80
[1-gon, 3-net, 2-ruth, 4-ruth, 0-future]

Enter Input: D//gon -1 -1 -1,dragon 1000 1000 1000,ryu 100 100 100
[0-gon, 1-dragon, 2-ryu]
'''
