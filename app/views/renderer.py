

class Renderer:

    def __init__(self):
        pass

    def draw(self, dungeon):
        for y in range(dungeon.height):
            for row in [
                lambda r, nr, br: r.get_character() + (' - ' + str(r.get_weight(nr)) + ' - ' if r.has_passage(nr) else '       '),
                lambda r, nr, br: '|       ' if r.has_passage(br) else '',
                lambda r, nr, br: str(r.get_weight(br)) + '       ' if r.has_passage(br) else '',
                lambda r, nr, br: '|       ' if r.has_passage(br) else '',

            ]:
                for x in range(dungeon.width):
                    room = dungeon.get_room(x + (dungeon.width * y))
                    next_room = x + (dungeon.width * y) + 1
                    bottom_room = x + (dungeon.width * y) + dungeon.width

                    print(row(room, next_room, bottom_room), end='')

                print()

    def debug(self, dungeon):
        for key, value in dungeon.rooms.items():
            print(str(key) + str(value.get_passages()))

