

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
                    print(row(dungeon.get_room(x + (dungeon.width * y)), x + (dungeon.width * y) + 1, x + (dungeon.width * y) + dungeon.width), end='')

                print()

    def debug(self, dungeon):
        for key, value in dungeon.rooms.items():
            print(str(key) + str(value.get_passages()))

