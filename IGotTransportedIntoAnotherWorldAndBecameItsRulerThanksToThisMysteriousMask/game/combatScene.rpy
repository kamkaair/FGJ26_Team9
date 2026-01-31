init python:

    import math, random

    # Player stats
    playerHP = 100
    playerAttack = 20
    isPlayerDefending = False

    # Enemy stats
    enemyHP = 100
    enemyAttack = 15
    isEnemyDefending = False

    # Whose turn?
    currentTurn = "player"

    def attack(damage, hp, defending):
        newDamage = math.floor(damage)
        if defending:
            newDamage //= 2

        hp -= newDamage
        hp = max(hp, 0)

        return hp

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

    def player_attack_enemy():
        global enemyHP, currentTurn, enemyHP

        damage = playerAttack * random.uniform(0.75, 1)
        enemyHP = attack(damage, enemyHP, isEnemyDefending)

        currentTurn = "enemy"

    def player_defend():
        global isPlayerDefending, currentTurn
        isPlayerDefending = True
        currentTurn = "enemy"

    def enemy_turn():
        global playerHP, isPlayerDefending, isEnemyDefending, currentTurn

        isEnemyDefending = False

        # Simple AI: random choice
        if random.choice(["attack", "defend"]) == "attack":
            damage = enemyAttack * random.uniform(0.75, 1)
            print("enemy attack")
            playerHP = attack(damage, playerHP, isPlayerDefending)

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

                    textbutton "Attack" action Function(player_attack_enemy)
                    textbutton "Defend" action Function(player_defend)

                    if(currentTurn == "enemy"):
                        text "Enemy Turn..."

label combat(enemySprite, inEnemyHP, inEnemyDamage):
    define eCombat = Character(None, window_background = None,
    what_size=28, what_outline=[(1, "#008000", 0,0)],
    what_xalign=0.5, what_textalign=0.5, what_layout='subtitle')

    image enemySprite = "[enemySprite]"
    show MainCharacter at left
    show enemySprite at right

    $ reset_combat(inEnemyHP, inEnemyDamage)
    show screen combat_ui
    
    while playerHP > 0 and enemyHP > 0:

        if currentTurn == "enemy":
            ##hide screen combat_ui
            $ enemy_turn()
            $ renpy.pause(2.0)

        else:
            ##show screen combat_ui
            $ renpy.pause(0.1)

    hide screen combat_ui
    hide MainCharacter at left
    hide enemySprite at right

    if playerHP <= 0:
        "You were defeated."
    else:
        "You won the battle!"

    return