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
    attackers = [   
        (
            165,{
                "player": {
                    "id": 1,
                    "military_tech": 12,
                    "defence_tech": 15,
                    "shield_tech": 10
                },
                "fleetDetail": {
                    "fleet_id": 165
                    #...
                },
                "unit": {
                    215: 5000,
                    213: 500,
                    211: 200,
                }
            }
        ),
        (
            166, {
                "player": {
                    "id": 1,
                    "military_tech": 12,
                    "defence_tech": 15,
                    "shield_tech": 10
                },
                "fleetDetail": {
                    "fleet_id": 166
                    #...
                },
                "unit": {
                    207: 5
                }
            }
        )
    ]
    
    defenders = [
        (
            0, {
                "player": {
                    "id": 7,
                    "military_tech": 10,
                    "defence_tech": 10,
                    "shield_tech": 10
                },
                "fleetDetail": {
                    "fleet_start_galaxy": 1
                    #...
                },
                "unit": {
                    215: 5000,
                    213: 500,
                    211: 200,
                }
            }
        )
    ]
    
    fleetTF = 0
    defTF = 0

    start_time = time.time()
    result = calculateAttack(attackers, defenders, fleetTF, defTF)
    print("--- %s seconds ---" % (time.time() - start_time))

    # Serializing json
    json_object = json.dumps(result, indent=4)
    
    # Writing to sample.json
    with open("result.json", "w") as outfile:
        outfile.write(json_object)


def run(attackers, defenders, FleetTF = 0, DefTF = 0, sim = False):
    calculateAttack(attackers, defenders, FleetTF, DefTF, sim)

