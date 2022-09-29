guests = {}


def read_guestlist(file_name):
    text_file = open(file_name, 'r')
    sended_guest = None
    line_data = []
    while True:
        sended_guest = yield line_data
        if sended_guest is not None:
            line_data = sended_guest.split(",")
        else:
            line_data = text_file.readline().strip().split(",")
            if len(line_data) < 2:
                # If no more lines, close file
                text_file.close()
                break

        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age


r = read_guestlist("guest_list.txt")
# Checkpoint 1
for i in range(1, 100):
    if i <= 9:
        next(r)
        # print(f'{i}{next(r)}')
    elif i == 10:
        # Send Jane's when count reachs 10
        r.send('Jane, 35')
        # print(f'{i}{next(r)}')
    else:
        try:
            next(r)
        except StopIteration:
            break

    i += 1
# i = 0
# for guest in guests:
#     print(f'{i+1}.{guest}')
#     i += 1
# Checkpoint 4
g_expression = ([guest, age] for guest, age in list(guests.items()) if age >= 21)
# for _ in g_expression:
#     print(_)
#Checkpoint 5

#Chicken, Beef, Fish.
def table_1():
    yield ('Chicken', 'Table 1', 'Seat 1')
    yield ('Chicken', 'Table 1', 'Seat 2')
    yield ('Beef', 'Table 1', 'Seat 3')
    yield ('Fish', 'Table 1', 'Seat 4')
    yield ('Chicken', 'Table 1', 'Seat 5')

def table_2():
    yield ('Chicken', 'Table 2', 'Seat 1')
    yield ('Chicken', 'Table 2', 'Seat 2')
    yield ('Beef', 'Table 2', 'Seat 3')
    yield ('Fish', 'Table 2', 'Seat 4')
    yield ('Chicken', 'Table 2', 'Seat 5')

def table_3():
    yield ('Chicken', 'Table 3', 'Seat 1')
    yield ('Chicken', 'Table 3', 'Seat 2')
    yield ('Beef', 'Table 3', 'Seat 3')
    yield ('Fish', 'Table 3', 'Seat 4')
    yield ('Chicken', 'Table 3', 'Seat 5')

def combined_tables():
    yield from table_1()
    yield from table_2()
    yield from table_3()


def assign_table(guests, generator):
    i = 1
    for guest in guests:
        # print(f'{i}.{(guest, next(generator))}')
        yield (guest, next(generator))
        i += 1

list_tables = assign_table(guests, combined_tables())
for table in list_tables:
    print(table)

