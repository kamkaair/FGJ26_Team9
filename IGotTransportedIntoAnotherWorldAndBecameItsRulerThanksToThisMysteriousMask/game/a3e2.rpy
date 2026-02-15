label a3e2:
    show textTavern
    "Click to continue..."

    scene bg bar
    with dissolve

    show protagonist mask neutral at center:
        xalign 0.15

    "Time passes by quickly. With four brand new friends in tow, our [mc_color] enters the Town Mayor's Selection."
    "They listen to the cheers from the audience, mentally psyching themself until it's their turn to enter the stage."

    wr "Ok ok ok. Pause! Pause! Everyone, pause!"

    menu:
        "What?":
            wr "Look, this is a free game made for Global Game Jam. We don't have the time or the energy or the budget to actually write a tournament arc"  

    menu:
        "But I want the story?":
            wr "Also, tournaments are stupidly difficult to write. Just ask anyone who's ever written M* He*o Aca*emia fanfiction. So I'll just..."  
            wr "(Insert epic tournament here)"
            wr "There. Now no one's happy >:D"
    
    menu:
        "Well fuck you too":
            wr "And anyway, we're making a parody about common isekai anime tropes. Everyone knows Protagonist-kun is going to win this thing. We can just get back to the story now..."
    
    menu:
        "Continue story":
            ar "And now, for the final fight!!"
            ar "Iiiin the left corner, we have the newcomer, the {color=#dda732}Masked Mystery Man{/color}, the one and only! Theeee [mc_color]!!!"
            wr "What the hell, how did that end up here?!?"

    menu:
        "Serves you right!":
            pass
    
    wr "Welp, guess we're doing the boss fight. Whatever. Enjoy, I guess?"

    show protagonist mask surprised
    mc "...Why is the tournament held in the tavern..?"

    wr "Because we didn't have time to make a colosseum."

    $ bm = Character(name=CharactersInfo[6][0], who_color=CharactersInfo[6][2])
    ar "And iiiin the right corner, we have the reigning champion of the last decade, the mysterious being we keep seeing in every isekai anime, the instigating incident! Theeeeee [bm_color]!!!"

    show truck at center:
        xalign 1.6
        xzoom -1.0

        linear 1.0 xalign 1.6
        linear 1.0 xalign 0.85

    bm "Wroom."

    show protagonist mask angry
    mc "What the hell is this?!?!"
    mc "You! Don't you dare send me to another world!"

    show truck at center:
        xalign 0.85
        xzoom -1.0

        linear 1.0 xalign 0.85
        linear 1.0 xalign 0.5
    bm "Nyoom."

    show protagonist mask angry
    mc "I finally have a chance to get a girl and touch some oppai, you're not ruining this for me!"

    ar "Are both contestants readyyyy?"

    menu:
        "Start boss fight":
            show protagonist mask angry at left
            mc "Yes"

            show truck at right
            bm "Wroom!"

            "Announcer: In that case, it is time! To! FIGHT!!!"

            menu:
                "Punch car":
                    call combat("images/truck.png", 100, 15) from _call_combat_3
                    scene bg black
                    pass
           
        "Flee":
            "Protagonist-kun flees the tavern like a coward."
            "They become the laughing stock of the town, and are never taken seriously again."
            return

    jump a3e3