def calculateAttack(attackers, defenders, FleetTF, DefTF, sim = False):
    pricelist = constants.PriceList
    CombatCaps = constants.CombatCaps
    resource = [] #Marker
    TRES = {
        'attacker': 0,
        'defender': 0
    }#Marker
    ARES = DRES = {
        'metal': 0,
        'crystal': 0
    }
    ROUNDA = []
    RF = []

    attackAmount = []
    defenseAmount = []

    #STARTDEF - snapshot of defense amount. Needed for 70% restore
    STARTDEF = []


    #calculate attackers fleet metal+crystal value
    for fleetID, attacker in attackers:
        for element, amount in attacker["unit"].items():
            ARES['metal'] += pricelist.get(element)['cost'].get(901) * amount
            ARES['crystal'] += pricelist.get(element)['cost'].get(902) * amount

    TRES['attacker'] = ARES['metal'] + ARES['crystal']


    #calculate defenders fleet metal+crystal value
    for fleetID, defender in defenders:
        for element, amount in defender["unit"].items():
            if element < 300:
                #ships
                DRES['metal'] += pricelist.get(element)['cost'].get(901) * amount
                DRES['crystal'] += pricelist.get(element)['cost'].get(902) * amount
            else:
                #defense
                if not STARTDEF[element]:
                    STARTDEF[element] = 0
            
            TRES['defender'] += pricelist.get(element)['cost'].get(901) * amount
            TRES['defender'] += pricelist.get(element)['cost'].get(902) * amount


    for roundNumber in range(constants.MaxAttackRounds+1):
        attArray = []
        defArray = []

        att = _initCombatValues(attackers, roundNumber == 0)
        deff = _initCombatValues(defenders, roundNumber == 0)
    
        ROUNDA.append({
            'attackers': copy.deepcopy(attackers),
            'defenders': copy.deepcopy(defenders),
            'attackA': copy.deepcopy(att['attackAmount']),
            'defenseA': copy.deepcopy(deff['attackAmount']),
            'infoA': copy.deepcopy(att['attArray']),
            'infoD': copy.deepcopy(deff['attArray'])
        })

        if att['attackAmount']['total'] > 0 and deff['attackAmount']['total'] > 0 and roundNumber < constants.MaxAttackRounds:
            #FIGHT
            fightResults = _fight(attackers, defenders, sim)

            _destroy(attackers)
            _destroy(defenders)
                    
            _restoreShields(attackers)
            _restoreShields(defenders)

            ROUNDA[roundNumber]['attack'] = fightResults['attack']
            ROUNDA[roundNumber]['defense'] = fightResults['defense']
            ROUNDA[roundNumber]['attackShield'] = fightResults['attackShield']
            ROUNDA[roundNumber]['defShield'] = fightResults['defShield']

        else:
            break
    
    if att['attackAmount']['total'] <= 0 and deff['attackAmount']['total'] > 0:
        won = "r" #defender
    elif att['attackAmount']['total'] > 0 and deff['attackAmount']['total'] <= 0:
        won = "a"; #attacker
    else:
        won = "w"; #draw
    
    #CDR
    for fleetID, attacker in attackers:
        for element, amount in attacker["unit"].items():

            TRES['attacker'] -= pricelist[element]['cost'][901] * amount
            TRES['attacker'] -= pricelist[element]['cost'][902] * amount

            ARES['metal'] -= pricelist[element]['cost'][901] * amount
            ARES['crystal'] -= pricelist[element]['cost'][902] * amount

    #restore defense (70% +/- 20%)
    DRESDefs = {
        'metal': 0,
        'crystal': 0
    }
    repairedDef = {}
    for fleetID, defender in defenders:
        for element, amount in defender["unit"].items():
            if element < 300:
                DRES['metal'] -= pricelist[element]['cost'][901] * amount
                DRES['crystal'] -= pricelist[element]['cost'][902] * amount

                TRES['defender'] -= pricelist[element]['cost'][901] * amount
                TRES['defender'] -= pricelist[element]['cost'][902] * amount
            else:
                TRES['defender'] -= pricelist[element]['cost'][901] * amount
                TRES['defender'] -= pricelist[element]['cost'][902] * amount

                lost = STARTDEF[element] - amount
                giveback = 0
                for i in range(lost):
                    if random.randint(1,100) <= 70:
                        giveback += 1
                defenders[fleetID]['unit'][element] += giveback
                
                if (lost > 0):
                    repairedDef[element]['units'] = giveback
                    repairedDef[element]['percent'] = giveback / lost * 100
                
                DRESDefs['metal'] += pricelist[element]['cost'][901] * (lost - giveback);
                DRESDefs['crystal'] += pricelist[element]['cost'][902] * (lost - giveback);



    ARES['metal'] = max(ARES['metal'], 0)
    ARES['crystal'] = max(ARES['crystal'], 0)
    DRES['metal'] = max(DRES['metal'], 0)
    DRES['crystal'] = max(DRES['crystal'], 0)
    TRES['attacker'] = max(TRES['attacker'], 0)
    TRES['defender'] = max(TRES['defender'], 0)

    totalLost = {
        'attacker': TRES['attacker'],
        'defender': TRES['defender']
    }
    debAttMet = ARES['metal'] * (FleetTF / 100)
    debAttCry = ARES['crystal'] * (FleetTF / 100)
    debDefMet = (DRES['metal'] * (FleetTF / 100)) + (DRESDefs['metal'] * (DefTF / 100))
    debDefCry = (DRES['crystal'] * (FleetTF / 100)) + (DRESDefs['crystal'] * (DefTF / 100))


    # Serializing json
    json_object = json.dumps(attackers)
    
    # Writing to sample.json
    with open("attack.json", "w") as outfile:
        outfile.write(json_object)
    
    # Serializing json
    json_object = json.dumps(defenders)
    
    # Writing to sample.json
    with open("def.json", "w") as outfile:
        outfile.write(json_object)

    return {
        'won': won,
        'debris': {
            'attacker': {
                901: debAttMet,
                902: debAttCry,
            },
            'defender': {
                901: debDefMet,
                902: debDefCry,
            }
        },
        'rw' : ROUNDA,
        'unitLost': totalLost,
        'repaired': repairedDef,
    }

def _fight(attackers, defenders, sim): #done
    attack = {
        'attack': 0,
        'shield': 0
    }
    defense = {
        'attack': 0,
        'shield': 0
    }

    #attackers shoot
    for fleetID, attacker in attackers:
        for unit in attacker["units"]:
            _shoot(copy.deepcopy(attacker['player']['id']), copy.deepcopy(unit), defenders, attack, sim)
    
    #defenders shoot
    for fleetID, defender in defenders:
        for unit in defender["units"]:
            _shoot(copy.deepcopy(defender['player']['id']), copy.deepcopy(unit), attackers, defense, sim)

    return{
        'attack': attack['attack'],
        'defense': defense['attack'],
        'attackShield': defense['shield'],
        'defShield': attack['shield']
    }

