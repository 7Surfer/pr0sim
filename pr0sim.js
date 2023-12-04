constants = {
    MaxAttackRounds: 6,
    CombatCaps: {
        202: { //KT
            'attack': 5,
            'shield': 10,
            'sd':{
                210: 5,
                212: 5
            }
        },
        203: { //GT
            'attack': 5,
            'shield': 25,
            'sd':{
                210: 5, //spio
                212: 5  //solar
            }
        },
        204: { //LJ
            'attack': 50,
            'shield': 10,
            'sd':{
                210: 5, //spio
                212: 5  //solar
            }
        },
        205: { //SJ
            'attack': 150,
            'shield': 25,
            'sd':{
                202: 3, //kt
                210: 5, //spio
                212: 5  //solar
            }
        },
        206: { //Xer
            'attack': 400,
            'shield': 50,
            'sd':{
                204: 6, //lj
                210: 5, //spio
                212: 5, //solar
                401: 10 //rak
            }
        },
        207: { //SS
            'attack': 1000,
            'shield': 200,
            'sd':{
                210: 5, //spio
                212: 5  //solar
            }
        },
        208: { //KOLO
            'attack': 50,
            'shield': 100,
            'sd':{
                210: 5, //spio
                212: 5  //solar
            }
        },
        209: { //rec
            'attack': 1,
            'shield': 10,
            'sd':{
                210: 5, //spio
                212: 5  //solar
            }
        },
        210: { //spio
            'attack': 0,
            'shield': 0,
        },
        211: { //b
            'attack': 1000,
            'shield': 500,
            'sd':{
                210: 5,  //spio
                212: 5,  //solar
                401: 20, //rak
                402: 20, //ll
                403: 10, //sl
                405: 10  //ion
            }
        },
        212: { //sat
            'attack': 0,
            'shield': 0,
        },
        213: { //z
            'attack': 2000,
            'shield': 500,
            'sd':{
                210: 5,  //spio
                212: 5,  //solar
                215: 2,  //sxer
                402: 10, //ll
            }
        },
        214: { //rip
            'attack': 200000,
            'shield': 50000,
            'sd':{
                202: 250,  //kt
                203: 250,  //gt
                204: 200,  //lj
                205: 100,  //sj
                206: 33,   //xer
                207: 30,   //ss
                208: 250,  //kolo
                209: 250,  //rec
                210: 1250, //spio
                211: 25,   //b
                212: 1250, //solar
                213: 5,    //z
                215: 15,   //sxer
                401: 200,  //rak
                402: 200,  //ll
                403: 100,  //sl
                404: 50,   //gaus
                405: 100   //ion
            }
        },
        215: { //sxer
            'attack': 700,
            'shield': 400,
            'sd':{
                202: 3,
                203: 3,
                205: 4,
                206: 4,
                207: 7,
                210: 5,
                212: 5
            }
        },
        401 : { //rak
            'attack': 80,
            'shield': 20,
        }
    },
    PriceList: {
        202: { //KT
            'cost' : {
                901: 2000,
                902: 2000,
                903: 0,
                911: 0
            }
        },
        203: { //GT
            'cost' : {
                901: 6000,
                902: 6000,
                903: 0,
                911: 0
            }
        },
        204: { //LJ
            'cost' : {
                901: 3000,
                902: 1000,
                903: 0,
                911: 0
            }
        },
        205: { //SJ
            'cost' : {
                901: 6000,
                902: 4000,
                903: 0,
                911: 0
            }
        },
        206: { //Xer
            'cost' : {
                901: 20000,
                902: 7000,
                903: 2000,
                911: 0
            }
        },
        207: { //SS
            'cost' : {
                901: 45000,
                902: 15000,
                903: 0,
                911: 0
            }
        },
        208: { //KOLO
            'cost' : {
                901: 10000,
                902: 20000,
                903: 10000,
                911: 0
            }
        },
        209: { //rec
            'cost' : {
                901: 10000,
                902: 6000,
                903: 2000,
                911: 0
            }
        },
        210: { //spio
            'cost' : {
                901: 0,
                902: 1000,
                903: 0,
                911: 0
            }
        },
        211: { //b
            'cost' : {
                901: 50000,
                902: 25000,
                903: 15000,
                911: 0
            }
        },
        212: { //sat
            'cost' : {
                901: 0,
                902: 2000,
                903: 500,
                911: 0
            }
        },
        213: { //z
            'cost' : {
                901: 60000,
                902: 50000,
                903: 15000,
                911: 0
            }
        },
        214: { //rip
            'cost' : {
                901: 5000000,
                902: 4000000,
                903: 1000000,
                911: 0
            }
        },
        215: { //sxer
            'cost' : {
                901: 30000,
                902: 40000,
                903: 15000,
                911: 0
            }
        },
        401 : { //rak
            'cost' : {
                901: 2000,
                902: 0,
                903: 0,
                911: 0
            }
        }
    }
}

