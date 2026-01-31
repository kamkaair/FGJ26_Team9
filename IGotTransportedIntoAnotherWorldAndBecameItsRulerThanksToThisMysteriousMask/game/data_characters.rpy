init:
    python:
        CharactersInfo = [
            ["Protagonist-kun", "Protagonist-kun","#dda732"],  #PROTAGONIST = 0  
            ["Mask", "Mask","#d30de1"],                        #MASK = 1
            ["Susan", "Slime-chan", "#3c92cb"],                 #SLIME_GIRL = 2
            ["Ara-ara", "Ayla", "#13c52b"],                      #PLANT_GIRL = 3
            ["Evelyn Morning-Glory", "Eve-tan", "#fdef2b"],       #LIGHT_GIRL = 4
            ["Tessa", "Nyan-chan", "#c78a06"],                   #CAT_GIRL = 5
            ["Man Behind The Scene","Big Boss-kun","#c83702"]   #BOSS_MAN = 6
            ] 

define mc = Character(name=CharactersInfo[0][0], who_color=CharactersInfo[0][2])
define mk = Character(name=CharactersInfo[1][0], who_color=CharactersInfo[1][2])
define sg = Character(name=CharactersInfo[2][0], who_color=CharactersInfo[2][2])
define pg = Character(name=CharactersInfo[3][0], who_color=CharactersInfo[3][2])
define lg = Character(name=CharactersInfo[4][0], who_color=CharactersInfo[4][2])
define cg = Character(name=CharactersInfo[5][0], who_color=CharactersInfo[5][2])
define bm = Character(name=CharactersInfo[6][0], who_color=CharactersInfo[6][2])