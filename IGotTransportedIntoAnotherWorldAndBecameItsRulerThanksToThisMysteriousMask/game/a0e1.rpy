image truckLogo = "images/truckLogo.png" # Load images like this, used inside the scene 1
#define flashbulp = Fade(0.2, 0.0, 0.8, color='#fff')
label a0e1:
    scene bg cool
    with dissolve

    show characterLayer round_Hat at right

    "It was a regular Wednesday evening. Our Protagonist-kun was returning home from college."

    e "Sigh... Another long day of studying. And no matter how hard I try, I just can't get a girlfriend :( It's almost like I'm so generic that all the girls forget I exist..."

    "They kept walking on, dejected, lamenting about life."

    e "I know I'm not the smartest... Or the strongest... Or anything special really, but I'm perfectly average at everything! It shouldn't be this hard to get a girl! Girls love average! Right? At this rate I'm going to grow old without ever touching a single oppai."

    "Unfortunately, they failed to look before crossing the road..."

    # TODO: animation / still image of truck-kun demolishing the main character
    scene bg forest
    with fade # or some other transition...

    show truckLogo at right
    "Truck"
    #"Great choice, [povname]."

    return  
    