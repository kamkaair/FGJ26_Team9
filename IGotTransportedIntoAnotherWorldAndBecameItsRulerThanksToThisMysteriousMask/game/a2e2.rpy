label a2e2:
    image bg black = "#000000"
    image textForest = Transform(Text("At the forest:", size=60), yalign=0.5)

    show bg black
    show textForest
    "Click to continue..."

    scene bg forest # PLACEHOLDER
    with dissolve

    #show MainCharacter empty_hat at center
    show protagonist mask at center:
        zoom 1.2
        xalign 0.5
        yalign 3.2

    show susan at center:
        xalign 0.9
        yalign 1.0

    show ayla neutral at center:
        xalign 0.1
        yalign 1.0

    mc "[pg_color] is so scary when she gets mad... I just wanted some breakfast before continuing on my quest to gain a harem..."
    "Their stomach rumbles loudly."

    mc "Well, nothing I can do about that now. I guess if I find the monster fast I'll be able to get back to town fast and then I'll be able to eat"

    "And so, our [mc_color] begins his search. They search high and low, behind bushes and under rocks. 
    They keep searching, as the sun makes its way higher and higher on the sky, eventually starting its slow descent towards dusk"
    
    mc "Where the hell is that stupid monster?!?!"
    "[mc_color] yells." 

    mc "I have been searching for it for hours! And it still hasn't shown up?!"

    "They hear no response to their yelling. Even the birds seem to have gone silent."

    mc "Whatever. I'm going back to town. [pg_color] can go find the monster herself if she gets mad."

    "Suddenly, a blinding light, capable of rivaling the sun, seemed to appear. It twinkled as it moved closer, radiating heat."
    #effects

    mc "How the hell do you defeat a light?" 
    "[mc_color] exclaimed."

    mk "Have you considered punching it?"
    "[mk_color]'s voice asks."

    mc "How do you punch a light?!?!"
    "[mc_color] yells as the light moves closer."

    mk "You punch by first pulling your fist back-"
    "[mk_color] begins to explain"

    mc "You know what, that's not helpful."
    "[mc_color] replies"

    "As the light moves right next to Protagonist-kun, they punch it."

    call combat("images/valo.png", 100, 15)

    mc "Huh… Turns out you can punch a light."
    "A tiny fairy stands up, her wings glowing with the same light that had formed the monster mere moments ago."

    show evelyn surprised at right:
        zoom 1.3

    lg "Ugh… That was the most unpleasant experience of my life!" 
    "she exclaims." 
    lg "Thank you so so SO much for saving me! I'm [lg_color], a master musician in my clan. If there's anything I can do to repay you, please let me know!"

    mc "Oh wow. It's nice to meet you…"
    "Protagonist-kun starts,"
    mc "...{color=#fdef2b}Eve-tan{/color}."

    lg "{size=+5}...-tan..?{/size}"
    "[lg_color] asks, shocked" 
    lg "{size=+5}TAN?!?!{/size} What do you think I am, a baby?!"

    mc "Err- Well, you are small and adorable so I thought..."
    "Protagonist-kun starts explaining."

    lg "...I guess you're right… And {color=#fdef2b}Eve-tan{/color} is a cute nickname, I suppose..."

    "The two of them stand in silence while Evelyn ponders about her new nickname."

    lg "Yeah, it's fine. I've never had a nickname before. Does this finally make me a proper idol?"
    "Evelyn asks."

    mc "It absolutely does!"
    "Protagonist-kun agrees."

    mc "Now, as much as I'd love to keep chatting with you in this lovely forest full of dangerous beasts, 
    I haven't eaten anything yet and I'm {size=+5}{i}starving{/i}{/size}. What do you think, should we head to the nearby town and grab something to eat?"

    "There's a low growl coming from somewhere close by."

    lg "Eep-!"
    "Evelyn shouts, frightened."
    lg "Yes yes, let's leave this forest!"

    "And so, the two of them make their way back into town."

    "{color=#dda732}They ask.{/color}" # This is kinda dumb way of getting the character's color, but it shall be fine for now.
    mc "{i}But I'm hungry...{/i}"
    pg "{size=+15}NOW!{/size}"
    "[pg_color] yells."


    #jump a2e2
    