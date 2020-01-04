class Model:

    def __init__(self, brain):
        # The Model's Neural Network
        self.brain = brain
        # The Model's score
        self.score = 0
        # The Model's memory
        self.memory = []

    # The Model's decision making
    def think(self, obs):
       return self.brain.predict(obs)
    
