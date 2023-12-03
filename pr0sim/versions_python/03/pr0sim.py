#my imports
import constants
from util.fleet import Fleet
from util.unit import Unit

#needed imports
import random
import math
import copy

#performance
import time

#debug imports
import pprint
import json


def main():
    #Main is used for testing
    # Perf tests call the method Run
    sets = [
        {
            "attackers": {
                0: {
                    "name": "attacker", #for testing
                    "military_tech": 15,
                    "defence_tech": 15,
                    "shield_tech": 15,
                    "unit": {
                        204: 100000,
                        206: 5000,
                        207: 1000,
                        213: 500,
                        214: 10,
                        215: 1000
                    }
                }
            },
            "defenders": {
                0: {
                    "name": "deffer", #for testing
                    "military_tech": 15,
                    "defence_tech": 15,
                    "shield_tech": 15,
                    "unit": {
                        204: 100000,
                        206: 5000,
                        207: 1000,
                        213: 500,
                        214: 10,
                        215: 1000
                    }
                }
            }
        },
        {
            "attackers": {
                0: {
                    "name": "attacker", #for testing
                    "military_tech": 15,
                    "defence_tech": 15,
                    "shield_tech": 15,
                    "unit": {
                        205: 2,
                        206: 3
                    }
                },
                1: {
                    "name": "attacker", #for testing
                    "military_tech": 15,
                    "defence_tech": 15,
                    "shield_tech": 15,
                    "unit": {
                        204: 1,
                        206: 2
                    }
                }
            },
            "defenders": {
                0: {
                    "name": "deffer", #for testing
                    "military_tech": 15,
                    "defence_tech": 15,
                    "shield_tech": 15,
                    "unit": {
                        204: 2,
                        213: 3
                    }
                }
            }
        }
    ]

    
    
    
    fleetTF = 0
    defTF = 0

    data = sets[1]
    start_time = time.time()
    result = calculateAttack(data["attackers"], data["defenders"])
    print("--- %s seconds ---" % (time.time() - start_time))


def run(attackers, defenders):
    calculateAttack(attackers, defenders)

def initFleet(fleetId, fleet):
    newFleet = Fleet(fleetId, fleet["military_tech"], fleet["shield_tech"], fleet["defence_tech"])
    
    for unitId, amount in fleet["unit"].items():
        for ship in range(amount):
            newFleet.addShip(unitId)
    return newFleet  

def calculateAttack(attackers, defenders):
    
    #init Fleets as Classes
    attackerFleets = []
    defendersFleets = []
    for fleetId, fleet in attackers.items():
        attackerFleets.append(initFleet(fleetId, fleet))
    for fleetId, fleet in defenders.items():
        defendersFleets.append(initFleet(fleetId, fleet))

    for round in range(constants.MaxAttackRounds+1):
        totalShipsAttacker = 0
        totalShipsDefender = 0
        
        for fleet in attackerFleets:
            totalShipsAttacker += len(fleet.units)
        for fleet in defendersFleets:
            totalShipsDefender += len(fleet.units)
        
        
        if totalShipsAttacker > 0 and totalShipsDefender > 0 and round < constants.MaxAttackRounds:
            #FIGHT
            _fight(attackerFleets, defendersFleets)

            _destroy(attackerFleets)
            _destroy(defendersFleets)
            
            #Resotre Shields
            for fleet in attackerFleets:
                fleet.restoreShield()
            for fleet in defendersFleets:
                fleet.restoreShield()
        else:
            break
    
    if totalShipsAttacker <= 0 and totalShipsDefender > 0:
        won = "r" #defender
    elif totalShipsAttacker > 0 and totalShipsDefender <= 0:
        won = "a"; #attacker
    else:
        won = "w"; #draw
    
    #ToDo: Add

    return {
        'won': won,
    }

def _fight(attackers, defenders):

    #attackers shoot
    for fleet in attackers:
        for unit in fleet.units:
            _shoot(unit, defenders)
    
    #defenders shoot
    for fleet in defenders:
        for unit in fleet.units:
            _shoot(unit, defenders)

def _shoot(unit, defenders):
    #SHOOT
    count = 0

    #count all ships
    for fleet in defenders:
        count += len(fleet.units)

    ran = random.randint(0,count-1)
    count = 0
    victimShip = 0

    #check wich chip got selected
    for fleet in defenders:
        count += len(fleet.units)
        # if selected ship is higher count than current count
        # -> ship is not in this defenders fleet
        # -> check next defnder
        if ran < count:
            victimShipId = random.randint(0, len(fleet.units) - 1)
            victimShip = fleet.units[victimShipId]
            break
    

    if unit.attack * 100 > victimShip.shield:
        penetration = unit.attack - victimShip.shield
        if penetration >= 0:
            #+penetration
            victimShip.shield = 0
            victimShip.armor -= penetration #shoot at armor
        else:
            #-penetration
            victimShip.shield -= unit.attack #shoot at shield
        
        #check destruction
        #may be explode if armor < 0.7
        if math.floor(victimShip.id / 100) == 2 and not victimShip.explode:
            if victimShip.armor > 0 and victimShip.armor < 0.7 * victimShip.initialArmor:
                ran = random.randint(0, victimShip.initialArmor)
                if ran > victimShip.armor:
                    victimShip.explode = True

        #always explode if armor <=0
        if victimShip.armor <= 0 and not victimShip.explode:
            victimShip.explode = True
    
    #Rapid fire
    if victimShip.id in unit.sd:
        count = unit.sd[victimShip.id]
        ran = random.randint(0, count)
        if (ran < count):
            _shoot(unit, defenders)

def _destroy(attackers):
    for fleet in attackers:
        for unit in fleet.units[:]: #create copy to loop through to remove correct entry
                                    #rework later
            if unit.armor <= 0 or unit.explode:
                #destroy unit
                fleet.units.remove(unit)
    

if __name__ == "__main__":
    main()