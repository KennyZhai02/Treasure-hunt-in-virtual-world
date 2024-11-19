import random

class World:

    def __init__(self, rows, cols, player_position, treasures, traps):
        self.player = Player(player_position)
        self.treasures = treasures
        self.traps = [Trap(*trap) for trap in traps]
        self.rows = rows
        self.cols = cols
        self.grid = [['E' for _ in range(cols)] for _ in range(rows)]

    def display_world(self):
        for row in self.grid:
            print(" ".join(row))

    def apply_traps(self):
        for trap in self.traps:
            trap_position, trap_type = trap
            if self.player.position == trap_position:
                if trap_type == "gravity":
                    self.player.apply_gravity_trap()
                elif trap_type == "speed":
                    self.player.apply_speed_trap()
                elif trap_type == "displacement":
                    self.player.apply_displacement_trap()
                elif trap_type == "remove_treasures":
                    self.remove_uncollected_treasures()
                    
    def move_player(self, direction):
        self.player.move(direction)
        self.apply_traps()

    def remove_uncollected_treasures(self):
        self.treasures = []
# Create a 6x10 virtual world
world = World(6, 10)

# Display the empty virtual world
world.display_world()

class Reward:
  def __init__ (self, reward):
    self.reward = reward

  def get_reward(self):
    if self.reward == "Reward 1":
      world.player.energy /= 2
      print("Reward applied: Energy halved")

    elif self.reward == "Reward 2":
      world.player.steps /= 2
      print("Reward applied: Speed halved")


class Player:
  def __init__(self, position):
      self.position = position
      self.energy = 100
      self.speed = 1
      self.last_direction = (0, 0)

  def move(self, direction):
      self.last_direction = direction
      new_position = (self.position[0] + direction[0] * self.speed,
                      self.position[1] + direction[1] * self.speed)
      self.position = new_position

class Trap:
    def __init__(self, position, trap_type):
        self.position = position
        self.trap_type = trap_type

    def apply_effect(self, player, world):
        if self.trap_type == "gravity":
            player.energy *= 2
        elif self.trap_type == "speed":                                        player.speed *= 0.5
        elif self.trap_type == "displacement":
            displacement = (player.last_direction[0] * 2, player.last_direction[1] * 2)
            new_position = (player.position[0] + displacement[0], player.position[1] + displacement[1])
            player.position = new_position
        elif self.trap_type == "remove_treasures":
            world.remove_uncollected_treasures()

# Simulate player movement
moves = [(1, 0), (1, 0), (0, 1), (1, 0), (1, 1), (1, 0), (1, 0)]
for move in moves:
    world.move_player(move)
    print(f"Player Position: {world.player.position}, Energy: {world.player.energy}, Speed: {world.player.speed}")
    print(f"Treasures: {world.treasures}")
    world.display_world()
    print()