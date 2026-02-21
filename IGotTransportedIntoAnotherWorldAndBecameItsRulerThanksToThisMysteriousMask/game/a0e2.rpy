init:
    $ flash = Fade(.25, 0, .75, color="#fff")

label a0e2:
    scene bg fantasy
    with flash
    play music woods_theme
    show protagonist at left

    mc "Groan..."
    "[mc_color] opens their eyes. They seem to have been transported into a fantasy world."

    mc "Ow ow ow..." 
    mc "What the hell was that?" 

    show protagonist at center

    "While dusting off their pants, [mc_color] notices something on the ground"

    mc "What's that? A mask?"
    "They pick it up."

    mk "Put me on..."

    show protagonist surprised at center

    mc "Huh? Where did that voice come from?"

    mk "Put me on..."

    mc "Is it the mask?"

    "Protagonist-kun listens for a moment. They can only hear the sounds of birds chirping in the distance."

    mc "Still, this mask is weird..."

    menu: 
        "Put the mask on":
            show protagonist neutral at center
            mc "I wonder what it would look like on my face…"
        "Leave the mask on the ground":
            "The mask compels [mc_color]..."
            "They can’t resist it."

    stop music fadeout 1.0
    #[insert sparkle sound effect here]
    #Maybe some other effect
    

    scene bg fantasy # PLACEHOLDER
    with dissolve

    "As [mc_color] puts the mask on their generic face, they feel a sudden rush of power surging through their body!" 

    mk "Thank you for picking me up."
    mk "I have been stuck on the side of this road for far too long..."

    show protagonist mask surprised at center

    play music woods_theme
    mc "Wait... Is the mask talking to me??"

    mk "Yes, I'm talking to you!"
    mk "And now, as a show of my gratitude for saving me from my predicament, I’m giving you my powers!"

    mk "Use them well…"



    mc "Your… powers?"

    "The mask stays silent."

    mc "What powers?!"

    "No matter how much they prod, the mask stays silent."

    show protagonist mask angry at center

    mc "Fine then! See if I care!"

    mc"I’m leaving you here, you stupid mask!"

    menu:
        "Pull at mask":
            pass
        "Push at mask":
            pass
    play sound hit5_sfx
    "Unfortunately for our Protagonist-kun…"
    "They can’t get the mask off."

    mc "What the hell?!?! Did this thing get super glued to my face???"

    "No matter how much they struggle, the mask isn’t budging."

    show protagonist mask at center

    mc "Okay. So… I got hit by a truck, I don’t know where I am, and I have a sometimes-talking-but-usually-not mask stuck to my face now?"

    show protagonist mask angry at center

    mc "What is this, a bad anime plot?"

    "Protagonist-kun looks around. They see a sign."

    menu:
        "Read sign":
            "Sign: Generic Fantasy Town, 3km ->"
            show protagonist mask angry at center
            mc "Ugh, I do not want to walk that long in this heat!"

            "Unfortunately, they don’t have a choice"
        "Start walking":
            pass

    jump a1e1
    