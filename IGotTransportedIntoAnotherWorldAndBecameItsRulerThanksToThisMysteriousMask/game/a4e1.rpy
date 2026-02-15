label a4e1:
    scene bg bar
    "As the group gathers at the tavern to celebrate Protagonist-kun’s new status as Town Mayor, the sun is slowly setting."

    "And with all the world’s evils defeated, our beloved Protagonist-kun decides to finally take their new companions on a date to a nearby beach."

    show protagonist mask at center
    mc "I should really be spending some time with my girls."

    show protagonist mask happy at center
    mc "The temperatures are nice and warm, and there’s practically no wind, so it’s a perfect beach day!"

    show protagonist mask happy at center
    mc "I just need to invite all my girlies with me."

    "Who do you want to go to the beach with?"

    jump dateSelection

        
label dateSelection:
menu:
    "Susan":
        call susanDate

    "Ayla":
        call aylaDate

    "Evelyn":
        call evelynDate

    "Tessa":
        call tessaDate

    "Truck-kun":
        call truck_kunDate

    "All of them":
        wr "{size=+150}HAHAHAHAHAHAHA{size=-150}"
        wr "No."
        jump dateSelection

scene bg black

"As the moon begins its climb across the sky, bringing stars with it, the day finally draws to a close. 
And so, Protagonist-kun lived happily ever after with all his new hot waifus and one husbando."

menu:
    "The end":
        pass

return