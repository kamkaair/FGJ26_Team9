label a1e2:
    image bg black = "#0b681f"
    image text = "{color=#83ca1f} At the tavern..{/color}"#Transform(Text("{color=#83ca1f} At the tavern..{/color}", size=60), yalign=0.5)

    show bg black
    show text
    "Click to continue..."
    
    show protagonist happy at left
    mc "Haah… I’m so glad this place has a tavern."
    show protagonist at left
    "What about you, [sg_color]?"
    
    "The slime-girl drinks the last of her beer, feeling herself fill up with courage."
    
    sg "A-actually, my name is Susan…"
    $ sg = Character(name=CharactersInfo[2][0], who_color=CharactersInfo[2][2])

    "Protagonist-kun ignores this completely."

    show protagonist happy at left
    mc "Yeah yeah. So! What should we do next?"
    mc "I was thinking of a romantic date on a nearby beach..."

    "[mc_color] wiggles their eyebrows."

    show susan happy at right
    sg "I l-like the water..."

    mc "What's the spirit!"

    mc "So, what do you say?"

    mc "We could enjoy a not-so-long-because-I\m-out-of-shape"
    mc "walk along the coastline before going on a romantic swim in the bay at sunset!"

    show susa susan at right
    sg "Uhm? Well.. It does sound fun.."

    mc "I know right?"

    mc "So, [sg_color], shall we go on the first date of my life, culminating in-?"

    "They get interrupted by a random person bursting into the tavern."

    $ r Character("Random Civilian")
    r "{size=+10}{b}Someone help! A plant monster has walked straight into town!{/b}{/size}"

    "There's people screaming outside."

    "Suddenly, the plant monster bursts into the tavern."

Protagonist-kun (surprised): “Whoa! What’s this? Someone dares intrude on my epic date plans?”

Protagonist-kun (surprised): “Slime-chan! get somewhere safe!”

[Move Susan’s sprite off-screen]

Plant monster: “Shuffle shuffle.”

Protagonist-kun (angry): “Oh wow, you seem way stronger than Slime-chan did…”

Mask: “You know, if you punch it my powers will turn it into a “hot waifu” as you seem to refer to them.”

Protagonist-kun (neutral): “Oh right, I totally forgot that.”

Protagonist-kun (angry): “Welp, here we go!”

[Player choice: “Punch the plant”]

[Insert fighting minigame here]

Narrator: As Protagonist-kun punches the lights out of the plant monster, it transforms into a hot elf waifu!

Elf (neutral): “Huh… What was I doing..?”

Narrator: The tall elf gets up, before setting her sights on Protagonist-kun.

Elf (neutral): “I must thank you for freeing me of that awful curse.”

Elf (neutral): “It was most unpleasant.”

[Player choice: “Ask about curse”]

Protagonist-kun (surprised): “Huh? What curse?”

Elf (neutral): “Oh? You don’t know?”

Elf (neutral): “The curse that’s turned half this world into hideous monsters, of course.”

Elf (neutral): “I must ask, how did you manage to unto the curse, Masked Warrior?”

Protagonist-kun (suprised) [whispering]: “Err… Hey mask, could I get a little help here?”

Narrator: The mask is once again silent.

Protagonist-kun (neutral) [whispering]: “Well then… Time to improvise.”

Protagonist-kun (happy): “Ahem. I’m a great mage from a faraway land, and I’ve come here to save all innocents because I’m such a good person.”

Protagonist-kun (happy) [whispering]: “And I definitely deserve to get a girlfriend for all my troubles.”

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
