class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits  # Dictionary: direction -> room name

    def info(self):
        print(f"\n{self.name}")
        print(self.description)
        print("Exits:", ", ".join(self.exits.keys()))


class Player:
    def __init__(self, start_room):
        self.current_room = start_room

    def move(self, direction, rooms):
        current_room = self.current_room
        exits = current_room.exits

        if direction not in exits:
            print("You can't go that way!")
        else:
            next_room_name = exits[direction]
            next_room = rooms[next_room_name]
            self.current_room = next_room
            print(f"You move {direction} to {next_room_name}")


def parse_maze_file(filename):
    # should return a dictionary: name -> room object
    room_dictionary = {}
    with open(filename, "r", encoding="utf-8") as file:

        room_line = file.readline()

        while room_line != "":
            stripped_room_line = room_line.strip()
            room_parts = stripped_room_line.split(": ")
            room_name = room_parts[1]

            description_line = file.readline()
            stripped_description_line = description_line.strip()
            description_parts = stripped_description_line.split(": ")
            description = description_parts[1]

            exit_line = file.readline()
            stripped_exit_line = exit_line.strip()
            exit_parts = stripped_exit_line.split(": ")
            exit_string = exit_parts[1]

            exit_strings = exit_string.split("; ") # ['north=Hallway1', 'east=DeadEnd1']
            exit_dictionary = {}
            for exit in exit_strings:
                # exit = 'north=Hallway1'
                direction, room_exit = exit.split("=")
                exit_dictionary[direction] = room_exit

            room = Room(room_name, description, exit_dictionary)
            room_dictionary[room_name] = room

            file.readline()

            room_line = file.readline()

    return room_dictionary


def main():
    rooms = parse_maze_file("maze.txt")
    player = Player(rooms["Entrance"])

    print("Welcome to the Maze Game!")
    player.current_room.info()

    playing = True
    while playing:
        print()
        command = input("> ")

        if command == "look":
            player.current_room.info()

        elif command.startswith("go"):
            # command = 'go north'
            direction = command.split(" ")[1]
            player.move(direction, rooms)

        elif command == "quit":
            print("Thanks for playing!")
            playing = False

        else:
            print("Unknown command. Try 'look', 'go <direction>', or 'quit'.")

        if player.current_room.name == 'Exit':
            playing = False
            print(player.current_room.description)

main()
