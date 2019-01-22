items = ['mic','phone', 323.12, 3123.123,'justin','bag','cliff bars', 134]
str_items = []
num_items = []

for i in items:
    if isinstance(i, float) or isinstance(i, int):
        num_items.append(i)
    elif isinstance(i, str):
        str_items.append(i)
    else:
        pass
print(str_items)
print(num_items)


def parse_lists(some_list):
    str_list_items = []
    num_list_items = []
    for i in some_list:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items .append(i)
        else:
            pass
    return str_list_items, num_list_items


print (parse_lists(items))

sum([123,323,423])
def my_sum(abc):
    total = 0
    for i in abc:
        if isinstance(i, float) or isinstance( i, int):
            total += i
    return totalitems = ['mic','phone', 323.12, 3123.123,'justin','bag','cliff bars', 134]
str_items = []
num_items = []

for i in items:
    if isinstance(i, float) or isinstance(i, int):
        num_items.append(i)
    elif isinstance(i, str):
        str_items.append(i)
    else:
        pass
print(str_items)
print(num_items)


def parse_lists(some_list):
    str_list_items = []
    num_list_items = []
    for i in some_list:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items .append(i)
        else:
            pass
    return str_list_items, num_list_items


print (parse_lists(items))

sum([123,323,423])
def my_sum(abc):
    total = 0
    for i in abc:
        if isinstance(i, float) or isinstance( i, int):
            total += i
    return total

sum(items)
my_sum(items)


def count_sum(abc):
    total = 0
    for i in abc:
        if isinstance(i, float) or isinstance( i, int):
            total += 1
    return total

def my_avg(abc):

    the_sum = my_sum(abc)
    num_of_itmes = count_sum(abc)
    return the_sum/ (num_of_itmes * 1.0)

my_avg(items)



def count_sum(abc):
    total = 0
    for i in abc:
        if isinstance(i, float) or isinstance( i, int):
            total += 1
    return total
    items = ['mic','phone', 323.12, 3123.123,'justin','bag','cliff bars', 134]
str_items = []
num_items = []

for i in items:
    if isinstance(i, float) or isinstance(i, int):
        num_items.append(i)
    elif isinstance(i, str):
        str_items.append(i)
    else:
        pass
print(str_items)
print(num_items)


def parse_lists(some_list):
    str_list_items = []
    num_list_items = []
    for i in some_list:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items .append(i)
        else:
            pass
    return str_list_items, num_list_items


print (parse_lists(items))

sum([123,323,423])
def my_sum(abc):
    total = 0
    for i in abc:
        if isinstance(i, float) or isinstance( i, int):
            total += i
    return total

my_sum(items)


def count_sum(abc):
    total = 0
    for i in abc:
        if isinstance(i, float) or isinstance( i, int):
            total += 1
    return total
count_sum(itmes)


def my_avg(abc):

    the_sum = my_sum(abc)
    num_of_itmes = count_sum(abc)
    return the_sum/ (num_of_itmes * 1.0)

my_avg(items)
