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
image huis6 = "huis6.png"

image huis1Gekocht = "Huis1Gekocht.png"
image huis2Gekocht = "Huis2Gekocht.png"
image huis3Gekocht = "Huis3Gekocht.png"
image huis4Gekocht = "Huis4Gekocht.png"
image huis5Gekocht = "Huis5Gekocht.png"
image huis6Gekocht = "huis6Gekocht.png"

default huisId = 0

image auto1 = "auto1.png"
image auto2 = "auto2.png"
image auto3 = "auto3.png"
image auto4 = "auto4.png"
image auto5 = "auto5.png"
image auto6 = "auto6.png"

default autoId = 0

image kapper = "kapperLogo.png"
image leerkrachtLogo = "leerkrachtLogo.png"
image politieLogo = "politieLogo.png"
image brandweerLogo = "brandweerLogo.png"
image dokterLogo = "dokterLogo.png"
image dierenverzorgLogo = "dierenverzorgerLogo.png"

image aDokter = "Dokter.png"

define e = Character("JC3")

default geld = 0
default leeftijd = 17
default maandIndicatie = 0

default maand = "januari"

default job = "werkloos"
default salaris = 0

default currentMaand = ''

default maanden = ["januari","maart", "mei", "juli", "september", "november"]

default ziek = False





# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    if maandIndicatie == 0 or maandIndicatie == 5:
        scene bgWinter
    elif maandIndicatie == 1 or maandIndicatie == 2:
        scene bgLente
    elif maandIndicatie == 3:
        scene bgZomer
    else:
        scene bgHerfst
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

    hide screen textHuis1
    hide screen textHuis2
    hide screen textHuis3
    hide screen textHuis4
    hide screen textHuis5
    hide screen textHuis6

    hide screen prijsHuis1
    hide screen prijsHuis2
    hide screen prijsHuis3
    hide screen prijsHuis4
    hide screen prijsHuis5
    hide screen prijsHuis6

    hide screen textauto1
    hide screen textauto2
    hide screen textauto3
    hide screen textauto4
    hide screen textauto5
    hide screen textauto6

    hide screen prijsauto1
    hide screen prijsauto2
    hide screen prijsauto3
    hide screen prijsauto4
    hide screen prijsauto5
    hide screen prijsauto6

    hide screen textjob1
    hide screen textjob2
    hide screen textjob3
    hide screen textjob4
    hide screen textjob5
    hide screen textjob6

    hide screen salarispolitie
    hide screen salarisbrandweer
    hide screen salarisleerkracht
    hide screen salarisdierenverzorg
    hide screen salarisdoker
    hide screen salariskapper

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    # e "saus"

    show text "{color=#000}Hallo!{/color}" at topleft
    with dissolve

    if huisId == 1:
        show huis1Gekocht:
            xpos 50
            ypos 150
    elif huisId == 2:
        show huis2Gekocht:
            xpos 50
            ypos 150
    elif huisId == 3:
        show huis3Gekocht:
            xpos 50
            ypos 150
    elif huisId == 4:
        show huis4Gekocht:
            xpos 50
            ypos 150
    elif huisId == 5:
        show huis5Gekocht:
            xpos 50
            ypos 150
    elif huisId == 6:
        show huis6Gekocht:
            xpos 50
            ypos 250

    
    if autoId == 1:
        show auto1:
            xpos 400
            ypos 650
    elif autoId == 2:
        show auto2:
            xpos 400
            ypos 650
    elif autoId == 3:
        show auto3:
            xpos 400
            ypos 650
    elif autoId == 4:
        show auto4:
            xpos 400
            ypos 650
    elif autoId == 5:
        show auto5:
            xpos 400
            ypos 650
    elif autoId == 6:
        show auto6:
            xpos 400
            ypos 650



    pause 1000
    # hide text
    # with dissolve


    # This ends the game.

    return


