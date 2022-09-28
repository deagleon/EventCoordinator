guests = {}


def read_guestlist(file_name):
    text_file = open(file_name, 'r')
    sended_guest = None
    while True:
        line_data = text_file.readline().strip().split(",")
        sended_guest = yield line_data
        if sended_guest is not None:
            line_data = sended_guest.split(",")
        if len(line_data) < 2:
            # If no more lines, close file
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age


r = read_guestlist("guest_list.txt")
# Checkpoint 1
for i in range(1, 11):
    if i <= 9:
        next(r)
        # print(f'{i}{next(r)}')
    elif i == 10:
        # Send Jane's when count reachs 10
        r.send('Jane, 35')
        # print(f'{i}{next(r)}')
    i += 1

for i in range(1, 11):
    print(f'{i} {next(r)}')
# Checkpoint 4
# g_expression = ([guest, age] for guest, age in list(guests.items()) if age >= 21)
# for _ in g_expression:
#     print(_)
