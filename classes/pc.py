import math

class pc:
    def __init__(self, STR, CON, DEX, WIS, INT, CHA, HP):
        self.STR = STR
        self.CON = CON
        self.DEX = DEX
        self.WIS = WIS
        self.INT = INT
        self.CHA = CHA
        self.HP = HP

    def plus(atr):
        return math.floor((atr-10)/2)


pc(18, 12, 14, 12, 10, 8, 32)

print(pc.plus(19))