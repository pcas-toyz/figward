import time

def minutestoseconds(minutes):
    return minutes * 60

def timerbasic(totalLength, steps):
    currenttime = time.time().__round__
    targettime = currenttime + totalLength

class timeSequence:
    
    
    def __init__(self):
        self.sequence = []
    def __init__(self, totalLength, steps):
        self.sequence = []


    def addtimer(self, timer):
        self.sequence.append(timer)
        return self.sequence
        





