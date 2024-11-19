class World:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [['E' for _ in range(cols)] for _ in range(rows)]

    def display_world(self):
        for row in self.grid:
            print(" ".join(row))


# Create a 6x10 virtual world
world = World(6, 10)

# Display the empty virtual world
world.display_world()
