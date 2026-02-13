label a2e2:
    image bg black = "#000000"
    image bg whiteFlash = "#ffffff"
    image textForest = Transform(Text("At the forest:", size=60), yalign=0.5)

    scene bg black
    show textForest
    "Click to continue..."

    scene bg forest # PLACEHOLDER
    with dissolve

    show protagonist mask sad at center
    mc "[pg_color] is so scary when she gets mad... "
    mc "I just wanted some breakfast before continuing on my quest to gain a harem..."
    "[mc_color]'s stomach rumbles loudly."

    show protagonist mask at center
    mc "Well, nothing I can do about that now."
    mc "I guess if I find the monster fast I'll be able to get back to town fast and then I'll be able to eat"

    "They keep searching, as the sun makes its way higher and higher on the sky, eventually starting its slow descent towards dusk."
    
    show protagonist mask angry at center
    mc "Where the hell is that stupid monster?!?!"
    mc "I have been searching for it for hours!"
    mc "And it still hasn't shown up?!"

    "They hear no response to their yelling. Even the birds seem to have gone silent."

    menu:
        "Go back to town":
            pass

    show protagonist mask at center
    mc "Whatever. I'm going back to town."
    mc "[pg_color] can go find the monster herself if she gets mad."

    "Suddenly, a flashing light, capable of momentarily rivaling the sun, seems to appear."
    
    show bg whiteFlash
    with vpunch

    show protagonist mask sad at center:
        zoom 1.0
        linear 1.0 xalign 0.5
        linear 1.0 xalign 0.0

    show valo at center: # Valo appears
        xalign 1.25
        yalign 1.0
        zoom 0.75
        linear 1.0 xalign 1.25
        linear 1.0 xalign 0.75
    "It sparks as it moves closer."

    show protagonist mask surprised
    mc "How the hell do you defeat a spider made of lightning?!?!" 

    mk "Have you considered punching it?"

    show valo at center: # Valo moves closer
        zoom 0.75
        linear 1.0 xalign 0.75
        linear 1.0 xalign 0.5

    show protagonist mask angry
    mc "How do you punch lightning?!?!"

    mk "You punch by first pulling your fist back-"

    mc "You know what, that's not helpful."

    show valo at center: # Valo is right next to the mc
        zoom 0.75
        linear 1.0 xalign 0.5
        linear 1.0 xalign 0.25
    
    pause 1.0 # Wait for the animation

    menu:
        "Punch it!":
            call combat("images/valo.png", 100, 15) from _call_combat

    mc "Huh… Turns out you can punch a light."
    "A tiny fairy stands up, her wings glowing the same purple light that had formed the spider mere moments ago."

    show evelyn angry at right:
        xalign 1.1
        yalign 1.0
        zoom 1.3

    lg "Ugh… That was the most unpleasant experience of my life!" 

    show evelyn happy
    lg "Thank you so so SO much for saving me!"
    show evelyn neutral
    lg "I'm [lg_color], a master idol known all through these lands." 
    $ lg = Character(name=CharactersInfo[4][0], who_color=CharactersInfo[4][2])
    lg "If there's anything I can do to repay you, please let me know!"

    show protagonist mask happy
    mc "Oh wow. It's nice to meet you…"
    menu:
        "Give Evelyn a nickname":
            pass

    mc "...{color=#fdef2b}Eve-tan{/color}."

    show evelyn surprised
    lg "{size=+5}...-tan..?{/size}"

    show evelyn angry
    lg "{size=+5}TAN?!?!{/size} What do you think I am, a baby?!"

    show protagonist mask surprised
    mc "Err- Well, you are small and adorable, so I thought…"

    show evelyn neutral
    lg "“...I guess you're right. {color=#fdef2b}Eve-tan{/color} {i}is{/i} a cute nickname..."

    "The two of them stand in silence while Evelyn ponders about her new nickname."

    show evelyn neutral
    lg "Yeah. It's fine! I've never had a nickname before so it just felt weird."

    show evelyn neutral
    lg "Does this finally make me a proper idol?"

    show protagonist mask happy
    mc "It absolutely does!"

    show protagonist mask
    mc "Now, as much as I'd love to keep chatting with you in this lovely forest full of dangerous beasts, I haven't eaten anything yet and I'm starving."
    mc "What do you think, should we head to a nearby town and grab something to eat?"

    "There's a low growl coming from somewhere close by."

    show evelyn surprised
    lg "Eep!"
    lg "Yes yes, let’s leave this forest, right now!"

    "And so, the two of them make their way back into town."

    jump a2e3
    