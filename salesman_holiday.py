from __future__ import print_function
import math
import random
from anneal import Annealer


def distance(a, b):
    """Calculates distance between two latitude-longitude coordinates."""
    R = 3963  # radius of Earth (miles)
    lat1, lon1 = math.radians(a[0]), math.radians(a[1])
    lat2, lon2 = math.radians(b[0]), math.radians(b[1])
    return math.acos(math.sin(lat1) * math.sin(lat2) +
                     math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * R


class TravellingSalesmanProblem(Annealer):

    """Test annealer with a travelling salesman problem.
    """
    
    # pass extra data (the distance matrix) into the constructor
    def __init__(self, state, distance_matrix, plan=0):
        self.distance_matrix = distance_matrix
        self.plan = plan
        super(TravellingSalesmanProblem, self).__init__(state)  # important! 

    def move(self):
        """Swaps two cities in the route."""
        if (self.plan == 0):
            a = random.randint(0, len(self.state) - 1)
            b = random.randint(0, len(self.state) - 1)
        else:
            a = random.randint(1, len(self.state) - 1)
            b = random.randint(1, len(self.state) - 1)
        self.state[a], self.state[b] = self.state[b], self.state[a]

    def energy(self):
        """Calculates the length of the route."""
        e = 0
        for i in range(len(self.state)):
            if (self.plan == 0) or ((i-1)%self.plan != 0):
                e += self.distance_matrix[self.state[i-1]][self.state[i]]
            else:
                e += self.distance_matrix[self.state[i-1]][self.state[0]] + self.distance_matrix[self.state[0]][self.state[i]]
        return e



def run_holiday(Din):

    distance_matrix=Din

    plan = 10
    state0 = 94

    # # initial state, a randomly-ordered itinerary
    # init_state = list(cities.keys())
    # random.shuffle(init_state)

    # create a distance matrix
    
    init_state = [ x for x in range(len(distance_matrix)) ]
    random.shuffle(init_state)



    while init_state[0] != state0:
        init_state = init_state[1:] + init_state[:1]  #
    print (init_state)
    tsp = TravellingSalesmanProblem(init_state, distance_matrix, plan)
    # since our state is just a list, slice is the fastest way to copy
    tsp.copy_strategy = "slice"  
    state, e = tsp.anneal()

    while state[0] != state0:
        state = state[1:] + state[:1]  # rotate NYC to start

    if (plan != 0):
        for i in range((len(distance_matrix)-2)/plan*plan,0,-plan):
            state = state[:i+1] + [state0] + state[i+1:]
    print("%i mile route:" % e)
    print(state)
    return state
    

