# Updates were made to the Spice Class and the SugarScapeG1mt Class
import mesa
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

class Sugar (mesa.Agent):
  #- contains an amount of sugar
  # Grows one amount of sugar each turn
  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar


class Spice(mesa.Agent):
    def __init__(self, unique_id, model, pos, max_spice):
      super().__init__(unique_id, model)
      self.pos = pos
      self.amount = max_spice
      self.max_spice = max_spice


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
  
    #initiate scheduler
    self.schedule = mesa.time.RandomActivationByType(self)


    #initiate sugar distribution
    
    # read in landscape file
    sugar_distribution = np.genfromtxt("sugar-map.txt")
    #print(sugar_distribution.shape)
    #print(sugar_distribution[30])
    spice_distribution = np.flip(sugar_distribution,1)
    #plt.imshow(spice_distribution, origin = "lower")

    agent_id = 0
    for _, (x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.grid.place_agent(sugar, (x,y))
        self.schedule.add(sugar)
        print(self.schedule.agents_by_type[Sugar][agent_id])
        agent_id +=1

      max_spice = spice_distribution[x,y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.grid.place_agent(spice, (x,y))
        self.schedule.add(spice)
        print(self.schedule.agents_by_type[Spice][agent_id])
        agent_id +=1

model = SugarScapeG1mt()
