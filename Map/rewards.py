class Reward:
  def __init__ (self, reward):
    self.reward = reward

  def get_reward(self):
    if self.reward == "Reward 1":
      world.energy /= 2
      print("")

    elif self.reward == "Reward 2":
      world.steps /= 2
      print("")
  