label a1e1:
    show bg forest #placeholder

    mc "{i}Huff, puff. I never thought I would miss Japan's rush-hour trains…{/i}"
    
    "[mc_color] had made it to a forest. Generic Fantasy Town should be close by now."
    "Unfortunately, their lack of athleticism seemed to have come back to haunt them."

    mc "I swear if I ever make it back home I'll start going to the {size=+10}{i}gym.{/i}{/size}"
    mc "Maybe then I can get a girl…"

    "They keep huffing and puffing, completely out of breath as they make their way through the forest." 
    "{size=+20}Suddenly, they hear {i}gurgling{/i}.{/size}"

    mc "What's that? Ew!"

    show susan at center:
        zoom 0.5
        linear 1.0 zoom 1.5

    "They gag as a slime slides next to them."
    "It seems to reach for them, making all kinds of disgusting slime noises as it does so."

    mc "Stay back!"

    show susan at center:
        zoom 1.5
        linear 1.0 zoom 2.0
    mc "I said stay back!"

    menu:
        "Punch the slime":
            jump slime_fight
    
    define slime_hp = 4

    label slime_fight:
        if(slime_hp <= 0):
            jump slime_waifu
        menu:
            "Slime has {color=#0bc30b}[slime_hp]{/color} health left"              
            "{color=#d11212}Kick{/color}":
                $ my_num = renpy.random.randint(1,5)
                $ slime_num = renpy.random.randint(1,3)
                if(my_num > slime_num):
                    $ slime_hp -= 2
                    "You managed to kick the slime!"
                    jump slime_fight
                else:
                    "{color=#d11a0d}You Took damage{/color}"
                    jump slime_fight
            "{color=#cfa406}Punch{/color}":
                $ my_num = renpy.random.randint(2,4)
                $ slime_num = renpy.random.randint(1,3)
                if(my_num > slime_num):
                    $ slime_hp -= 1
                    "You managed punch the slime!"
                    jump slime_fight
                else:
                    "{color=#d11a0d}You took damage{/color}"
                    jump slime_fight

            "{color=#3f41d4}Dodge{/color}":
                $ my_num = renpy.random.randint(1,5)
                $ slime_num = renpy.random.randint(1,3)
                if(my_num > slime_num):
                    "You managed to dodge the slime."
                    jump slime_fight
                else:
                    "{color=#d11a0d}You took damage{/color}"
                    jump slime_fight

            "{color=#05b32e}Block{/color}":
                $ my_num = renpy.random.randint(1,3)
                $ slime_num = renpy.random.randint(1,1)
                if(my_num > slime_num):
                    "You managed to block."
                    jump slime_fight
                else:
                    "{color=#d11a0d}You took damage{/color}"
                    jump slime_fight

                
label slime_waifu:
    #slime explodes
    show susan at center
    sg "Ow ow ow…"
    sg "Huh? I seem to have {size=+5}{i}transformed{/i}{/size} somehow?"
    sg "Uhm…"
    show susan shy
    sg "W-w-w-what did you do to me?"
    
    mc "{alpha=0.8}{i}She's adorable. Extremely shy, sure. But adorable.{/i}{/alpha}"
    
    sg "Huh? W-w-w-what are you doing?"

    #Protagonist-kun takes her hands into his.

    mc "Are you the first member of my {b}harem{/b}?"

    sg "{size=+20}...What?{/size}"
    
    mc "My harem! Since I'm clearly now part of a bad anime plot I must have a harem!"
    mc "that you transformed from my, erm.." #light tap on the shoulder...

    sg "Actually, you punched me in the face…"

    mc "{size=+20}...then clearly that must mean that I’m destined to have a harem!{/size}"

    sg "I don't think that's how it works…"

    mc "Nonsense! Now, let's go, Slime-chan!" 
    mc "The town full of hot anime waifus is waiting for me!"
    $ sg = Character(name=CharactersInfo[2][1], who_color=CharactersInfo[2][2])

    sg "S-s-slime-chan? Who's that?"
    
    mc "Why, you, of course!"

    show bg cool 
    with dissolve

    "[mc_color] practically runs into town, dragging the poor [sg_color] behind them."

