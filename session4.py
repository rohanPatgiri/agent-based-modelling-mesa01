import mesa
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

class Sugar (mesa.Agent):
  #- contains an amount of sugar
  # Grows one amount of sugar each turn
  def __init__(self):
    print ("I am sugar")


class Spice(mesa.Agent):
    def __init__(self):
      print ("I am spice")


class Trader (mesa.Agent):
  # Trader
  # - has a metabolism for sugar and spice
  # - harvests and trades sugar and spice to survive and thrive
  def __init__(self):
    print ("I am a trader")


class SugarScapeG1mt (mesa.Model):
  '''
  A model class to manage Sugarscape with traders (G1mt)
  Book Used :  Growing Artificial Societies by Axtell and Epstein

  '''
  def __init__(self, width = 50, height = 50):
    #Initiate width and height of sugarscape
    self.width = width
    self.height = height

    # initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)

    # read in landscape file
    sugar_distribution = np.genfromtxt("sugar-map.txt")
    #print(sugar_distribution.shape)
    #print(sugar_distribution[30])
    spice_distribution = np.flip(sugar_distribution,1)
    plt.imshow(spice_distribution, origin = "lower")



