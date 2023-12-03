import sys
sys.path.append("..")

import constants

class Unit:
    def __init__(self, id, military_tech, shieldTech, defence_tech):
        self.id = id
        self._met = constants.PriceList[self.id]['cost'].get(901)
        self._kirs = constants.PriceList[self.id]['cost'].get(902)
        self._deut = constants.PriceList[self.id]['cost'].get(903)
        
        
        self.attack = constants.CombatCaps[self.id]['attack'] * military_tech
        self.initialShield = constants.CombatCaps[self.id]['shield'] * shieldTech
        self.shield = constants.CombatCaps[self.id]['shield'] * shieldTech
        self.initialArmor = (self._met + self._kirs) / 10 * defence_tech
        self.armor = (self._met + self._kirs) / 10 * defence_tech
        self.explode = False
        
        self.sd = constants.CombatCaps[self.id]['sd']
    
    def __str__(self):
        return f"""Ship {self.id}\nValues:\n attack:{self.attack}\n shield: {self.shield}\n armor: {self.armor}\n"""