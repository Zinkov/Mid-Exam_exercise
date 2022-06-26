queue = int(input())
cabin_capacity = 4
cabin_seats = [int(seat) for seat in input().split(' ')]

filled_seats = []

for taken_seats in cabin_seats:
    free_seats = cabin_capacity - taken_seats  # shows the amount of filled seats in a cabin
    if queue >= free_seats:
        queue -= cabin_capacity
        filled_seats.append(cabin_capacity)
    else:
        filled_seats.append(queue)
        queue -= queue

if queue > 0:
    print(f"There isn't enough space! {queue} people in a queue!")
    print('%s' % ' '.join(map(str, filled_seats)))
else:
    print("The lift has empty spots!")
    print('%s' % ' '.join(map(str, filled_seats)))
