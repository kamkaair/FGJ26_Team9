label a1e2:
    image bg black = "#0b681f"
    image tavern_text = Transform(Text("{color=#efc727} At the tavern..{/color}", size=60), yalign=0.5)

    show bg black
    show tavern_text
    "Click to continue..."
    hide tavern_text
    show bg bar

    show protagonist mask happy at left
    show susan at right
    mc "Haah… I’m so glad this place has a tavern."
    show protagonist mask at left
    "What about you, [sg_color]?"
    
    "The slime-girl drinks the last of her beer, feeling herself fill up with courage."
    
    sg "A-actually, my name is {color=#3c92cb}Susan…{/color}"
    $ sg = Character(name=CharactersInfo[2][0], who_color=CharactersInfo[2][2])

    "[mc_color] ignores this completely."

    show protagonist mask happy at left
    mc "Yeah yeah. So! What should we do next?"
    mc "I was thinking of a romantic date on a nearby beach..."

    "[mc_color] wiggles their eyebrows."

    show susan happy at right
    sg "I l-like the water..."

    mc "What's the spirit!"

    mc "So, what do you say?"

    mc "We could enjoy a not-so-long-because-I\m-out-of-shape"
    mc "walk along the coastline before going on a romantic swim in the bay at sunset!"

    show susan at right
    sg "Uhm? Well.. It does sound fun.."

    mc "I know right?"

    mc "So, [sg_color], shall we go on the first date of my life, culminating in-?"

    "They get interrupted by a random person bursting into the tavern."
    hide protagonist mask
    hide susan
    $ r = Character("Random Civilian")
    r "{size=+10}{b}Someone help! A plant monster has walked straight into town!{/b}{/size}"

    show protagonist mask surprised at center
    show susan surprised at right

    "There's people screaming outside."

    #show white 
    show white with dissolve
    "Suddenly, the plant monster bursts into the tavern."

    show kasvi at left

    mc "Whoa! What's this? Someone dares intrude on my epic date plans?"

    mc "[sg_color]! get somewhere safe!"

    show susan surprised:
        xalign 0.75
        linear 1.0 xalign 2.0

    pg "Shuffle shuffle."

    show protagonist mask angry at center
    mc "Oh wow, you seem way stronger than [sg_color]."

    mk "You know, if you punch it my powers will turn it into a {b}hot waifu{/b} as you seem to refer to them."

    show protagonist mask at center
    mc "Oh right, I totally forgot that."

    show protagonist mask angry at center 
    mc "Welp, here we go!"

    menu:
        "Punch the plant":
            pass

    define plant_hp = 8

    label plant_fight:
        show protagonist mask
        if(plant_hp <= 0):
            jump plant_waifu
        menu:
            "Slime has {color=#0bc30b}[plant_hp]{/color} health left"              
            "{color=#d11212}Kick{/color}":
                $ my_num = renpy.random.randint(1,5)
                $ plant_num = renpy.random.randint(1,3)
                if(my_num > plant_num):
                    $ plant_hp -= 2
                    show protagonist mask angry ###
                    "You managed to kick the slime!"
                    jump plant_fight
                else:
                    show protagonist mask sad ###
                    "{color=#d11a0d}You Took damage{/color}"
                    jump plant_fight
            "{color=#cfa406}Punch{/color}":
                $ my_num = renpy.random.randint(2,4)
                $ plant_num = renpy.random.randint(1,3)
                if(my_num > plant_num):
                    $ plant_hp -= 1
                    show protagonist mask angry ###
                    "You managed punch the slime!"
                    jump plant_fight
                else:
                    show protagonist mask sad ###
                    "{color=#d11a0d}You took damage{/color}"
                    jump plant_fight

            "{color=#3f41d4}Dodge{/color}":
                $ my_num = renpy.random.randint(1,5)
                $ plant_num = renpy.random.randint(1,3)
                if(my_num > plant_num):
                    show protagonist mask surprised
                    "You managed to dodge the slime."
                    jump plant_fight
                else:
                    show protagonist mask sad ###
                    "{color=#d11a0d}You took damage{/color}"
                    jump plant_fight

            "{color=#05b32e}Block{/color}":
                $ my_num = renpy.random.randint(1,3)
                $ plant_num = renpy.random.randint(1,1)
                if(my_num > plant_num):
                    show protagonist mask surprised
                    "You managed to block."
                    jump plant_fight
                else:
                    show protagonist mask sad ###
                    "{color=#d11a0d}You took damage{/color}"
                    jump plant_fight

