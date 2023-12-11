def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):

    room = 1
    out = []
    for name in names:
        out.append(f"Hello, {name}! You'll be assigned to room {room}!")
        room += 1
    return out

def printer(names):
    for name in names:
        print(badge_maker(name))
    rooms = assign_rooms(names)
    for room in rooms:
        print(room)
