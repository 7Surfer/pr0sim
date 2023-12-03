
MaxAttackRounds = 6

PriceList = {
    202: { #KT
        'cost' : {
            901: 2000,
            902: 2000,
            903: 0,
            911: 0
        }
    },
    203: { #GT
        'cost' : {
            901: 6000,
            902: 6000,
            903: 0,
            911: 0
        }
    },
    204: { #LJ
        'cost' : {
            901: 6000,
            902: 6000,
            903: 0,
            911: 0
        }
    },
    205: { #SJ
        'cost' : {
            901: 6000,
            902: 4000,
            903: 0,
            911: 0
        }
    },
    206: { #Xer
        'cost' : {
            901: 20000,
            902: 7000,
            903: 0,
            911: 0
        }
    },
    207: { #SS
        'cost' : {
            901: 45000,
            902: 15000,
            903: 0,
            911: 0
        }
    },
    208: { #KOLO
        'cost' : {
            901: 10000,
            902: 20000,
            903: 10000,
            911: 0
        }
    },
    209: { #rec
        'cost' : {
            901: 10000,
            902: 6000,
            903: 2000,
            911: 0
        }
    },
    210: { #spio
        'cost' : {
            901: 0,
            902: 1000,
            903: 0,
            911: 0
        }
    },
    211: { #b
        'cost' : {
            901: 50000,
            902: 25000,
            903: 15000,
            911: 0
        }
    },
    212: { #sat
        'cost' : {
            901: 0,
            902: 2000,
            903: 500,
            911: 0
        }
    },
    213: { #z
        'cost' : {
            901: 60000,
            902: 50000,
            903: 15000,
            911: 0
        }
    },
    214: { #rip
        'cost' : {
            901: 5000000,
            902: 4000000,
            903: 1000000,
            911: 0
        }
    },
    215: { #sxer
        'cost' : {
            901: 30000,
            902: 40000,
            903: 15000,
            911: 0
        }
    },
}

CombatCaps = {
    202: { #KT
        'attack': 5,
        'shield': 10,
        'sd':{
            210: 5,
            212: 5
        }
    },
    203: { #GT
        'attack': 5,
        'shield': 25,
        'sd':{
            210: 5, #spio
            212: 5  #solar
        }
    },
    204: { #LJ
        'attack': 50,
        'shield': 10,
        'sd':{
            210: 5, #spio
            212: 5  #solar
        }
    },
    205: { #SJ
        'attack': 150,
        'shield': 25,
        'sd':{
            202: 3, #kt
            210: 5, #spio
            212: 5  #solar
        }
    },
    206: { #Xer
        'attack': 400,
        'shield': 50,
        'sd':{
            204: 6, #lj
            210: 5, #spio
            212: 5, #solar
            401: 10 #rak
        }
    },
    207: { #SS
        'attack': 1000,
        'shield': 200,
        'sd':{
            210: 5, #spio
            212: 5  #solar
        }
    },
    208: { #KOLO
        'attack': 50,
        'shield': 100,
        'sd':{
            210: 5, #spio
            212: 5  #solar
        }
    },
    209: { #rec
        'attack': 1,
        'shield': 10,
        'sd':{
            210: 5, #spio
            212: 5  #solar
        }
    },
    210: { #spio
        'attack': 0,
        'shield': 0,
    },
    211: { #b
        'attack': 1000,
        'shield': 500,
        'sd':{
            210: 5,  #spio
            212: 5,  #solar
            401: 20, #rak
            402: 20, #ll
            403: 10, #sl
            405: 10  #ion
        }
    },
    212: { #sat
        'attack': 0,
        'shield': 0,
    },
    213: { #z
        'attack': 2000,
        'shield': 500,
        'sd':{
            210: 5,  #spio
            212: 5,  #solar
            215: 2,  #sxer
            402: 10, #ll
        }
    },
    214: { #rip
        'attack': 200000,
        'shield': 50000,
        'sd':{
            202: 250,  #kt
            203: 250,  #gt
            204: 200,  #lj
            205: 100,  #sj
            206: 33,   #xer
            207: 30,   #ss
            208: 250,  #kolo
            209: 250,  #rec
            210: 1250, #spio
            211: 25,   #b
            212: 1250, #solar
            213: 5,    #z
            215: 15,   #sxer
            401: 200,  #rak
            402: 200,  #ll
            403: 100,  #sl
            404: 50,   #gaus
            405: 100   #ion
        }
    },
    215: { #sxer
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
}