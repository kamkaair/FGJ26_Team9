label a2e1:
    image bg black = "#000000"
    image text = Transform(Text("The next day:", size=60), yalign=0.5)

    show bg black
    show text
    "Click to continue..."

    scene bg cool # PLACEHOLDER
    with dissolve

    #show MainCharacter empty_hat at center
    show MainCharacter empty_hat at center:
        zoom 1.2
        xalign 0.5
        yalign 3.2

    show susan at center:
        xalign 0.9
        yalign 1.0

    show logo base at center:
        xalign 0.1
        yalign 1.0

    "Our beloved [mc_color] wakes up around mid-day, feeling refreshed."

    mc "Ahh. That was some of the best sleep I've ever had. I wonder how the girls are doing..."

    "[mc_color] makes their way to the main area of the tavern, where [pg_color] and [sg_color] are enjoying lunch."

    sg "...and then they punched me! And I got turned into a girl!"
    "[sg_color] exclaims."

    pg "So that's how they cured you from that awful curse. It's great that you ran into a great hero, such as the Masked One..."
    "[pg_color] replies."

    sg "{size=-7}Ah, no. I-I was {i}never{/i} cursed...{/size}"
    "[sg_color] mumbles."

    mc "Goood morning girls!"
    "[mc_color] greets them."

    pg "Ara ara. You finally woke up! I was worried that someone had assassinated you in your sleep or something..."

    mc "Assassinated..?"
    "[mc_color] asks, worried."

    pg "In any case, there were some reports of a monster made of blinding light wreaking havoc in a nearby forest. Sounds like a job for you,"
    "[pg_color] tells them."

    "[mc_color]'s stomach rumbles loudly."
    
    mc "I'll go after I've eaten breakfast..?"
    "{color=#dda732}They ask.{/color}" # This is kinda dumb way of getting the character's color, but it shall be fine for now.

    pg "Nonsense! You must go straight away. Otherwise the monster might kill someone!"

    mc "{i}But I'm hungry...{/i}"

    pg "{size=+15}NOW!{/size}"
    "[pg_color] yells."

    "Protagonist-kun escapes from the tavern, and runs straight out of the town."

    #jump a2e2
    