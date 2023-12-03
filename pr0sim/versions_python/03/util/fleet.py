import sys
sys.path.append("..")

from util.unit import Unit


class Fleet:
    def __init__(self, fleetId, military_tech, shield_tech, defence_tech):
        self._id = fleetId
        self._military_tech = 1 + (0.1 * military_tech)
        self._shieldTech = 1 + (0.1 * shield_tech)
        self._defence_tech = 1 + (0.1 * defence_tech)
        
        self.units = []
    
    def addShip(self, shipId):
        self.units.append(Unit(shipId, self._military_tech, self._shieldTech, self._defence_tech))
        
    def restoreShield(self):
        for unit in self.units:
            unit.shield = unit.initialShield
        
    def __str__(self):
        result = f"Fleet: {self._id}\nTechs:\n military:{self._military_tech}\n shield:{self._shieldTech}\n defence:{self._defence_tech}\n"
        result += f"{len(self.units)} ships inside fleet:\n"
        for idx,ship in enumerate(self.units):
            result += str(idx) + " " + str(ship)
        return result + "\n"