function perfTest(){
    const testset = {
        "attackers": {
            0: {
                "name": "attacker", //field for testing
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
                "name": "deffer", //field for testing
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
    }

    let results = []

    for (let index = 1; index <= 20; index++) {
        console.time('Run ' + index)
        let result = calculateAttack(testset.attackers, testset.defenders)
        console.timeEnd('Run ' + index)
        
        results.push(result)
    }

    console.log(getPrettyResults(results))
}

function run() {
    const attackers = {
        0: {
            "name": "attacker",
            "military_tech": 15,
            "defence_tech": 15,
            "shield_tech": 15,
            "unit": {
                205: 2,
                206: 3
            }
        },
        1: {
            "name": "attacker",
            "military_tech": 15,
            "defence_tech": 15,
            "shield_tech": 15,
            "unit": {
                204: 1,
                206: 2
            }
        }
    }
    const defenders = {
        0: {
            "name": "deffer",
            "military_tech": 15,
            "defence_tech": 15,
            "shield_tech": 15,
            "unit": {
                204: 1,
                205: 1,
                206: 1,
                207: 1,
                208: 1,
                209: 1,
            }
        }
    }
    console.time('calculateAttack')
    result = calculateAttack(attackers, defenders)
    console.timeEnd('calculateAttack')
    console.log(result)
    console.log(getPrettyResults([result]))
}


function getPrettyResults(results){
    let data = {
        "averrage": {
            "unitsLost" : {
                "attacker" : {},
                "defender" : {}
            }
        },
        "max": {
            "unitsLost" : {
                "attacker" : {},
                "defender" : {}
            }
        },
        "min": {
            "unitsLost" : {
                "attacker" : {},
                "defender" : {}
            }
        }
    }

    //Get All ships part in combat
    let unitIdsInCombat = []
    results.forEach(round => {
        for (const [fleetId, fleet] of Object.entries(round.attackerFleets)) {
            for (const [unitIndex, unitData] of fleet.destoryedUnits) {
                if (!unitIdsInCombat.includes(unitData.unit.id)){
                    unitIdsInCombat.push(unitData.unit.id)
                }
            }
            for (const [unitIndex, unit] of fleet.units) {
                if (!unitIdsInCombat.includes(unit.id)){
                    unitIdsInCombat.push(unit.id)
                }
            }
        }
        for (const [fleetId, fleet] of Object.entries(round.defendersFleets)) {
            for (const [unitIndex, unitData] of fleet.destoryedUnits) {
                if (!unitIdsInCombat.includes(unitData.unit.id)){
                    unitIdsInCombat.push(unitData.unit.id)
                }
            }
            for (const [unitIndex, unit] of fleet.units) {
                if (!unitIdsInCombat.includes(unit.id)){
                    unitIdsInCombat.push(unit.id)
                }
            }
        }
    })


    //calculate averrages
    let sum = {
        "attacker" : {},
        "defender" : {},
    }
    results.forEach(round => {
        //attacker
        for (const [fleetId, fleet] of Object.entries(round.attackerFleets)) {
            for (const [unitIndex, unitData] of fleet.destoryedUnits) {
                sum.attacker[unitData.unit.id] = sum.attacker[unitData.unit.id] + 1 || 1
            }
        }
        //defender
        for (const [fleetId, fleet] of Object.entries(round.defendersFleets)) {
            for (const [unitIndex, unitData] of fleet.destoryedUnits) {
                sum.defender[unitData.unit.id] = sum.defender[unitData.unit.id] + 1 || 1
            }
        }
    });
    for (const [unitId, amount] of Object.entries(sum.attacker)) {
        data.averrage.unitsLost.attacker[unitId] = amount / results.length
    }
    for (const [unitId, amount] of Object.entries(sum.defender)) {
        data.averrage.unitsLost.defender[unitId] = amount / results.length
    }

    //calculate max/min [of each ship]
    let max = {
        "attacker" : {},
        "defender" : {}
    }
    let min = {
        "attacker" : {},
        "defender" : {}
    }
    let roundSum = {}
    results.forEach(round => {
        //reset roundSum
        roundSum = {
            "attacker" : new Map(),
            "defender" : new Map()
        }
        //attacker
        for (const [fleetId, fleet] of Object.entries(round.attackerFleets)) {
            for (const [unitIndex, unitData] of fleet.destoryedUnits) {
                roundSum.attacker.set(unitData.unit.id, roundSum.attacker.get(unitData.unit.id) + 1)
                if (!roundSum.attacker.get(unitData.unit.id)){
                    roundSum.attacker.set(unitData.unit.id,1)
                }
            }
        }
        //defender
        for (const [fleetId, fleet] of Object.entries(round.defendersFleets)) {
            for (const [unitIndex, unitData] of fleet.destoryedUnits) {
                roundSum.defender.set(unitData.unit.id, roundSum.defender.get(unitData.unit.id) + 1)
                if (!roundSum.defender.get(unitData.unit.id)){
                    roundSum.defender.set(unitData.unit.id,1)
                }
            }
        }

        
        
        unitIdsInCombat.forEach(unitId => {
            //Attacker
            let amountAttacker = roundSum.attacker.get(unitId)
            let amountDefender = roundSum.defender.get(unitId)

            if (!amountAttacker){
                amountAttacker = 0
            }
            if (!amountDefender){
                amountDefender = 0
            }



            if ( max.attacker[unitId]) {
                if ( max.attacker[unitId] < amountAttacker){
                    max.attacker[unitId] = amountAttacker
                }
            }else{
                max.attacker[unitId] = amountAttacker
            }
            if ( min.attacker[unitId]) {
                if ( min.attacker[unitId] > amountAttacker){
                    min.attacker[unitId] = amountAttacker
                }
            }else{
                min.attacker[unitId] = amountAttacker
            }
            //Defender
            if ( max.defender[unitId]) {
                if ( max.defender[unitId] < amountDefender){
                    max.defender[unitId] = amountDefender
                }
            }else{
                max.defender[unitId] = amountDefender
            }
            if ( min.defender[unitId]) {
                if ( min.defender[unitId] > amountDefender){
                    min.defender[unitId] = amountDefender
                }
            }else{
                min.defender[unitId] = amountDefender
            }
        });
    });
    data.max.unitsLost.attacker = max.attacker
    data.max.unitsLost.defender = max.defender
    data.min.unitsLost.attacker = min.attacker
    data.min.unitsLost.defender = min.defender

    return data
}

function calculateAttack(attackers, defenders) {
    //init Fleets as Classes
    let attackerFleets = []
    let defendersFleets = []


    for (const [fleetId, fleet] of Object.entries(attackers)) {
        attackerFleets.push(initFleet(fleetId, fleet))
    }
    for (const [fleetId, fleet] of Object.entries(defenders)) {
        defendersFleets.push(initFleet(fleetId, fleet))
    }

    let round = 0
    for (; round <= constants.MaxAttackRounds; round++) {
        totalShipsAttacker = 0
        totalShipsDefender = 0

        for (const fleet of attackerFleets) {
            totalShipsAttacker += fleet.units.size
        }
        for (const fleet of defendersFleets) {
            totalShipsDefender += fleet.units.size
        }
            
        if ( totalShipsAttacker > 0 && totalShipsDefender > 0 && round < constants.MaxAttackRounds) {
            //FIGHT
            _fight(attackerFleets, defendersFleets)

            _destroy(attackerFleets, round)
            _destroy(defendersFleets, round)
            
            //Resotre Shields
            for (const fleet of attackerFleets) {
                fleet.restoreShield()
            }
            for (const fleet of defendersFleets) {
                fleet.restoreShield()
            }
        }
        else {
            break
        }
    }

        
    
    if (totalShipsAttacker <= 0 && totalShipsDefender > 0) {
        won = "defender" //defender
    }else if (totalShipsAttacker > 0 && totalShipsDefender <= 0 ){
        won = "attacker"; //attacker
    }else{
        won = "draw"; //draw
    }
    //ToDo: Add

    return {
        'won': won,
        'rounds': round,
        'attackerFleets': attackerFleets,
        'defendersFleets': defendersFleets
    }
}

function initFleet(fleetId, fleet){
    let newFleet = new Fleet(fleetId, fleet["military_tech"], fleet["shield_tech"], fleet["defence_tech"])
    
    for (const [unitId, amount] of Object.entries(fleet["unit"])) {
        for (let index = 0; index < amount; index++) {
            newFleet.addShip(unitId)
        }
    }
    return newFleet 
} 

function _fight(attackers, defenders){

    //attackers shoot
    for (const fleet of attackers) {
        for (const [unitId,unit] of fleet.units){
            _shoot(unit, defenders)
        }
    }
        
    //defenders shoot
    for (const fleet of defenders) {
        for (const [unitId,unit] of fleet.units){
            _shoot(unit, attackers)
        }
    }
}

function getRandomInt(max) {
    return Math.floor(Math.random() * (max + 1));
}


function _shoot(unit, defenders){
    //SHOOT
    count = 0

    //count all ships
    for (fleet of defenders) {
        count += fleet.units.size
    }
    
    
    ran = getRandomInt(count-1)
    count = 0
    victimShip = 0

    //check which ship got selected
    for (fleet of defenders) {
        count += fleet.units.size
        // if selected ship is higher count than current count
        // -> ship is not in this defenders fleet
        // -> check next defnder
        if (ran < count){
            //get random victim ship
            let shipId = getRandomInt(fleet.units.size-1)
            victimShip = fleet.units.get(shipId)
            break
        }
    }
    

    if (unit.attack * 100 > victimShip.shield) {
        penetration = unit.attack - victimShip.shield
        if (penetration >= 0){
            //+penetration
            victimShip.shield = 0
            victimShip.armor -= penetration //shoot at armor
        }else{
            //-penetration
            victimShip.shield -= unit.attack //shoot at shield
        }
        
        //check destruction
        //may be explode if armor < 0.7
        if (Math.floor(victimShip.id / 100) == 2 && !victimShip.explode){
            if (victimShip.armor > 0 && victimShip.armor < 0.7 * victimShip.initialArmor){
                ran = getRandomInt(parseInt(victimShip.initialArmor))
                if (ran > victimShip.armor){
                    victimShip.explode = true
                }
            }
        }

        //always explode if armor <=0
        if (victimShip.armor <= 0 && !victimShip.explode){
            victimShip.explode = true
        }
    }

    //Rapid fire recursive
    if (unit.sd) {
        for (const [sdUnitId, count] of Object.entries(unit.sd)) {
            if (victimShip.id == sdUnitId) {
                ran = getRandomInt(count)
                if (ran < count) {
                    _shoot(unit, defenders)
                }
            }
        }
    }
}
        

function _destroy(fleets, round){
    for (fleet of fleets) {
        //loop backwards to have stable _destroyShip function!
        for(let unitId = fleet.units.size-1; unitId >= 0 ;unitId--){
            const unit = fleet.units.get(unitId);
            if( unit.armor <= 0 || unit.explode){
                //destroy unit
                _destroyShip(fleet,unitId, unit, round)
            }
        }
    }
}

function _destroyShip(fleet, unitId, unit, round){
    //only for result
    fleet.destoryedUnits.set(fleet.destoryedUnitsCount, { "unit": unit, "round": round})
    fleet.destoryedUnitsCount +=1

    //Replace Destroyed ship with last ship in fleet
    const size = fleet.units.size
    
    // IF unit to destroy == last ship in fleet
    // Delete without replacing
    if(unitId == size-1){
        fleet.units.delete(unitId)
        return
    }

    //destoryed ship is replaced with its successor.
    //last ship gets deleted
    for (let i = unitId; i+1 < size; i++) {
        fleet.units.set(i, fleet.units.get(i+1)
    }
    fleet.units.delete(size-1)
    
}


class Fleet {
    constructor(fleetId, military_tech, shield_tech, defence_tech){
        this._id = fleetId
        this._military_tech = 1 + (0.1 * military_tech)
        this._shieldTech = 1 + (0.1 * shield_tech)
        this._defence_tech = 1 + (0.1 * defence_tech)
        
        this.units = new Map()
        this.unitAmount = 0

        //test
        this.destoryedUnits = new Map()
        this.destoryedUnitsCount = 0
    }

    addShip(shipId){
        this.units.set(this.unitAmount,new Unit(shipId, this._military_tech, this._shieldTech, this._defence_tech))
        this.unitAmount ++
    }

    restoreShield(){
        for (const [unitId,unit] of this.units) {
            unit.shield = unit.initialShield
        }
    }
}


class Unit {
    constructor(id, military_tech, shieldTech, defence_tech){
        this.id = id
        this._met = constants.PriceList[this.id]['cost'][901]
        this._kirs = constants.PriceList[this.id]['cost'][902]
        this._deut = constants.PriceList[this.id]['cost'][903]
        
        
        this.attack = constants.CombatCaps[this.id]['attack'] * military_tech

        this.initialShield = constants.CombatCaps[this.id]['shield'] * shieldTech
        this.shield = constants.CombatCaps[this.id]['shield'] * shieldTech

        this.initialArmor = (this._met + this._kirs) / 10 * defence_tech
        this.armor = (this._met + this._kirs) / 10 * defence_tech

        this.explode = false
        
        this.sd = constants.CombatCaps[this.id]['sd']
    }
}


