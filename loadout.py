import random
#A CUSTOM LOADOUT MAKER FOR SOLDIER! WILL NOT IMPLEMENT UI UNLESS INTOXICATED
primary = ["RCJP", "BGBZ", "CWMN", "ORGN", "BLBX", "DRHT", "STCK", "LBLN", "AIRS"]
secondary = ["SHTG", "BFBN", "GNBO", "BABA", "CONC", "MNTR", "RSSH", "RIBS", "BASE", "PNAT"]
melee = ["SHVL", "MRKT", "FPAN", "COOB", "HASH", "EQLZ", "PATR", "HAZA", "DIAC", "ESPL"]


while True:

    x = random.choice(primary)
    y = random.choice(secondary)
    z = random.choice(melee)

    cmnd = input(">> ")

    if cmnd == "roll":
        print(f"{x}, {y}, {z}")
        continue
        
    else:
        continue
    
        