def _shoot(attacker, unit, defenders, ad, sim): #done
    #SHOOT
    pricelist = constants.PriceList
    CombatCaps = constants.CombatCaps
    count = 0
    
    for fID, defender in defenders:
        count += len(defender["units"])
    
    ran = random.randint(0,count-1)
    count = 0
    victimShip = 0
    initialArmor = 0

    for fID, defender in defenders:
        count += len(defender['units'])
        if ran < count:
            victimShipId = random.randint(0, len(defender['units']) - 1)
            victimShip = defender['units'][victimShipId]
            armorTech = (1 + (0.1 * defender['player']['defence_tech']))
            initialArmor = (pricelist[victimShip['unit']]['cost'][901] + pricelist[victimShip['unit']]['cost'][902]) / 10 * armorTech
            break
    
    ad['attack'] += unit['att']
    if unit['att'] * 100 > victimShip['shield']:
        penetration = unit['att'] - victimShip['shield']
        if penetration >= 0:
            #+penetration
            ad['shield'] += victimShip['shield']
            victimShip['shield'] = 0
            victimShip['armor'] -= penetration; #shoot at armor
        else:
            #-penetration
            ad['shield'] += unit['att']
            victimShip['shield'] -= unit['att']; #shoot at shield
        
        #check destruction
        if math.floor(victimShip['unit'] / 100) == 2 and not victimShip['explode']:
            if victimShip['armor'] > 0 and victimShip['armor'] < 0.7 * initialArmor:
                ran = random.randint(0, initialArmor)
                if ran > victimShip['armor']:
                    victimShip['explode'] = True
                    #Update advnced stats removed


        if (not sim and victimShip['armor'] <= 0 and not victimShip['explode']):
            victimShip['explode'] = True
            #Update advnced stats removed
    
    #Rapid fire
    if 'sd' in CombatCaps[unit['unit']]:
        for sdId,count in CombatCaps[unit["unit"]]["sd"].items():
            if (victimShip['unit'] == sdId):
                ran = random.randint(0, count)
                if (ran < count):
                    _shoot(copy.deepcopy(attacker), copy.deepcopy(unit), defenders, ad, sim)

def _destroy(attackers):
    for fleetID, attacker in attackers:
        for unit in attacker['units'][:]:
            if unit['armor'] <= 0 or unit['explode']:
                #destroy unit
                attacker['unit'][unit['unit']] -= 1
                attacker['units'].remove(unit)

def _restoreShields(fleets):
    CombatCaps = constants.CombatCaps

    for fleetID, attacker in fleets:
         shieldTech = (1 + (0.1 * attacker['player']['shield_tech']))
         for unit in attacker['units']:
            unit['shield'] = CombatCaps[unit['unit']]['shield'] * shieldTech

def _initCombatValues(fleets, firstInit=False): #done
    CombatCaps = constants.CombatCaps
    pricelist = constants.PriceList
    attackAmount = {
        'total': 0
    }
    attArray = {}

    for fleetID, attacker in fleets:
        attackAmount[fleetID] = 0

        # init techs
        attTech = 1 + (0.1 * attacker['player']['military_tech']);
        shieldTech = 1 + (0.1 * attacker['player']['shield_tech']);
        armorTech = 1 + (0.1 * attacker['player']['defence_tech']);

        if firstInit:
            attacker["techs"] = [attTech, shieldTech, armorTech]
            attacker["units"] = []
        
        #init single ships
        for element, amount in attacker["unit"].items():

            #dont randomize +/-20% of attack power. The random factor is high enough
            thisAtt = CombatCaps[element]['attack'] * attTech
            thisShield = CombatCaps[element]['shield'] * shieldTech
            thisArmor = (pricelist[element]['cost'][901] + pricelist[element]['cost'][902]) / 10 * armorTech

            attArray.setdefault(fleetID, {}).setdefault(element, {}).setdefault('def', 0)
            attArray.setdefault(fleetID, {}).setdefault(element, {}).setdefault('shield', 0)
            attArray.setdefault(fleetID, {}).setdefault(element, {}).setdefault('att', 0)

            for ship in range(amount):
                if firstInit: 
                    attacker['units'].append(
                        {
                            'unit': element,
                            'shield': thisShield,
                            'armor': thisArmor,
                            'att': thisAtt,
                            'explode': False
                        }
                    )
                
                attArray[fleetID][element]['def'] += attacker['units'][ship]['armor']
                attArray[fleetID][element]['shield'] += thisShield
                attArray[fleetID][element]['att'] += thisAtt
            
            

            attackAmount[fleetID] += amount
            attackAmount['total'] += amount

    return{
        'attackAmount': attackAmount,
        'attArray': attArray
    }

if __name__ == "__main__":
    main()