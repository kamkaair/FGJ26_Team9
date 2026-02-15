init:
    python:
        CharactersInfo = [
            ["Protagonist-kun", "Protagonist-kun","#dda732"],    #PROTAGONIST = 0  
            ["Mask", "Mask","#d30de1"],                          #MASK = 1
            ["Susan", "Slime-chan", "#3c92cb"],                  #SLIME_GIRL = 2
            ["Ayla", "Ai-chan", "#13c52b"],                      #PLANT_GIRL = 3
            ["Evelyn Morning-Glory", "Eve-tan", "#fdef2b"],      #LIGHT_GIRL = 4
            ["Tessa", "Nyan-chan", "#c78a06"],                   #CAT_GIRL = 5
            ["Truck-kun","Truck-kun","#c83702"],              #BOSS_MAN = 6
            ["Writer","Writer","#4a08c4"],                       #WRITER = 7
            ["Announcer","Announcer","#00d31c"],                 #ANNOUNCER = 8
            ] 

define mc = Character(name="Protagonist-kun", who_color="#dda732")
define mk = Character(name="Mask", who_color=CharactersInfo[1][2])
define sg = Character(name="Slime", who_color=CharactersInfo[2][2])
define pg = Character(name="Plant monster", who_color=CharactersInfo[3][2])
define lg = Character(name="Light monster", who_color=CharactersInfo[4][2])
define cg = Character(name="Tiger", who_color=CharactersInfo[5][2])
define bm = Character(name="Mysterious truck", who_color=CharactersInfo[6][2])
define wr = Character(name="Writer", who_color=CharactersInfo[7][2])
define ar = Character(name="Announcer", who_color=CharactersInfo[8][2])

define mc_color = "{color=#dda732}" + CharactersInfo[0][0] + "{/color}"
define mk_color = "{color=#d30de1}" + CharactersInfo[1][1] + "{/color}"
define sg_color = "{color=#3c92cb}" + CharactersInfo[2][1] + "{/color}"
define pg_color = "{color=#13c52b}" + CharactersInfo[3][1] + "{/color}"
define lg_color = "{color=#fdef2b}" + CharactersInfo[4][1] + "{/color}"
define cg_color = "{color=#c78a06}" + CharactersInfo[5][1] + "{/color}"
define bm_color = "{color=#c83702}" + CharactersInfo[6][1] + "{/color}"
define wr_color = "{color=#c83702}" + CharactersInfo[7][1] + "{/color}"
define ar_color = "{color=#c83702}" + CharactersInfo[8][1] + "{/color}"