label plus:
    $ maandIndicatie +=1
    $ if maandIndicatie > 5: maandIndicatie = 0
    $ if maandIndicatie == 0: leeftijd +=1
    $ geld += (2*salaris)

    if maandIndicatie == 0 or maandIndicatie == 5:
        scene bgWinter
    elif maandIndicatie == 1 or maandIndicatie == 2:
        scene bgLente
    elif maandIndicatie == 3:
        scene bgZomer
    else:
        scene bgHerfst
    
    if huisId == 1:
        show huis1Gekocht:
            xpos 50
            ypos 150
    elif huisId == 2:
        show huis2Gekocht:
            xpos 50
            ypos 150
    elif huisId == 3:
        show huis3Gekocht:
            xpos 50
            ypos 150
    elif huisId == 4:
        show huis4Gekocht:
            xpos 50
            ypos 150
    elif huisId == 5:
        show huis5Gekocht:
            xpos 50
            ypos 150
    elif huisId == 6:
        show huis6Gekocht:
            xpos 50
            ypos 250
    

    if autoId == 1:
        show auto1:
            xpos 400
            ypos 650
    elif autoId == 2:
        show auto2:
            xpos 400
            ypos 650
    elif autoId == 3:
        show auto3:
            xpos 400
            ypos 650
    elif autoId == 4:
        show auto4:
            xpos 400
            ypos 650
    elif autoId == 5:
        show auto5:
            xpos 400
            ypos 650
    elif autoId == 6:
        show auto6:
            xpos 400
            ypos 650


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

    show screen textjob1
    show screen textjob2
    show screen textjob3
    show screen textjob4
    show screen textjob5
    show screen textjob6

    show screen salarispolitie
    show screen salarisbrandweer
    show screen salarisleerkracht
    show screen salarisdierenverzorg
    show screen salarisdoker
    show screen salariskapper

    show politieLogo:
        xpos 100
        ypos 100
    show brandweerLogo:
        xpos 100
        ypos 350
    show leerkrachtLogo:
        xpos 100
        ypos 600
    show dierenverzorgLogo:
        xpos 1000
        ypos 100
    show dokterLogo:
        xpos 1000
        ypos 350
    show kapper:
        xpos 1000
        ypos 600

    show text "{color=#000}Werk pagina (Klik op het loon om een job te selecteren.){/color}" at top
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
    show screen textHuis1
    show screen textHuis2
    show screen textHuis3
    show screen textHuis4
    show screen textHuis5
    show screen textHuis6

    show screen prijsHuis1
    show screen prijsHuis2
    show screen prijsHuis3
    show screen prijsHuis4
    show screen prijsHuis5
    show screen prijsHuis6

    show text "{color=#000}Huizen pagina (klik op de prijs om het huis te kopen){/color}" at top
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
    show huis6:
        xpos 1000
        ypos 550
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
    show screen textauto1
    show screen textauto2
    show screen textauto3
    show screen textauto4
    show screen textauto5
    show screen textauto6

    show screen prijsauto1
    show screen prijsauto2
    show screen prijsauto3
    show screen prijsauto4
    show screen prijsauto5
    show screen prijsauto6

    show text "{color=#000}auto pagina (klik op de prijs om de auto te kopen){/color}" at top

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
    
label werkTeJong:
    scene bgWerkHuisAuto

    hide screen plusButton
    hide screen werk
    hide screen docter
    hide screen winkel
    hide screen huizen
    hide screen autos

    show screen home

    show text "{color=#000}Je bent nog te jong om vast te mogen werken." at truecenter
    with dissolve
    pause 10000

# start text boxes rechtsboven
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
#eind text boxes rechtsboven


#start knoppen
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
        if leeftijd >= 18:
            action [ToggleScreen("werk"), Jump("Jobs")]
        else:
            action [ToggleScreen("werk"), Jump("werkTeJong")]

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

#eind knoppen

#start beschrijving huizen
screen textHuis1:
    vbox:
        xpos 0.17
        ypos 0.15
        text "{color=#000}Een groot luxe huis.{/color}" 

screen textHuis2:
    vbox:
        xpos 0.17
        ypos 0.40
        text "{color=#000}Een mooi groot huis.{/color}"

