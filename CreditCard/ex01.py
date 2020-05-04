class ClassRoom:

    def __init__(self, number, capacity, number_of_machines, size):
        self.crnumber = number
        self.crcapacity = capacity
        self.crnumber_of_machines = number_of_machines
        self.crsize = size


    def getNumber(self):
        return self.crnumber
    def getCapacity(self):
        return self.crcapacity
    def getNumMach(self):
        return self.crnumber_of_machines
    def getSize(self):
        return self.crsize