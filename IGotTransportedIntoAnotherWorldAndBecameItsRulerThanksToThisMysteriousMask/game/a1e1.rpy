label a1e1:
    show bg forest #placeholder
    show protagonist mask at left
    mc "{i}Huff, puff. I never thought I would miss Japan's rush-hour trains…{/i}"
    hide protagonist mask
    "[mc_color] had made it to a forest. Generic Fantasy Town should be close by now."
    "Unfortunately, their lack of athleticism seemed to have come back to haunt them."
    show protagonist mask at left 
    mc "I swear if I ever make it back home I'll start going to the {size=+10}{i}gym.{/i}{/size}"
    mc "Maybe then I can get a girl…"

    menu:
        "Wipe your forehead":
            "[mc_color] wipes their forehead. It doesn't help much in the summer heat."
            pass
        "Pause to take a breath":
            "[mc_color] stops and leans on their knees. They take a couple deep breaths."
            "They don't help much."
            pass

    hide protagonist mask 
    "{size=+20}Suddenly, they hear {i}gurgling{/i}.{/size}"

    show protagonist mask surprised at left 

    show slime:
        xalign 0.75
        yalign 1.0
        zoom 0.75
        linear 1.0 xalign 0.75
        linear 1.0 xalign 0.5

    mc "What's that? Ew!"


    "They gag as a slime slides next to them."
    "It seems to reach for them, making all kinds of disgusting slime noises as it does so."

    mc "Stay back!"

    show slime:
        xalign 0.5
        yalign 1.0
        zoom 0.75
        linear 1.0 xalign 0.5
        linear 1.0 xalign 0.3

    mc "I said stay back!"
    show protagonist mask angry
    menu:
        "Punch the slime":
            pass

    define slime_hp = 4

    label slime_fight:
        show protagonist mask
        if(slime_hp <= 0):
            jump slime_waifu
        menu:
            "Slime has {color=#0bc30b}[slime_hp]{/color} health left"              
            "{color=#d11212}Kick{/color}":
                $ my_num = renpy.random.randint(1,5)
                $ slime_num = renpy.random.randint(1,3)
                if(my_num > slime_num):
                    $ slime_hp -= 2
                    show protagonist mask angry ###
                    "You managed to kick the slime!"
                    jump slime_fight
                else:
                    show protagonist mask sad ###
                    "{color=#d11a0d}You Took damage{/color}"
                    jump slime_fight
            "{color=#cfa406}Punch{/color}":
                $ my_num = renpy.random.randint(2,4)
                $ slime_num = renpy.random.randint(1,3)
                if(my_num > slime_num):
                    $ slime_hp -= 1
                    show protagonist mask angry ###
                    "You managed punch the slime!"
                    jump slime_fight
                else:
                    show protagonist mask sad ###
                    "{color=#d11a0d}You took damage{/color}"
                    jump slime_fight

            "{color=#3f41d4}Dodge{/color}":
                $ my_num = renpy.random.randint(1,5)
                $ slime_num = renpy.random.randint(1,3)
                if(my_num > slime_num):
                    show protagonist mask surprised
                    "You managed to dodge the slime."
                    jump slime_fight
                else:
                    show protagonist mask sad ###
                    "{color=#d11a0d}You took damage{/color}"
                    jump slime_fight

            "{color=#05b32e}Block{/color}":
                $ my_num = renpy.random.randint(1,3)
                $ slime_num = renpy.random.randint(1,1)
                if(my_num > slime_num):
                    show protagonist mask surprised
                    "You managed to block."
                    jump slime_fight
                else:
                    show protagonist mask sad ###
                    "{color=#d11a0d}You took damage{/color}"
                    jump slime_fight

                
label slime_waifu:
    #slime explodes
    show white 


    "As their punch connects, the slime gets covered in bright light"
    "[mc_color] scrambles further back, worried about the slime" 
    "exploding and covering them in its nastiness."

    hide white with dissolve
    show susan:
        xalign 0.3
        yalign 1.0 
    with dissolve
    hide slime

    show protagonist mask surprised at left 
    sg "Ow ow ow…"
    show susan surprised at right
    sg "Huh? I seem to have {size=+5}{i}transformed{/i}{/size} somehow?"
    
    mc "Uhm…"
    
    show susan angry at right
    sg "W-w-w-what did you do to me?"
    
    show protagonist mask at left
    "{alpha=0.8}{i}She's adorable. Extremely shy, sure. But adorable.{/i}{/alpha}"
    
    menu:
        "Approach":
            pass
    show protagonist mask:
        xalign 0.25
        linear 1.0 xalign 0.5

    show susan surprised at right
    sg "Huh? W-w-w-what are you doing?"

    "[mc_color] takes her hands into his."

    show protagonist mask happy
    mc "Are you the first member of my {b}harem{/b}?"


    sg "{size=+20}...What?{/size}"
    
    mc "My harem!" 
    mc "Since I'm clearly now part of a bad anime plot {i}I must have a harem{/i}!"
    mc "And since you transformed from my, erm..." #light tap on the shoulder...

    show protagonist mask:
        xalign 0.5
    menu:
        "tap lightly on the shoulder":
            pass
    
    show susan angry at right
    sg "Actually, you punched me in the face…"

    show protagonist mask happy:
        xalign 0.5
    mc "{size=+20}...then clearly that must mean that I'm destined to have a harem!{/size}"

    show susan at right
    sg "I don't think that's how it works…"


    mc "Nonsense! Now, let's go, Slime-chan!" 

    mc "The town full of hot anime waifus is waiting for me!"
    
    show susan surprised at right
    sg "S-s-slime-chan? Who's that?"


    mc "Why, you, of course!"

    hide protagonist mask
    hide susan 
    show bg black 
    with dissolve
    "[mc_color] practically runs into town, dragging the poor [sg_color] girl behind them."


    jump a1e2

    