screen textHuis3:
    vbox:
        xpos 0.17
        ypos 0.63
        text "{color=#000}Een zeer groot huis{/color}"

screen textHuis4:
    vbox:
        xpos 0.65
        ypos 0.15
        text "{color=#000}Een groot huis.{/color}"


screen textHuis5:
    vbox:
        xpos 0.65
        ypos 0.40
        text "{color=#000}Een klein tof huisje.{/color}"


screen textHuis6:
    vbox:
        xpos 0.65
        ypos 0.63
        text "{color=#000}Een algemeen huisje.{/color}"
#eind beschrijving huizen

#start prijzen huizen
screen prijsHuis1:
    vbox:
        xpos 0.40
        ypos 0.15
        if geld >= 500000:
            textbutton "{color=#0F0}€500 000{/color}" action [SetVariable("geld", geld - 500000),SetVariable("huisId", 1), Jump("start") ]
        else:
            text "{color=#F00}€500 000{/color}"

screen prijsHuis2:
    vbox:
        xpos 0.40
        ypos 0.40
        if geld >= 350000:
            textbutton "{color=#0F0}€350 000{/color}" action [SetVariable("geld", geld - 350000),SetVariable("huisId", 2), Jump("start") ]
        else:
            text "{color=#F00}€350 000{/color}"

screen prijsHuis3:
    vbox:
        xpos 0.40
        ypos 0.63
        if geld >= 900000:
            textbutton "{color=#0F0}€900 000{/color}" action [SetVariable("geld", geld - 900000),SetVariable("huisId", 3), Jump("start") ]
        else:
            text "{color=#F00}€900 000{/color}"

screen prijsHuis4:
    vbox:
        xpos 0.90
        ypos 0.15
        if geld >= 280000:
            textbutton "{color=#0F0}€280 000{/color}" action [SetVariable("geld", geld - 280000),SetVariable("huisId", 4), Jump("start") ]
        else:
            text "{color=#F00}€280 000{/color}"


screen prijsHuis5:
    vbox:
        xpos 0.90
        ypos 0.40
        if geld >= 150000:
            textbutton "{color=#0F0}€150 000{/color}" action [SetVariable("geld", geld - 150000),SetVariable("huisId", 5), Jump("start") ]
        else:
            text "{color=#F00}€150 000{/color}"


screen prijsHuis6:
    vbox:
        xpos 0.90
        ypos 0.63
        if geld >= 215000:
            textbutton "{color=#0F0}€215 000{/color}" action [SetVariable("geld", geld - 215000),SetVariable("huisId", 6), Jump("start") ]
        else:
            text "{color=#F00}€215 000{/color}"

#eind prijzen huizen

#start beschrijving auto's
screen textauto1:
    vbox:
        xpos 0.17
        ypos 0.15
        text "{color=#000}Een groene jeep.{/color}" 

screen textauto2:
    vbox:
        xpos 0.17
        ypos 0.40
        text "{color=#000}Een blauwe sedan.{/color}"

screen textauto3:
    vbox:
        xpos 0.17
        ypos 0.63
        text "{color=#000}Een grijze cabrio.{/color}"

screen textauto4:
    vbox:
        xpos 0.65
        ypos 0.15
        text "{color=#000}Een rode smart.{/color}"


screen textauto5:
    vbox:
        xpos 0.65
        ypos 0.40
        text "{color=#000}Een licht blauwe pickup.{/color}"


screen textauto6:
    vbox:
        xpos 0.65
        ypos 0.63
        text "{color=#000}Een donker groene SUV.{/color}"
#eind beschrijving auto's

#start prijzen auto's
screen prijsauto1:
    vbox:
        xpos 0.40
        ypos 0.15
        if geld >= 68000:
            textbutton "{color=#0F0}€68 000{/color}" action [SetVariable("geld", geld - 68000),SetVariable("autoId", 1), Jump("start") ]
        else:
            text "{color=#F00}€68 000{/color}"