label plant_waifu:
    show white
    "As [mc_color] punches the lights out of the plant monster, it transforms into a hot elf waifu!"

    hide white with dissolve
    show ayla neutral:
        xalign 0.3
        yalign 1.0 
        with dissolve
    hide kasvi

    pg "Huh… What was I doing..?"

    "The tall elf gets up, before setting her sights on [mc_color]."

    pg "I must thank you for freeing me of that awful curse."

    pg "It was most unpleasant."

    menu:
        "Ask about curse":
            pass

    show protagonist mask surprised
    mc "Huh? What curse?"

    pg "Oh? You don't know?"

    pg "The curse that's turned half this world into hideous monsters, of course."

    pg "I must ask, how did you manage to unto the curse, Masked Warrior?"

    mc "{size=-10}{i}{alpha=0.8}Err… Hey mask, could I get a little help here?{/alpha}{/i}{/size}"

    "The mask is once again silent."

    mc "{size=-10}{i}{alpha=0.8}Well then.. Time to improvise.{/alpha}{/i}{/size}"

    show protagonist mask happy

    mc "Ahem. I'm a great mage from a faraway land, "
    mc "and I've come here to save all innocents because I'm such a good person."

    mc "{size=-10}{i}{alpha=0.8}And I definitely deserve to get a girlfriend for all my troubles.{/alpha}{/i}{/size}" 

    show ayla happa at left
Elf (happy): “Ara ara… Such a strong mage you are, then.”

Elf (neutral): “My name is Ayla. It’s a pleasure to meet you.”

[Change elf’s name to Ayla]

Protagonist-kun (happy): “I see. It’s a pleasure to meet you, Ai-chan!”

Ayla (angry): “The name. Is. A-y-l-a.”

Ayla (angry): “If you do not wish for pain, you’ll keep that in mind.”

[Player choice: “Got it.” or “I think Ai-chan would be better…”]

[If “Ai-chan would be better.”]

Ayla: “So you have chosen death.”

[Game over]

Protagonist-kun (neutral): “Got it.”

[Susan comes back into frame]

Ayla (neutral): “And who’s this adorable little lady with you?”

Susan (neutral): “Oh, me..? My name is S-”

Protagonist-kun (neutral): “This is Slime-chan!”

Protagonist-kun (happy): “She was the first damsel in distress I rescued, and she fell madly in love with me thanks to my heroics!”

Susan (angry): “...not really..?”

Ayla (happy): “Oh, such a brave warrior you are, Masked One.”

Ayla (neutral): “Perhaps I should join forces with you, see if you’re the prophesized warrior who shall cleanse the curse from these lands.”

Protagonist-kun (happy): “Feel free to join my har-”

Protagonist-kun (neutral): “I-I mean crew! I’m always looking for more followers.”

Protagonist-kun (happy) [whispering]: “The fact that you’re a hot elf waifu also helps…”

Ayla (neutral): “Excellent! If you need help with magic, do let me know.”

Ayla (neutral): “I’m knowledgeable when it comes to the arcane, although I’m no master.”

Narrator: The three of them chat, until it’s time to go to sleep.

Narrator: To protagonist-kun’s dismay, the girls get a separate room of their own.

Ayla (angry): “It would be extremely inappropriate to share a bed with a member of another gender before marriage!”

Ayla (angry): “Now, good night!”

[Player choice: “Go to sleep” or “Stay up”]

[If “Stay up”]

Narrator: Protagonist-kun stays up late, watching the moon.

Protagonist-kun (neutral): “Huh, what on earth has my life turned into…”

Narrator: They keep watching the moon, until they fall asleep. A member of staff carries them to their room and dumps them on the bed.


