# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image bgZomer = im.Scale("bgZomer.png", 1920,1080)
image bgWinter = im.Scale("bgWinter.png", 1920,1080)
image bgLente = im.Scale("bgLente.png", 1920,1080)
image bgHerfst = im.Scale("bgHerfst.png", 1920,1080)
image bgWerkHuisAuto = im.Scale("bgWerkHuisAuto.png",1920,1080)
image huis1 = "Huis1.png"
image huis2 = "Huis2.png"
image huis3 = "Huis3.png"
image huis4 = "Huis4.png"
image huis5 = "Huis5.png"

image auto1 = "auto1.png"
image auto2 = "auto2.png"
image auto3 = "auto3.png"
image auto4 = "auto4.png"
image auto5 = "auto5.png"
image auto6 = "auto6.png"

image aDokter = "Dokter.png"

define e = Character("JC3")

default geld = 0
default leeftijd = 8
default maandIndicatie = 0

default maand = "januari"

default job = "werkloos"

default currentMaand = ''

default maanden = ["januari","maart", "mei", "juli", "september", "november"]

default ziek = False





# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bgWinter

    # show redButton
    show screen geld
    show screen job
    show screen plusButton
    show screen leeftijd
    show screen maand
    show screen werk
    # show screen winkel
    show screen docter
    show screen huizen
    show screen autos

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    # e "saus"

    show text "{color=#000}Hallo!{/color}" at topleft
    with dissolve
    pause 1000
    # hide text
    # with dissolve


    # This ends the game.

    return


label plus:
    $ maandIndicatie +=1
    $ if maandIndicatie > 5: maandIndicatie = 0
    $ if maandIndicatie == 0: leeftijd +=1

    if maandIndicatie == 0 or maandIndicatie == 5:
        scene bgWinter
    elif maandIndicatie == 1 or maandIndicatie == 2:
        scene bgLente
    elif maandIndicatie == 3:
        scene bgZomer
    else:
        scene bgHerfst


    hide text
    with dissolve
    pause 0.5
    show text "{color=#000}2 Maanden verder ...{/color}" at topleft
    with dissolve
    
    
    
    show screen geld
    show screen job
    show screen plusButton
    show screen leeftijd
    show screen maand
    show screen werk
    # show screen winkel
    show screen docter
    show screen huizen
    show screen autos

    pause 10000

    return

label Jobs:
    scene bgWerkHuisAuto

    hide screen job
    hide screen plusButton
    hide screen leeftijd
    hide screen maand
    hide screen werk
    hide screen winkel
    hide screen docter
    hide screen huizen
    hide screen autos

    show screen home

    show text "{color=#000}Werk pagina{/color}" at top
    with dissolve
    pause 10000

    return

label dokter:
    scene bgWerkHuisAuto

    hide screen job
    hide screen plusButton
    hide screen leeftijd
    hide screen maand
    hide screen werk
    hide screen docter
    hide screen winkel
    hide screen huizen
    hide screen autos

    show screen home

    show text "{color=#000}Docter pagina{/color}" at top

    show aDokter:
        xpos 300
        ypos 100
    
    show text "{color=#000}Momenteel ben je niet ziek.{/color}" at truecenter

    if ziek:
        show text "{color=#000}€25 voor dokters bezoek{/color}":
            xpos 800
            ypos 700

    with dissolve
    pause 10000

    return


label huis:
    scene bgWerkHuisAuto

    hide screen job
    hide screen plusButton
    hide screen leeftijd
    hide screen maand
    hide screen werk
    hide screen docter
    hide screen winkel
    hide screen huizen
    hide screen autos

    show screen home

    show text "{color=#000}Huizen pagina{/color}" at top
    show huis1:
        xpos 100
        ypos 50
    show huis2:
        xpos 100
        ypos 300
    show huis3:
        xpos 100
        ypos 550
    show huis4:
        xpos 1000
        ypos 50
    show huis5:
        xpos 1000
        ypos 300
    with dissolve
    pause 10000

    return

label auto:
    scene bgWerkHuisAuto

    hide screen job
    hide screen plusButton
    hide screen leeftijd
    hide screen maand
    hide screen werk
    hide screen docter
    hide screen winkel
    hide screen huizen
    hide screen autos

    show screen home

    show text "{color=#000}auto pagina{/color}" at top

    show auto1:
        xpos 100
        ypos 50
    show auto2:
        xpos 100
        ypos 300
    show auto3:
        xpos 100
        ypos 550
    show auto4:
        xpos 1000
        ypos 50
    show auto5:
        xpos 1000
        ypos 300
    show auto6:
        xpos 1000
        ypos 550

    with dissolve
    pause 10000

    return
    


screen geld:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.999999999
        yalign 0
        text "Geld: € [geld]" yalign 0.5 xalign 0.5

screen job:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.999999999
        yalign 0.07
        text "Job: [job]" yalign 0.5 xalign 0.5

screen leeftijd:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.999999999
        yalign 0.147
        text "leeftijd: [leeftijd]" yalign 0.5 xalign 0.5

screen maand:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.999999999
        yalign 0.22
        default currentMaand = maanden[maandIndicatie]
        text "Maand: [currentMaand]" yalign 0.5 xalign 0.5


screen plusButton:
    imagebutton:
        xpos 0.47
        ypos 0.8
        idle "plusKnop.png"
        action Jump("plus")

screen werk:
    imagebutton:
        xpos 0.27
        ypos 0.8
        idle "knopWerk.png"
        action [ToggleScreen("werk"), Jump("Jobs")]

screen docter:
    imagebutton:
        xpos 0.07
        ypos 0.8
        idle "knopDokter.png"
        action [ToggleScreen("docter"), Jump("dokter")]
    
screen huizen:
    imagebutton:
        xpos 0.67
        ypos 0.8
        idle "knopHuis.png"
        action [ToggleScreen("huizen"), Jump("huis")]

screen autos:
    imagebutton:
        xpos 0.87
        ypos 0.8
        idle "knopAuto.png"
        action [ToggleScreen("autos"), Jump("auto")]


screen home:
    imagebutton:
        xpos 0.47
        ypos 0.8
        idle "knopHome.png"
        action [ToggleScreen("home"), Jump("start")]