screen prijsauto2:
    vbox:
        xpos 0.40
        ypos 0.40
        if geld >= 25000:
            textbutton "{color=#0F0}€25 000{/color}" action [SetVariable("geld", geld - 25000),SetVariable("autoId", 2), Jump("start") ]
        else:
            text "{color=#F00}€25 000{/color}"

screen prijsauto3:
    vbox:
        xpos 0.40
        ypos 0.63
        if geld >= 118300:
            textbutton "{color=#0F0}€118 300{/color}" action [SetVariable("geld", geld - 118300),SetVariable("autoId", 3), Jump("start") ]
        else:
            text "{color=#F00}€118 300{/color}"

screen prijsauto4:
    vbox:
        xpos 0.90
        ypos 0.15
        if geld >= 17900:
            textbutton "{color=#0F0}€17 900{/color}" action [SetVariable("geld", geld - 17900),SetVariable("autoId", 4), Jump("start") ]
        else:
            text "{color=#F00}€17 900{/color}"


screen prijsauto5:
    vbox:
        xpos 0.90
        ypos 0.40
        if geld >= 45000:
            textbutton "{color=#0F0}€45 000{/color}" action [SetVariable("geld", geld - 45000),SetVariable("autoId", 5), Jump("start") ]
        else:
            text "{color=#F00}€45 000{/color}"


screen prijsauto6:
    vbox:
        xpos 0.90
        ypos 0.63
        if geld >= 35800:
            textbutton "{color=#0F0}€35 800{/color}" action [SetVariable("geld", geld - 35800),SetVariable("autoId", 6), Jump("start") ]
        else:
            text "{color=#F00}€35 800{/color}"

#eind prijzen auto's

#start beschrijving jobs
screen textjob1:
    vbox:
        xpos 0.17
        ypos 0.15
        text "{color=#000}Politie{/color}" 

screen textjob2:
    vbox:
        xpos 0.17
        ypos 0.40
        text "{color=#000}Brandweer{/color}"

screen textjob3:
    vbox:
        xpos 0.17
        ypos 0.63
        text "{color=#000}Leerkracht{/color}"

screen textjob4:
    vbox:
        xpos 0.65
        ypos 0.15
        text "{color=#000}Dierenverzorger{/color}"


screen textjob5:
    vbox:
        xpos 0.65
        ypos 0.40
        text "{color=#000}Dokter{/color}"


screen textjob6:
    vbox:
        xpos 0.65
        ypos 0.63
        text "{color=#000}kapper{/color}"
#eind beschrijving jobs

#start salaris jobs
screen salarispolitie:
    vbox:
        xpos 0.35
        ypos 0.15
        textbutton "{color=#000}€2500/maand{/color}" action [SetVariable("job", "Politie"), SetVariable("salaris", 2500), Jump("start")]

screen salarisbrandweer:
    vbox:
        xpos 0.35
        ypos 0.40
        textbutton "{color=#000}€3000/maand{/color}" action [SetVariable("job", "Brandweer"), SetVariable("salaris", 3000), Jump("start")]

screen salarisleerkracht:
    vbox:
        xpos 0.35
        ypos 0.63
        textbutton "{color=#000}€4000/maand{/color}" action [SetVariable("job", "Leerkracht"), SetVariable("salaris", 4000), Jump("start")]

screen salarisdierenverzorg:
    vbox:
        xpos 0.85
        ypos 0.15
        textbutton "{color=#000}€2000/maand{/color}" action [SetVariable("job", "Dierenverzorger"), SetVariable("salaris", 2000), Jump("start")]


screen salarisdoker:
    vbox:
        xpos 0.85
        ypos 0.40
        textbutton "{color=#000}€4900/maand{/color}" action [SetVariable("job", "Dokter"), SetVariable("salaris", 4900), Jump("start")]


screen salariskapper:
    vbox:
        xpos 0.85
        ypos 0.63
        textbutton "{color=#000}€1700/maand{/color}" action [SetVariable("job", "Kapper"), SetVariable("salaris", 1700), Jump("start")]

#eind salaris jobs
