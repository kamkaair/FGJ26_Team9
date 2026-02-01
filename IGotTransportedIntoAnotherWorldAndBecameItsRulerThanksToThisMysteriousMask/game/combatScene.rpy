init python:

    import math, random

    # Default player stats
    playerHP = 100
    playerAttack = 20
    isPlayerDefending = False
    playerAreaOfAttack = 3

    # Default enemy stats
    enemyHP = 100
    enemyAttack = 15
    isEnemyDefending = False
    enemyAreaOfAttack = 3

    # Whose turn?
    currentTurn = "player"

    # Deals the damage of an attack
    def attack(damage, hp, defending, victimAOA, attackerAOA):
        newDamage = math.floor(damage)

        hitResult = abs(victimAOA - attackerAOA)
        if defending:
            if hitResult == 0:
                #perfect guard
                newDamage += 8
                print("Perfect Guard")
            elif hitResult == 1:
                #imperfect guard
                newDamage //= 2
                print("Imperfect Guard")
            else:
                #bad guard
                newDamage //= 1.2
                print("Bad Guard")

        print(newDamage)

        hp -= newDamage
        hp = max(hp, 0)

        return hp

    # Initializes the combat
    def reset_combat(inEnemyHP, inEnemyDamage):
        global playerHP, enemyHP, enemyAttack
        global isPlayerDefending, isEnemyDefending
        global currentTurn

        playerHP = 100
        enemyHP = inEnemyHP
        enemyAttack = inEnemyDamage
        isPlayerDefending = False
        isEnemyDefending = False

        currentTurn = "player"

    def player_attack_enemy(height):
        global enemyHP, currentTurn, enemyHP, playerAreaOfAttack
        playerAreaOfAttack = height
        damage = playerAttack * random.uniform(0.75, 1)
        enemyHP = attack(damage, enemyHP, isEnemyDefending, playerAreaOfAttack, enemyAreaOfAttack)

        currentTurn = "enemy"

    def player_defend(height):
        global isPlayerDefending, currentTurn, playerAreaOfAttack
        isPlayerDefending = True
        playerAreaOfAttack = height

        currentTurn = "enemy"
                

    def enemy_turn():
        global playerHP, isPlayerDefending, isEnemyDefending, currentTurn, enemyAreaOfAttack

        isEnemyDefending = False
        enemyAreaOfAttack = math.floor(random.uniform(1,3))

        # Simple AI: random choice
        if random.choice(["attack", "defend"]) == "attack":
            damage = enemyAttack * random.uniform(0.5, 1)
            print("enemy attack")
            playerHP = attack(damage, playerHP, isPlayerDefending, enemyAreaOfAttack, playerAreaOfAttack)

        else:
            print("enemy defending")
            isEnemyDefending = True

        isPlayerDefending = False
        currentTurn = "player"

screen combat_ui():

    frame:
        xalign 0.5
        yalign 0.75
        padding (80, 80)

        vbox:
            spacing 40

            text "Player HP: [playerHP]"
            text "Enemy HP: [enemyHP]"

            if currentTurn == "player":
                text "Your Turn"

                hbox:
                    spacing 40

                    #textbutton "Attack" action Function(player_attack_enemy)
                    #textbutton "Defend" action Function(player_defend)

                    textbutton "Attack" action Show("combat_attackCheck")
                    textbutton "Defend" action Show("combat_defenseCheck")

                    if(currentTurn == "enemy"):
                        text "Enemy Turn..."

screen combat_defenseCheck():

    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)

        vbox:
            spacing 20

            text "Which part do you want to GUARD?"

            textbutton "Guard High" action [Function(player_defend, 3), Hide("combat_defenseCheck")]
            textbutton "Guard Mid" action [Function(player_defend, 2), Hide("combat_defenseCheck")]
            textbutton "Guard Low" action [Function(player_defend, 1), Hide("combat_defenseCheck")]

screen combat_attackCheck():

    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)

        vbox:
            spacing 20

            text "Where part do you want to target?"

            textbutton "High" action [Function(player_attack_enemy, 3), Hide("combat_attackCheck")]
            textbutton "Mid" action [Function(player_attack_enemy, 2), Hide("combat_attackCheck")]
            textbutton "Low" action [Function(player_attack_enemy, 1), Hide("combat_attackCheck")]
                

label combat(enemySprite, inEnemyHP, inEnemyDamage):
    define eCombat = Character(None, window_background = None,
    what_size=28, what_outline=[(1, "#008000", 0,0)],
    what_xalign=0.5, what_textalign=0.5, what_layout='subtitle')

    scene bg forest
    with vpunch

    image enemySprite = "[enemySprite]"
    show MainCharacter at left
    show enemySprite at right

    $ reset_combat(inEnemyHP, inEnemyDamage)
    show screen combat_ui
    
    while playerHP > 0 and enemyHP > 0:

        if currentTurn == "enemy":
            hide screen combat_ui
            $ enemy_turn()
            $ renpy.pause(2.0)

        else:
            #call defenseCheck(playerAreaOfAttack)
            show screen combat_ui
            $ renpy.pause(2.0)

    hide screen combat_ui
    hide MainCharacter at left
    hide enemySprite at right

    if playerHP <= 0:
        "You were defeated."
        "Do you want to try again?"
        menu:
            "yes":
                call combat(enemySprite, inEnemyHP, inEnemyDamage)
            "no":
                $ MainMenu(confirm=False)() # Should force back to main menu
    else:
        "You won the battle!"

    return

label defenseCheck(AOA):
    menu:
        "Which spot do you want to either ATTACK or DEFEND?"
        "High":
            $ AOA = 3
        "Middle":
            $ AOA = 2
        "Low":
            $ AOA = 1

    return