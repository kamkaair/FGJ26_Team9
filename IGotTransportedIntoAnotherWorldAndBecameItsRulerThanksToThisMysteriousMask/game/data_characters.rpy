init:
    python:
        CharactersInfo = [
            ["Protagonist-kun", "Protagonist-kun","#dda732"],  #PROTAGONIST = 0  
            ["Mask", "Mask","#d30de1"],                        #MASK = 1
            ["Slime", "Slime-chan", "#3c92cb"],                 #SLIME_GIRL = 2
            ["Ara-ara", "Ayla", "#13c52b"],                      #PLANT_GIRL = 3
            ["Evelyn Morning-Glory", "Eve-tan", "#fdef2b"],       #LIGHT_GIRL = 4
            ["Tessa", "Nyan-chan", "#c78a06"],                   #CAT_GIRL = 5
            ["Man Behind The Scene","Big Boss-kun","#c83702"]   #BOSS_MAN = 6
            ] 

define mc = Character(name="Protagonist-kun", who_color="#dda732")
define mk = Character(name=CharactersInfo[1][0], who_color=CharactersInfo[1][2])
define sg = Character(name=CharactersInfo[2][0], who_color=CharactersInfo[2][2])
define pg = Character(name=CharactersInfo[3][0], who_color=CharactersInfo[3][2])
define lg = Character(name=CharactersInfo[4][0], who_color=CharactersInfo[4][2])
define cg = Character(name=CharactersInfo[5][0], who_color=CharactersInfo[5][2])
define bm = Character(name=CharactersInfo[6][0], who_color=CharactersInfo[6][2])

define mc_color = "{color=#dda732}" + CharactersInfo[0][0] + "{/color}"
define mk_color = "{color=#d30de1}" + CharactersInfo[1][1] + "{/color}"
define sg_color = "{color=#3c92cb}" + CharactersInfo[2][1] + "{/color}"
define pg_color = "{color=#13c52b}" + CharactersInfo[3][1] + "{/color}"
define lg_color = "{color=#fdef2b}" + CharactersInfo[4][1] + "{/color}"
define cg_color = "{color=#c78a06}" + CharactersInfo[5][1] + "{/color}"
define bm_color = "{color=#c83702}" + CharactersInfo[6][1] + "{/color}"
