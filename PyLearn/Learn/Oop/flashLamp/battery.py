class battery:
    def __init__(self):
        self.energy = 10

    def setEnergy(self, energy):
        self.energy = energy

    def getEnergy(self):
        return self.energy

    def decreaseEnergy(self):
        if self.energy == 0 or self.energy == 1:
            return
        elif self.energy >= 2:
            self.energy -= 2



