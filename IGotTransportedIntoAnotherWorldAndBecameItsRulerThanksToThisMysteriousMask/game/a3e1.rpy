label a3e1:
    show textForest
    "Click to continue..."

    scene bg forest
    with dissolve

    "One day while training, [mc_color] hears a dangerous growl from the nearby bushes."

    show protagonist mask surprised at center:
        xalign 0.25
    mc "Huh? What's that?"

    "The growling comes closer. And closer, and closer, until!"

    "They get pounced."

    show protagonist mask surprised
    mc "Ow! Shit, it's a tiger!"

    show tiger at center:
        xalign 1.0
        yalign 1.5

    cg "Rawr."

    show protagonist mask neutral
    mc "Oh, why am I worried?"

    mc "I've been training to fight the strongest opponents this world has to offer. One measly tiger shouldn't be too hard to beat!"

    menu:
        "Punch tiger":
            call combat("images/tiger.png", 1, 15)
    
    "As [mc_color] lands one final punch on the tiger, it transforms into a beautiful tiger-girl."

    show protagonist mask angry
    mc "Huff, puff... That was a lot tougher than I expected."

    show tessa angry
    cg "Ow... What the hell? Why did you punch me?!"

    show protagonist mask angry
    mc "You tried to attack me! What else was I supposed to do?!"

    show tessa angry
    cg "Well, maybe you shouldn't have been training so hard!"

    cg "You would've noticed me staring at you!"

    "She punches [mc_color]."

    show protagonist mask sad
    mc "Ow... Ok, yeah, getting punched definitely hurts..."

    show protagonist mask neutral
    mc "I'd say I'm sorry but it cured your curse so..."

    show tessa angry
    cg "So it's ok to punch women?!"

    show protagonist mask surprised
    mc "Well, when you put it that way, I guess I should learn to use my powers some other way."

    show protagonist mask neutral
    mc "{size=-10} Psst... Hey mask, is there any chance your powers might work without the punching? {/size}"

    "No."

    show protagonist mask neutral
    mc "Why?!"

    "Because my power turns whatever you punch into whatever your heart most desires."

    show tessa angry
    cg "Who're you talking to?! And why am I not included??"

    show protagonist mask surprised
    mc "Ahh... Uhm... That's... Well-"

    show tessa angry
    cg "Whatever. It's not like I care about you or anything."

    show protagonist mask neutral
    mc "Right..."

    mc "Anyway, I really should head back to the town. Are you coming with me or..?"

    show tessa neutral
    cg "Yes!"

    "They begin to walk towards town."

    show protagonist mask neutral
    mc "Right... Anyway, I'm [mc_color]. What's your name?"

    show tessa neutral
    cg "I'm [cg_color]."

    show protagonist mask neutral
    mc "Nyan-chan. Got it."

    show tessa angry
    cg "Do I look like a regular house-cat, you baka?!?!"

    "The two of them kept arguing all the way back into town..."



    #show bg whiteFlash
    #with vpunch

    #show valo at center: # Valo appears
        #xalign 1.25
        #yalign 1.0
        #zoom 0.75
        #linear 1.0 xalign 1.25
        #linear 1.0 xalign 0.75
    

    #mc "...{color=#fdef2b}Eve-tan{/color}."
    #lg "{size=+5}...-tan..?{/size}"
    #lg "“...I guess you're right. {color=#fdef2b}Eve-tan{/color} {i}is{/i} a cute nickname..."

   
    #jump a2e4
    