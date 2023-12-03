#my imports
import constants

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

def calculateAttack(attackers, defenders):

    for round in range(constants.MaxAttackRounds+1):

        att = _initCombatValues(attackers, round == 0)
        deff = _initCombatValues(defenders, round == 0)

        if att['attackAmount'] > 0 and deff['attackAmount'] > 0 and round < constants.MaxAttackRounds:
            #FIGHT
            _fight(attackers, defenders)

            _destroy(attackers)
            _destroy(defenders)
                    
            _restoreShields(attackers)
            _restoreShields(defenders)
        else:
            break
    
    if att['attackAmount'] <= 0 and deff['attackAmount'] > 0:
        won = "r" #defender
    elif att['attackAmount'] > 0 and deff['attackAmount'] <= 0:
        won = "a"; #attacker
    else:
        won = "w"; #draw
    
    #ToDo: Add

    return {
        'won': won,
    }

def _fight(attackers, defenders):

    #attackers shoot
    for fleetID, attacker in attackers.items():
        for unit in attacker["units"]:
            _shoot(unit, defenders)
    
    #defenders shoot
    for fleetID, defender in defenders.items():
        for unit in defender["units"]:
            _shoot(unit, attackers)

def _shoot(unit, defenders):
    #SHOOT
    pricelist = constants.PriceList
    CombatCaps = constants.CombatCaps
    count = 0


    #count all ships
    for fleetId, defender in defenders.items():
        count += len(defender["units"])
    
    ran = random.randint(0,count-1)
    count = 0
    victimShip = 0
    initialArmor = 0

    #check wich chip got selected
    for fleetId, defender in defenders.items():
        count += len(defender['units'])
        # if selected ship is higher count than current count
        # -> ship is not in this defenders fleet
        # -> check next defnder
        if ran < count:
            victimShipId = random.randint(0, len(defender['units']) - 1)
            victimShip = defender['units'][victimShipId]
            armorTech = (1 + (0.1 * defender['defence_tech']))
            initialArmor = (pricelist[victimShip['unit']]['cost'][901] + pricelist[victimShip['unit']]['cost'][902]) / 10 * armorTech
            break
    

    if unit['att'] * 100 > victimShip['shield']:
        penetration = unit['att'] - victimShip['shield']
        if penetration >= 0:
            #+penetration
            victimShip['shield'] = 0
            victimShip['armor'] -= penetration; #shoot at armor
        else:
            #-penetration
            victimShip['shield'] -= unit['att']; #shoot at shield
        
        #check destruction
        #may be explode if armor < 0.7
        if math.floor(victimShip['unit'] / 100) == 2 and not victimShip['explode']:
            if victimShip['armor'] > 0 and victimShip['armor'] < 0.7 * initialArmor:
                ran = random.randint(0, initialArmor)
                if ran > victimShip['armor']:
                    victimShip['explode'] = True
                    #Update advnced stats removed

        #always explode if armor <=0
        if victimShip['armor'] <= 0 and not victimShip['explode']:
            victimShip['explode'] = True
    
    #Rapid fire
    if 'sd' in CombatCaps[unit['unit']]:
        for sdId,count in CombatCaps[unit["unit"]]["sd"].items():
            if (victimShip['unit'] == sdId):
                ran = random.randint(0, count)
                if (ran < count):
                    _shoot(unit, defenders)

def _destroy(attackers):
    for fleetID, attacker in attackers.items():
        for unit in attacker['units'][:]:
            if unit['armor'] <= 0 or unit['explode']:
                #destroy unit
                attacker['unit'][unit['unit']] -= 1
                attacker['units'].remove(unit)

def _restoreShields(fleets):
    CombatCaps = constants.CombatCaps

    for fleetID, fleet in fleets.items():
         shieldTech = (1 + (0.1 * fleet['shield_tech']))
         for unit in fleet['units']:
            unit['shield'] = CombatCaps[unit['unit']]['shield'] * shieldTech

def _initCombatValues(fleets, firstInit=False):
    CombatCaps = constants.CombatCaps
    pricelist = constants.PriceList

    attArray = {}

    totalShips = 0
    for fleetId, fleet in fleets.items():
        # init techs
        attTech = 1 + (0.1 * fleet['military_tech']);
        shieldTech = 1 + (0.1 * fleet['shield_tech']);
        armorTech = 1 + (0.1 * fleet['defence_tech']);

        if firstInit:
            fleet["techs"] = [attTech, shieldTech, armorTech]
            fleet["units"] = []
        
        #init single ships
        for shipId, shipAmount in fleet["unit"].items():

            
            thisAtt = CombatCaps[shipId]['attack'] * attTech
            thisShield = CombatCaps[shipId]['shield'] * shieldTech
            thisArmor = (pricelist[shipId]['cost'][901] + pricelist[shipId]['cost'][902]) / 10 * armorTech


            attArray.setdefault(fleetId, {}).setdefault(shipId, {}).setdefault('def', 0)
            attArray.setdefault(fleetId, {}).setdefault(shipId, {}).setdefault('shield', 0)
            attArray.setdefault(fleetId, {}).setdefault(shipId, {}).setdefault('att', 0)


            # Create each ship as standalone
            for ship in range(shipAmount):
                if firstInit: 
                    fleet['units'].append(
                        {
                            'unit': shipId,
                            'shield': thisShield,
                            'armor': thisArmor,
                            'att': thisAtt,
                            'explode': False
                        }
                    )
                
                attArray[fleetId][shipId]['def'] += fleet['units'][ship]['armor']
                attArray[fleetId][shipId]['shield'] += thisShield
                attArray[fleetId][shipId]['att'] += thisAtt

            totalShips += shipAmount
    print(attArray)
    return{
        'attackAmount': totalShips,
        'attArray': attArray
    }

    

if __name__ == "__main__":
    main()