#Backgrounds
image bg exterieur memorial = "exterieur_memorial.jpg"
image bg excelior = "excelior_world.jpg"
image bg quartier residentiel = "quartier_residentiel.jpg"
image bg rdc memorial = "rdc_memorial.jpg"
image bg toilettes = "hall_memorial.jpg"
image bg caleche = "caleche.jpg"
image bg poste securite = "poste_securite.jpg"
image bg bibliotheque = "bibliotheque.jpg"
image bg sommet memorial = "sommet_memorial.jpg"
image bg la rose noire = "la_rose_noire.png"
image bg logo = "logo.jpg"
image bg generique = "generique.jpg"

#Déclaration des personnages en jeu
define l = Character('Leily', color="FF7E33")
define g = Character('Gardien', color="0DC10D")
define m = Character('Minerve', color="8A41E8")
define c = Character('Capitaine', color="D08A03")
define ma = Character('Matelot', color="07A9DB")
define p = Character('Pirate', color="CD012B")
define cm = Character('Commanditaire', color="D00348")

#Personnages
image leily neutre = "images/leily_neutre.png"
image leily defiante = "images/leily_defiance.png"
image leily proteste = "images/leily_proteste.png"
image leily confiante = "images/leily_confiante.png"
image leily soucieuse = "images/leily_soucis.png"
image leily amuse = "images/leily_amuse.png"
image leily contrarie = "images/leily_contrariee.png"
image leily desolee = "images/leily_desolee.png"
image leily fiere = "images/leily_fiere.png"
image leily idee = "images/leily_idee.png"
image leily moqueuse = "images/leily_moqueuse.png"
image leily nargue = "images/leily_nargue.png"
image leily gaffeuse = "images/leily_gaffeuse.png"
image leily soupir = "images/leily_soupir.png"
image leily surprise = "images/leily_surprise.png"
image leily triste = "images/leily_triste.png"

image gardien 1 = "images/gardien_1_sourire.png"
image gardien 1 dubitatif = "images/gardien_1_dubitatif.png"
image gardien 1 avertissement = "images/gardien_1_avertissement.png"
image gardien 1 surprise = "images/gardien_1_surprise.png"
image jack = "images/gardien_2.png"
image gardien 3 = "images/gardien_3.png"
image romuald = "images/gardien_4.png"

image minerve = "images/minerve_neutre.png"
image minerve irritee = "images/minerve_irritee.png"
image minerve colerique = "images/minerve_colere.png"
image minerve menace = "images/minerve_menace.png"
image minerve agacee = "images/minerve_agacee.png"
image minerve certaine = "images/minerve_certaine.png"
image minerve contrariee = "images/minerve_contrariee.png"
image minerve ecoute = "images/minerve_ecoute.png"
image minerve hautaine = "images/minerve_hautaine.png"
image minerve moqueuse = "images/minerve_moqueuse.png"
image minerve rire = "images/minerve_rire.png"
image minerve satisfaite = "images/minerve_satisfaite.png"
image minerve soupir = "images/minerve_soupir.png"
image minerve surprise = "images/minerve_soupir.png"

#Avatar
image side leily neutre = "images/avatar_leily_neutre.png"
image side leily defiante = "images/avatar_leily_defiante.png"
image side leily proteste = "images/avatar_leily_proteste.png"
image side leily confiante = "images/avatar_leily_confiante.png"
image side leily soucieuse = "images/avatar_leily_soucis.png"
image side leily amuse = "images/avatar_leily_amusee.png"
image side leily contrarie = "images/avatar_leily_contrariee.png"
image side leily desolee = "images/avatar_leily_desolee.png"
image side leily fiere = "images/avatar_leily_fiere.png"
image side leily idee = "images/avatar_leily_idee.png"
image side leily moqueuse = "images/avatar_leily_moqueuse.png"
image side leily nargue = "images/avatar_leily_nargue.png"
image side leily gaffeuse = "images/avatar_leily_gaffeuse.png"
image side leily soupir = "images/avatar_leily_soupir.png"
image side leily surprise = "images/avatar_leily_surprise.png"
image side leily triste = "images/avatar_leily_triste.png"
image side leily colere = "images/avatar_leily_colere.png"

#Assets
image element feu = "images/element_fire.png"
image element eau = "images/element_water.png"
image element air = "images/element_wind.png"
image element terre = "images/element_earth.png"
image ecosphere = "images/ecosphere_asset.png"
image piedestal ecosphere = "images/piedestal_sprite.png"
image neptune = "images/neptune.png"
image montre gousset = "images/montre_gousset.png"
image fragment perle = "images/fragment_perle.png"

#Sauvegarde automatique
define config.autosave_frequency = 200
define config.autosave_on_choice = True

#Timer choix narratifs (documentation Ren'py)
# How long the player has to make a choice in timeout seconds.
default timeout = 5.0

# The label the player is sent to if they fail to make a choice in the time
# allotted. If None, the timeout is disabled.
default timeout_label = None

# A preference that enables or disables timed choices.
default persistent.timed_choices = True

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    if (timeout_label is not None) and persistent.timed_choices:

        bar:
            xalign 0.5
            ypos 0
            xsize 1280
            ysize 10
            value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=timeout)
            left_bar "#FF0000"
            right_bar "#000000cc"

        timer timeout action Jump(timeout_label)


#Début du jeu

label start:
    scene bg exterieur memorial
    with fade

    play music "audio/memorial_exterieur.WAV"

    "Les visiteurs affluent des quatre coins du monde d’Excelior pour se rendre au Mémorial, bâti en l’honneur d’un grand héros."
    "Et je suis dans la file d'attente depuis plus d'une heure !"

    show leily neutre
    with moveinleft

    "Mon nom est Leily Stirner."
    "Comme tous les visiteurs, je dois passer devant un poste de sécurité pour être fouillée."
    "Les Gardiens s’assurent que personne ne porte d’armes."
    "Et justement, voici mon tour !"

    hide leily
    with dissolve
    show gardien 1
    with ease

    show side leily neutre onlayer overlay:
        pos (0,715)

    g "Suivante."

    show side leily defiante onlayer overlay:
        pos (0,715)
    "S'il pense pouvoir me tripoter de la sorte, il se trompe !"

    show side leily proteste onlayer overlay:
        pos (0,715)
    l "Pas touche, mon cher ! J’ai une nette préférence pour les dames."

    show side leily neutre onlayer overlay:
        pos (0,715)

    show gardien 1 dubitatif
    g "..."

    show side leily neutre onlayer overlay:
        pos (0,715)
    "Il regarde en direction d'une autre gardienne. Sa supérieure hiérarchique, je suppose."

    show gardien 1 with moveinleft:
        xalign 0.75
        yalign 1.0

    show minerve with moveinleft:
        xalign 0.25
        yalign 1.0

    show side leily neutre onlayer overlay:
        pos (0,715)

    m "C'est bon, je m'en occupe."

    show side leily neutre onlayer overlay:
        pos (0,715)

    show gardien 1:
        xalign 0.75
        yalign 1.0
    g "À vos ordres, Officière Minerve !"

    show side leily neutre onlayer overlay:
        pos (0,715)
    m "Veuillez avancer, et vite."

    $ timeout_label = None

    menu:
        "Obtempérer":
            jump plan001

        "Et puis quoi, encore ?":
            jump plan002


    label plan001:

        "Je m’exécute et j’avance vers elle."
        jump plan003


    label plan002:

        "Je n'aime pas ce ton... Voyons voir si sa patience a des limites !"

        show side leily confiante onlayer overlay:
            pos (0,715)
        l "Je regrette mais je ne suis pas d'humeur à obéir bien sagement !"

        show minerve colerique:
            xalign 0.25
            yalign 1.0

        show gardien 1 dubitatif:
            xalign 0.75
            yalign 1.0

        show side leily neutre onlayer overlay:
            pos (0,715)

        m "Et moi, vu la queue, je ne suis pas d'humeur à faire mumuse."

        show side leily soucieuse onlayer overlay:
            pos (0,715)

        m "Alors obéissez ou dégagez !"

        show side leily soucieuse onlayer overlay:
            pos (0,715)
        "Pas très commode, la dame..."

        show side leily neutre onlayer overlay:
            pos (0,715)
        l "Bon, bon... On se calme."

        jump plan003


    label plan003:

        show minerve:
            xalign 0.25
            yalign 1.0
        show gardien 1:
            xalign 0.75
            yalign 1.0

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Je tends mes bras en croix pour la laisser faire."

        play sound "audio/fouille_1.WAV"

        show side leily defiante onlayer overlay:
            pos (0,715)
        "Elle me palpe rapidement, on voit qu’elle a le coup de main !"

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Par chance, le dispositif discrètement logé dans mon oreille passe inaperçu. C’est un émetteur radio."

        show side leily neutre onlayer overlay:
            pos (0,715)

        m "Aucune arme, rien à signaler."

        show side leily confiante onlayer overlay:
            pos (0,715)
        l "Je confirme, désarmée jusqu’au bout des ongles !"

        show minerve menace:
            xalign 0.25
            yalign 1.0

        show side leily neutre onlayer overlay:
            pos (0,715)
        m "Par contre, un détail m'intrigue."

        show side leily soucieuse onlayer overlay:
            pos (0,715)
        "Elle regarde les marques apposées sur le dos de chacune de mes mains."

        show side leily soucieuse onlayer overlay:
            pos (0,715)
        "L'Affinité."

        hide minerve
        hide gardien 1

#Sequence002

    scene bg excelior
    with fade

    play music "audio/monde_excelior.WAV" fadeout 1

    "Depuis les origines du monde d'Excelior, ses habitants naissent avec une Affinité."
    "Il en existe quatre : une par élément naturel."

    play sound "audio/element_feu.WAV"

    show element feu with moveinleft:
        pos (400,350)

    "Le Feu."

    play sound "audio/element_eau.WAV"

    show element eau with moveinleft:
        pos (700,350)

    "L'Eau."

    play sound "audio/element_terre.WAV"

    show element terre with moveinleft:
        pos (1000,350)

    "La Terre."

    play sound "audio/element_air.WAV"

    show element air with moveinleft:
        pos (1300,350)

    "L'Air."

    hide element air

    "Cette marque est gravée à même la chair, sur le dos de chaque main, tel un pacte avec la nature."
    "Et permet à tout à chacun de contrôler l'élément qui lui a été affilié à la naissance."
    "J’ai la particularité d’en avoir deux : l’Eau et l’Air."

#Sequence003

    scene bg exterieur memorial
    with fade

    play music "audio/memorial_exterieur.WAV"

    show minerve:
        xalign 0.25
        yalign 1.0

    show gardien 1:
        xalign 0.75
        yalign 1.0

    with dissolve

    m "Deux Affinités ? C'est extrêmement rare..."

    show side leily neutre onlayer overlay:
        pos (0,715)
    m "Rappellez-moi votre nom ?"

    show side leily confiante onlayer overlay:
        pos (0,715)
    l "Capitaine Leily Stirner !"

    show side leily neutre onlayer overlay:
        pos (0,715)
    m "Hmm… ça me dit quelque chose."

    hide gardien 1

    show minerve with move:
        xalign 0.75
        yalign 1.0

    show gardien 3 with move:
        xalign 0.25
        yalign 1.0

    show side leily surprise onlayer overlay:
        pos (0,715)
    "Au même moment, j’aperçois l’autre garde en train de trifouiller des documents accrochés sur le mur du poste de sécurité."

    show side leily surprise onlayer overlay:
        pos (0,715)
    "Vraisemblablement des avis de recherches…"
    show side leily surprise onlayer overlay:
        pos (0,715)
    "Il en décroche un et le tend à sa supérieure."

    with vpunch

    show side leily contrarie onlayer overlay:
        pos (0,715)
    g "Officière Minerve, attendez !"

    show side leily soucieuse onlayer overlay:
        pos (0,715)
    "Elle commence à lire le document."

    show side leily soucieuse onlayer overlay:
        pos (0,715)
    m "C’est bien ce que je pensais…"

    show side leily soucieuse onlayer overlay:
        pos (0,715)
    m "Vous êtes la Princesse des pirates, dont l'équipage met un point d'honneur à ne jamais tuer personne."

    show side leily moqueuse onlayer overlay:
        pos (0,715)
    l "Ravie de voir que ma réputation me précède !"

    show minerve irritee:
        xalign 0.75
        yalign 1.0

    show side leily soucieuse onlayer overlay:
        pos (0,715)
    m "Mais malgré cette « qualité », vous n’en restez pas moins une maudite pirate !"

    show side leily soucieuse onlayer overlay:
        pos (0,715)
    m "Vols, coups et blessures, enlèvements..."

    hide gardien 3

    show minerve colerique with move:
        xalign 0.25
        yalign 1.0
    show gardien 1 avertissement:
        xalign 0.75
        yalign 1.0

    with move and vpunch

    show side leily soucieuse onlayer overlay:
        pos (0,715)
    g "Nous devrions vous arrêter sur le champs !"

    show side leily colere onlayer overlay:
        pos (0,715)
    "Bigre ! Ils sont déjà prêts à me mettre le grappin dessus."

    show side leily soupir onlayer overlay:
        pos (0,715)
    "Entrer par la porte principale risque d’être compliqué..."

    $ timeout_label = "plan005"

    menu:
        "Tenter de négocier":
            jump plan004

        "Chercher une autre issue":
            jump plan005

    label plan004:

        "Mais heureusement pour moi, j’avais tout prévu !"

        show side leily neutre onlayer overlay:
            pos (0,715)
        "De mon index, j’abaisse l’avis de recherche des yeux de mon interlocutrice pour croiser à nouveau son regard."

        show side leily amuse onlayer overlay:
            pos (0,715)
        l "Vous savez aussi bien que vous n’avez pas le droit de m’arrêter ici."

        show minerve surprise:
            xalign 0.25
            yalign 1.0

        show side leily amuse onlayer overlay:
            pos (0,715)
        m "..."

        hide gardien 1

        show minerve surprise with move:
            xalign 0.75
            yalign 1.0
        show gardien 3 with ease:
            xalign 0.25
            yalign 1.0

        show side leily neutre onlayer overlay:
            pos (0,715)
        g "Malheureusement elle n’a pas tort, cheffe."

        show minerve contrariee:
            xalign 0.75
            yalign 1.0

        show side leily fiere onlayer overlay:
            pos (0,715)
        "Et oui ! Un décret oblige tout citoyen à se rendre au moins une fois au Mémorial."

        show side leily fiere onlayer overlay:
            pos (0,715)
        "Par devoir de mémoire envers le héros à qui est dédié ce monument."

        show minerve agacee:
            xalign 0.75
            yalign 1.0

        play sound "audio/avis_recherche.WAV"

        show side leily surprise onlayer overlay:
            pos (0,715)
        "L’officière Minerve froisse soudain l’avis de recherche."

        show side leily neutre onlayer overlay:
            pos (0,715)
        m "Une pirate qui respecte la loi… On aura tout vu !"

        show side leily neutre onlayer overlay:
            pos (0,715)
        m "Retournez tous à vos postes."

        hide gardien 3
        show minerve at center with move

        show side leily neutre onlayer overlay:
            pos (0,715)
        m "Mais j’y pense, je ne vois pas votre célèbre équipage..."

        show side leily moqueuse onlayer overlay:
            pos (0,715)
        l "Ils sont à bord de mon navire, la Rose noire."

        show side leily moqueuse onlayer overlay:
            pos (0,715)
        l "J’ai décidé de profiter de cette magnifique journée pour visiter le Mémorial !"

        show minerve satisfaite at center

        show side leily neutre onlayer overlay:
            pos (0,715)
        m "Voyez-vous ça…"

        show side leily neutre onlayer overlay:
            pos (0,715)
        m "Vous pouvez passer, si vous y tenez tant."

        show side leily amuse onlayer overlay:
            pos (0,715)
        "Je ne peux m’empêcher d’esquisser un sourire de victoire."

        show side leily amuse onlayer overlay:
            pos (0,715)
        l "Fort bien ! Dans ce cas, je vais prendre congé immédiatement."

        "Alors que je m'éloigne, j'aperçois son sous-fifre s'approcher pour lui murmurer quelque chose à l'oreille."

        show minerve with move:
            xalign 0.25
            yalign 1.0

        show gardien 1 dubitatif with moveinright:
            xalign 0.75
            yalign 1.0

        g "Vous êtes sûre, Cheffe ?"
        g "J’ai un mauvais pressentiment…"

        show minerve hautaine:
            xalign 0.25
            yalign 1.0

        m "Vous rigolez, j’espère ?"
        m "On doit la laisser entrer dans le Mémorial mais rien n’oblige à la laisser sortir. Libre, en tout cas…"
        m "Gardez-là à l’œil ! Si elle fait le moindre écart, enfermez-là dans le poste de sécurité."

        show minerve rire:
            xalign 0.25
            yalign 1.0
        m "Si jamais elle se tient tranquille, cueillez-là à la sortie !"

        show gardien 1:
            xalign 0.75
            yalign 1.0
        g "À vos ordres !"

        hide minerve
        hide gardien 1

        jump plan012


    label plan005:

    show minerve:
        xalign 0.25
        yalign 1.0

    show gardien 1 dubitatif:
        xalign 0.75
        yalign 1.0

    "La situation devient tendue... Il vaut mieux passer par une autre entrée."

    show side leily moqueuse onlayer overlay:
        pos (0,715)
    "Ne nous énervons pas, je vais simplement me retirer..."

    show side leily confiante onlayer overlay:
        pos (0,715)
    "Mais je ne manquerai pas d'indiquer aux autorités que vous m'avez empêché d'accomplir mon devoir de citoyenne !"

    show minerve colerique:
        xalign 0.25
        yalign 1.0

    show side leily confiante onlayer overlay:
        pos (0,715)

    m "Cette fois, vous dépassez les bornes ! Hors de ma vue !"

    show side leily soupir onlayer overlay:
        pos (0,715)
    "Elle ne manque pas d’entrain cette bougresse !"

    show minerve:
        xalign 0.25
        yalign 1.0

    show side leily soupir onlayer overlay:
        pos (0,715)
    "Mieux vaut éviter de m’attirer des ennuis si je ne veux pas compromettre l’opération."

    show side leily neutre onlayer overlay:
        pos (0,715)
    "Je décide de m’éloigner du poste de sécurité."

    hide minerve
    hide gardien 1

    jump plan006

#Sequence004

    label plan006:

        show bg quartier residentiel
        with fade

        play music "audio/quartier_residentiel.WAV" fadeout 1

        show leily neutre at center
        with moveinleft

        "Je me dirige vers le quartier résidentiel à proximité du Mémorial, qui accueille les visiteurs désirant y passer plusieurs jours."
        "Un port se trouve sur les lieux. Des navires font la navette le long du fleuve pour approvisionner régulièrement les commerçants."
        "Et justement, je vois un navire mouillant sur les quais !"
        "Une calèche se trouve à côté, l’équipage est en train d’y charger une cargaison provenant du bateau."

        ma "Qu’est-ce qu’il leur prend de commander autant ?"
        c "T’occupes pas, notre boulot du jour c’est faire la livraison aux Gardiens."
        c "On s’occupe de leur déposer la cargaison derrière le poste de sécurité. Le reste, c’est leur problème !"

        show leily confiante at center
        with dissolve
        "Mais voilà qui tombe à pic !"

        show leily neutre at center
        with dissolve
        "Alors que les marins retournent à bord chercher une autre caisse, je lance un regard discret sur la marchandise."
        "La plupart des caisses contiennent de la nourriture et des biens de première nécessité, probablement pour l’équipe de sécurité."
        "Et effectivement, la calèche est pleine à craquer !"
        "Une énorme caisse remplie d’armes est entreposée au fond, je pourrais me cacher derrière... C’est risqué mais j’ai mes chances d’entrer dans le Mémorial !"

        $ timeout_label = None

        menu:

            "Se cacher dans la calèche":
                jump plan008

            "Chercher une autre entrée":
                jump plan007


    label plan007:

        show leily contrarie at center
        with dissolve

        "Hmm... Trop risqué, ils vont sûrement contrôler la marchandise une fois livrée."
        "Je regarde à nouveau aux alentours."
        "Puis je remarque un conteneur près d’un embarcadère, à l’abri des regards."

        play sound "audio/couvercle.WAV"

        "Je m'approche pour soulever le couvercle, il contient des poussières et des restes de gravas."

        show leily idee at center
        with dissolve
        "Intéressant..."

        show leily amuse at center
        with dissolve

        "Je regarde en direction du Mémorial. L'aile Ouest est effectivement en chantier, les ouvriers sont en plein travail."
        "J'aperçois l'un d'entre eux qui jette des gravas dans un conteneur similaire s’y trouve. Il est presque plein."
        "Très intéressant... Le conteneur vide se trouve probablement à proximité du port pour qu'un navire vienne évacuer les gravas."
        "Si mon hypothèse est exacte, les ouvriers vont bientôt venir intervertir les deux conteneurs..."
        "Il y a plus élégant comme entrée en matière mais c’est le moyen le plus simple d’entrer."

        show leily confiante at center
        with dissolve

        "Les Gardiens ne vérifieront certainement pas à l’intérieur. Personne n’aurait l’idée de se cacher dans un conteneur poussiéreux… À part la Princesse des pirates, bien sûr !"

        show leily neutre at center
        with dissolve

        "Je m’assure que personne ne me regarde et je me faufile dans le conteneur."

        play sound "audio/conteneur.WAV"

        hide leily neutre at center
        with fade

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Puis j’attends, un moment."

        show side leily contrarie onlayer overlay:
            pos (0,715)
        "Un long moment..."

        show side leily amuse onlayer overlay:
            pos (0,715)
        "Puis des voix finissent par se faire entendre. Quelqu'un saisit le conteneur et commence à le pousser, ce sont deux ouvrirers."

        show bg exterieur memorial
        with pixellate

        show minerve:
            xalign 0.25
            yalign 1.0

        show gardien 1:
            xalign 0.75
            yalign 1.0

        show side leily amuse onlayer overlay:
            pos (0,715)
        "Le conteneur s'arrête. J'entends les voix des Gardiens du poste de sécurité, ils laissent passer les ouvriers. Mes deux complices malgré eux !"

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Après qu’ils aient déposer le conteneur en bas du chantier, j’attendrai qu’ils s’éloignent pour entrer en scène !"

        show side leily confiante onlayer overlay:
            pos (0,715)
        "Me voilà enfin dans le Mémorial."

        hide minerve
        hide gardien 1

        jump plan012


#Sequence005

    label plan008:

        hide leily
        scene bg caleche
        with fade

        play music "audio/caleche.WAV" fadeout 1

        "Je me faufile au milieu de la cargaison."

        show side leily confiante onlayer overlay:
            pos (0,715)
        "Rien qu’à l’odeur, je devine qu’il y a du vin et du rhum. Les Gardiens ont l'air de ne rien se refuser pendant leur temps libre !"

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Les marins chargent les derrières caisses à l’entrée, sans même entrer dans la calèche."

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Ils ne remarquent pas ma présence, recroquevillée derrière la caisse d'armes."

        with vpunch
        play sound "audio/caleche_mouvement.WAV"

        show side leily contrarie onlayer overlay:
            pos (0,715)
        "Il y a soudain du mouvement, les chevaux se mettent à tirer la calèche."

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Cela dure un petit moment, puis la calèche s'arrête. Certainement devant le poste de sécurité."

        show minerve at center
        with moveinright

        show side leily surprise onlayer overlay:
            pos (0,715)
        "J’entends quelqu’un s’approcher."

        show side leily neutre onlayer overlay:
            pos (0,715)
        "À sa voix, je la reconnais : c’est l’officière de tout à l’heure."

        show side leily confiante onlayer overlay:
            pos (0,715)
        "C’est comment son nom déjà ? Oh, peu importe..."

        show side leily surprise onlayer overlay:
            pos (0,715)
        m "Je vais jeter un œil à la cargaison."

        play music "audio/urgence.WAV"

        show side leily proteste onlayer overlay:
            pos (0,715)
        "Euh... Là par contre, ça m’importe beaucoup plus !"

        show side leily contrarie onlayer overlay:
            pos (0,715)
        "Mon cœur se met à battre la chamade."

        show side leily colere onlayer overlay:
            pos (0,715)
        "Il faut réagir et vite !"

        $ timeout_label = "plan010"

        menu:
            "Rester cacher":
                jump plan009

            "Sortir de la calèche":
                jump plan010


    label plan009:

        show minerve menace at center

        m "Il y a une tonne de marchandises dedans ! Et même un ours en peluche !?"

        show side leily surprise onlayer overlay:
            pos (0,715)

        m "Ça va prendre des heures à contrôler tout ça, on a énormément de visiteurs aujourd’hui !"

        show side leily surprise onlayer overlay:
            pos (0,715)

        c "On a pourtant respecté votre commande à la lettre."

        show minerve irritee at center

        show side leily surprise onlayer overlay:
            pos (0,715)

        m "C’est pas faux, on a commandé de quoi tenir plusieurs mois… J’avais pas pensé au contrôle de la livraison."

        show side leily soucieuse onlayer overlay:
            pos (0,715)

        "Elle jette un dernier coup d’œil rapide."

        show minerve at center

        show side leily soucieuse onlayer overlay:
            pos (0,715)

        m "Bon… Tout à l’air en ordre."

        play music "audio/caleche.WAV" fadeout 1

        show side leily soupir onlayer overlay:
            pos (0,715)

        m "Allons dans mon bureau pour votre paiement."

        show side leily confiante onlayer overlay:
            pos (0,715)
        "Quel soulagement !"

        hide minerve
        with moveoutright

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Je les entends s’éloigner vers le poste de sécurité."

        play sound "audio/fouille_1.WAV"

        show leily neutre at center
        with moveinbottom

        show leily neutre at right
        with moveoutright

        "En me redressant, je constate que l’équipe à l’entrée est toujours occupée à palper les visiteurs."

        show leily amuse at right
        with dissolve

        "Un groupe d’une dizaine de visiteurs se dirige vers le Mémorial."
        "Je sors discrètement de ma cachette et me fonds en queue de peloton."

        show leily moqueuse at right
        with dissolve

        "Ni vue, ni connue !"

        hide leily

        jump plan012


    label plan010:

        "Une grille d'aération est située à mes pieds."

        show side leily colere onlayer overlay:
            pos (0,715)
        "Je m'y faufile en vitesse..."

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Et je parviens à m’extirper de ce bourbier !"

        stop music

        hide minerve
        show bg exterieur memorial
        with pixellate

        show side leily soupir onlayer overlay:
            pos (0,715)
        "C’était de justesse !"

        play sound "audio/element_eau.WAV"
        with vpunch

        show side leily surprise onlayer overlay:
            pos (0,715)
        "Mais soudain, une bombe acqueuse vient me frôler la joue."

        play sound "audio/rassemblement.WAV"

        show gardien 1 avertissement at center
        with moveinright

        show side leily surprise onlayer overlay:
            pos (0,715)

        g "Plus un geste !"

        show side leily colere onlayer overlay:
            pos (0,715)

        g "Cheffe, c’est la pirate de tout à l’heure !"

        show side leily soupir onlayer overlay:
            pos (0,715)
        "Repérée… J’aurais peut-être dût rester cachée."

#Sequence006

    label plan011:

        hide gardien 1
        scene bg poste securite
        with fade

        play music "audio/poste_securite.WAV" fadeout 1

        "Les Gardiens m’ont enfermé dans le bureau de l’Officière, situé dans le poste de sécurité."

        show minerve colerique
        with moveinleft

        show side leily contrarie onlayer overlay:
            pos (0,715)

        m "On dirait bien que le message n’est pas rentré !"

        show side leily contrarie onlayer overlay:
            pos (0,715)

        m "J’ai pris contact avec les autorités compétentes pour qu’ils viennent vous chercher."

        show minerve hautaine

        show side leily contrarie onlayer overlay:
            pos (0,715)

        m "Vous allez croupir en prison pour un bon moment !"

        show side leily confiante onlayer overlay:
            pos (0,715)
        l "Vous aimeriez vous en convaincre, n’est-ce pas ?"

        show minerve

        show side leily neutre onlayer overlay:
            pos (0,715)

        m "Je pense surtout que vous allez déchanter quand ils arriveront."

        show side leily surprise onlayer overlay:
            pos (0,715)

        m "Et ce sera pas volé !"

        show side leily neutre onlayer overlay:
            pos (0,715)
        "C'est ce qu'on va voir..."

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Après vérifié que j'étais bien menottée au siège, l’officière quitte la pièce. Elle a appelé un sous-fifre pour venir me surveiller."

        hide minerve
        with moveoutleft

        show side leily defiante onlayer overlay:
            pos (0,715)
        "Je n’ai que quelques instants pour agir !"

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Je garde toujours un outil de crochetage dissimulé dans ma longue chevelure."

        play sound "audio/crochetage.WAV"

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Avec son aide, je parviens à crocheter rapidement les menottes."

        show side leily amuse onlayer overlay:
            pos (0,715)
        "Je me cache derrière la porte pour surprendre le Gardien qui s’approche à grands pas."

        show gardien 1 at center
        with moveinleft

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Elle s’entrouvre."

        show gardien 1 dubitatif at center
        play sound "audio/coup_de_poing.WAV"
        with vpunch

        show side leily colere onlayer overlay:
            pos (0,715)
        "À peine le Gardien entre dans la pièce, je l’assomme d’un coup sec sur la nuque."

        hide gardien 1
        with moveoutbottom

        show side leily defiante onlayer overlay:
            pos (0,715)
        "Je le retiens pour éviter que le choc au sol n’alerte ses collègues, puis je l’adosse contre le mur."

        show side leily confiante onlayer overlay:
            pos (0,715)
        "Il va faire une sieste un bon moment !"

        show leily contrarie at center
        with moveinbottom

        "Je passe discrètement la tête pour regarder à l’extérieur, l’équipe de sécurité se trouve juste devant le poste."
        "Hors de question de sortir par l’entrée principale !"

        show leily neutre at center
        with dissolve

        "Mais j’aperçois un groupe d’une dizaine de visiteurs passer la zone de contrôles, je pense pouvoir m’infiltrer parmi eux."
        "J’ouvre la fenêtre du bureau et que l’enjambe discrètement avant que le groupe de visiteurs ne me remarque."

        show bg exterieur memorial
        with pixellate

        play music "audio/memorial_exterieur.WAV" fadeout 1

        "Et j’attends un instant, adossée au mur d’un air innocent."
        "Lorsque les visiteurs passent à mon niveau, je me faufile derrière eux et leur emboîte le pas."
        "Les Gardiens ne remarquent rien, toute leur attention est consacrée au contrôle des visiteurs."

        show leily confiante at center
        with dissolve

        "J’entre dans le Mémorial, incognito !"

        hide leily

        jump plan012

#Sequence007

    label plan012:

        scene bg rdc memorial
        with fade

        play music "audio/rdc_memorial.WAV" fadeout 1

        show leily neutre at center
        with moveinright

        "Je traverse l’immense porte qui marque l’entrée du Mémorial."
        "Et l’intérieur est des plus somptueux !"
        "Un large vitrail domine le rez-de-chaussée, représentant l'affrontement entre un héros et un colosse de métal."
        "Les rayons du soleil qui le traversent donnent lieu à une atmosphère aussi paisible que colorée."
        "Mais pas le temps de faire du tourisme ! L’objet de toutes mes convoitises est enfin à portée de main : l’Écosphère."

        show piedestal ecosphere with zoomin:
            pos (400,475)

        play sound "audio/ecosphere.WAV"

        "C'est un orbe capable de contrôler la nature : pour faire simple, il permet de maîtriser les quatre éléments simultanément !"
        "Un commanditaire m'a mandaté pour le dérober... D'où ma présence ici !"
        "Mon précieux butin trône au centre du rez-de-chaussée, sur un piédestal en marbre, de manière à être la première chose que les visiteurs découvrent en entrant."

        show leily contrarie at center
        with dissolve

        "Mais quelque chose me turlupine… Aucune vitrine de protection, ni garde à proximité ?"
        "De plus, il a l'air tout neuf !"
        "C'est vraiment étrange..."

        $ timeout_label = None

        menu:

            "Chercher des indices":
                jump plan013

            "Voler directement l'Écosphère":
                jump plan014


    label plan013:

        show leily neutre at center
        with dissolve

        "D'autres éléments sont exposés au Rez-de-chaussée, les affichettes d'information qui les accompagnent me renseigneront sûrement !"

        show leily neutre at left
        with moveinright
        with dissolve

        "Je jette un oeil du côté du vitrail."
        "Ce mémorial est construit en l'honneur du Maître Ingénieur : Conrad Kross."
        "Il était connu pour avoir mis au point des inventions des plus remarquables, comme le géant de métal représenté sur le vitrail."
        "Ce dernier symbolise en réalité une intelligence artificielle qui régulait la pollution en contrôlant l’activité des machines."
        "Sa mission était de protéger la nature. Nom de code du projet : Programme Jénius."

        show leily neutre at right
        with moveinleft
        with dissolve

        "Je m'approche d'une modélisation à son effigie, accompagnée de plans de conception."
        "Ce programme arriva à la conclusion que le seul moyen de protéger la nature était d’éradiquer la cause de toute pollution : l'espèce humaine."

        show leily moqueuse at right
        with dissolve

        "Un monde sans humains, voilà qui aurait pu me séduire !"

        show leily contrarie at right
        with dissolve

        "Mais je dois avouer que l’extermination de masse m’enchante beaucoup moins…"
        "Une terrible guerre éclata entre humains et machines, il y a une douzaine d'années."
        "Avec d’innombrables victimes et une cité entière fut réduite à néant, Global City."

        show leily contrarie at center
        with moveinright
        with dissolve

        "Rongé par la culpabilité d’avoir crée un tel monstre, c’est à ce moment que Conrad Kross inventa l’Écosphère."
        "L’orbe donna au Maître Ingénieur le pouvoir de contrôler les quatre éléments naturels. L’Eau, la Terre, le Feu et l’Air devinrent ses armes face aux machines."

        show leily triste at center
        with dissolve

        "Il finit par triompher de l’intelligence artificielle… Au prix de sa propre vie."
        "Ce Mémorial a été bâti en l’honneur de son sacrifice et chaque citoyen du monde d’Excelior doit s’y rendre au moins une fois dans sa vie."

        show leily soucieuse at center
        with dissolve

        "La plupart des gens y voient un acte d’héroïsme, moi j’y vois une profonde injustice."
        "Au nom de quoi devrait-on donner sa vie pour sauver celles de tous les autres ? Sans rien en retour par dessus le marché !"
        "Ça me dépasse…"

        show leily soupir at center
        with dissolve

        "Hmmm... Toujours rien à l’horizon pour expliquer pourquoi cet orbe a l’air tout neuf !"

        $ timeout_label = "plan017"

        menu:

            "Dérober l'Écosphère":
                jump plan014

            "Contacter le Commanditaire":
                jump plan017

#Sequence008

    label plan014:

        show leily neutre at center
        with dissolve

        "Je m’approche du piédestal en marbre et je me saisis de l’Écosphère."

        hide piedestal ecosphere
        with moveoutbottom

        play music "audio/urgence.WAV" fadeout 1
        play sound "audio/ecosphere.WAV"

        "Alors que je m'éloigne avec célérité, plusieurs visiteurs crient à l’aide. Les scélérats !"
        "Mais c’est inutile, je vais grimper sommet du Mémorial et gagner du temps jusqu’à ce que..."

        hide leily
        play sound "audio/element_feu.WAV"
        with vpunch

        show side leily colere onlayer overlay:
            pos (0,715)
        "Jusqu’à ce qu’une boule de feu vienne me heurter de plein fouet pour stopper mon élan !"

        play sound "audio/rassemblement.WAV"
        stop music fadeout 1.0

        show romuald at center
        with moveinleft

        show side leily contrarie onlayer overlay:
            pos (0,715)

        g "Halte !"

        show side leily soucieuse onlayer overlay:
            pos (0,715)
        "Un Gardien était en embuscade près de l’entrée du Mémorial."

        show side leily soucieuse onlayer overlay:
            pos (0,715)

        g "L’Officière Minerve avait raison ! On a bien fait de vous surveiller, au cas où vous tenteriez quelque chose !"

        show side leily defiante onlayer overlay:
            pos (0,715)
        l "Vous m’en direz tant…"

        hide leily
        hide romuald

        jump plan015

#Sequence009

    label plan015:

        scene bg poste securite
        with fade

        play music "audio/poste_securite.WAV" fadeout 1

        "Les Gardiens m’amènent au poste de sécurité et me menottent à une chaise en fer. Et évidemment ils me dépossèdent de l'Écosphère !"

        show side leily soupir onlayer overlay:
            pos (0,715)
        "Ils préviennent ensuite leur officière, qui vient à ma rencontre avec une humeur des plus… Massacrante !"

        show minerve colerique at center
        with moveinleft

        show side leily neutre onlayer overlay:
            pos (0,715)
        m "Encore vous !?"

        show side leily confiante onlayer overlay:
            pos (0,715)
        l "Ravie de vous revoir, moi aussi !"

        show side leily neutre onlayer overlay:
            pos (0,715)

        m "Je vais ajouter ces éléments à charge dans votre dossier, vous allez passer un sale quart d'heure quand les autorités vont venir vous chercher."

        show side leily neutre onlayer overlay:
            pos (0,715)

        m "Vous allez vous tenir vous tenir tranquille jusque là, je vous le garantis !"

        show side leily defiante onlayer overlay:
            pos (0,715)
        l "Mais évidemment !"

        hide minerve
        with moveoutleft

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Elle sort du bureau pour retourner prêter main forte à ses collègues, un Gardien va venir prendre la relève après avoir fait sa ronde."

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Pas une seconde à perdre ! Je saisis mon petit outil caché dans ma chevelure."

        play sound "audio/crochetage.WAV"

        show leily neutre at center
        with moveinbottom

        "Le temps de crocheter les menottes, me voilà de nouveau libre."
        "Je quitte discrètement le poste de sécurité par la fenêtre. Une chance qu’il n’y ait pas d’étages !"

        hide leily
        with moveoutright

        "En revanche, dès que le Garde découvrira mon «absence» il sonnera l’alerte."
        "Je dois faire vite !"

        jump plan016

#Sequence010

    label plan016:

        scene bg rdc memorial
        with pixellate

        play music "audio/rdc_memorial.WAV" fadeout 1

        show piedestal ecosphere with ease:
            pos (400,475)

        show leily neutre at center
        with moveinleft

        "Bon, me voilà à nouveau à l’intérieur ! Je balaye du regard la salle pour m’assurer qu’aucun Gardien n’est dans le périmètre..."
        "Et visiblement, non ! Ils ont dût relacher la surveillance, me croyant enfermée !"
        "Cette fois, pas le droit à l’erreur... J’appelle le Commanditaire."

        jump plan017

    label plan017:

        show leily neutre at center

        "J’active le dispositif logé dans mon oreille."

        play sound "audio/radio.WAV"

        cm "Ça y est, vous êtes sur place ?"

        "C’est le commanditaire qui m’a embauché pour dérober l'Écosphère, je ne connais pas son identité."
        "Je parle à voix basse et je m’éloigne des visiteurs pour éviter d’attirer l’attention."

        show leily confiante at center
        with dissolve

        l "Je suppose que dans votre jargon, ça veut dire Bonjour !"

        show leily neutre at center
        with dissolve

        l "Mais pour votre gouverne, j’ai réussi à entrer."
        l "En revanche, quelque chose semble anormal : l'Écosphère a l'air intacte, c'est pourtant censé être une arme de guerre."

        show leily surprise at center
        with dissolve

        cm "Tout juste, le modèle exposé au public n'est qu'une réplique. Une pâle copie."
        cm "L'original se trouve dans un lieu tenu secret."

        show leily soupir at center
        with dissolve

        l "Cette information aurait été la bienvenue dès notre rencontre, vous ne trouvez pas ?"

        show leily contrarie at center
        with dissolve

        cm "Si j'avais été honnête dès le début, vous auriez refusé cette mission par manque d'enjeux..."
        cm "Mais pas de panique, vous n'êtes pas venu ici pour rien."
        l "Et quelle est la suite des festivités, au juste ?"
        cm "Vous allez retrouver un indice qui nous permettra de retrouver la trace du véritable Écosphère."

        show leily proteste at center
        with dissolve

        l "Effectivement, c'est beaucoup moins clinquant comme mission !"

        show leily contrarie at center
        with dissolve

        cm "Lorsque vous m'aurez remis l'orbe vous aurez la récompense que nous avons convenu."

        show leily soucieuse at center
        with dissolve

        "En retour, il a promis de m'aider à localiser et remettre à flot l'Ouragan d'Azur, le navire de mon défunt père qui a sombré durant mon enfance. Un navire de guerre en écailles de dragon."

        show leily neutre at center
        with dissolve

        "Il m'a aussi promis de l'argent. Beaucoup d'argent !"
        "De quoi financer toute une flotte, avec l'Ouragan d'Azur à sa tête, pour renverser l'actuel Roi des pirates... Et prendre sa place, bien-sûr !"

        show leily confiante at center
        with dissolve

        l "Vous avez un certain talent pour remonter le moral !"

        show leily neutre at center
        with dissolve

        cm "Disons que je suis plein de surprise."
        cm "Maintenant, vous allez emprunter les escaliers pour rejoindre le huitième étage et vous rendre dans la Biblitothèque."

        show leily amuse at center
        with dissolve

        l "Mais il va falloir que je passe au petit coin avant d’aller chercher votre fameux indice !"
        cm "Vous plaisantez, j'espère ?"

        hide leily
        with moveoutright

        hide piedestal ecosphere

#Sequence011

        scene bg toilettes
        with fade

        play music "audio/toilettes.WAV" volume 0.5

        show leily neutre with moveinleft:
            xalign 0.25
            yalign 1.0

        "En longeant un couloir exposant des armures mises au point par le Maître Ingénieur, j’arrive à un panneau qui m’indique la direction des toilettes."
        "Et j'entre par le côté dédié aux dames !"
        "Mais je ne suis pas ici pour faire ce que l’on fait d'habitude dans ce genre d’endroit…"
        "Ce que je cherche est dissimulé dans le réservoir d’eau de la cuvette."

        cm "Vous avez terminé ?"
        l "Patience... Je suis simplement venu chercher mon talisman, le Neptune."

        show neptune with zoomin:
            xalign 0.65
            yalign 0.25

        play sound "audio/neptune.WAV"

        l "Mon petit doigt me dit que je vais en avoir besoin."
        "Les talismans sont des armes qui permettent de canaliser et amplifier les Affinités."

        cm "Vous avez pu contourner l’interdiction du port d’armes… Astucieux !"

        l "Rien de bien compliqué, j’ai soudoyé un agent d’entretien hier pour qu’il cache mon talisman ici."

        hide neptune with zoomout

        l "Maintenant direction le huitième étage !"

        hide toilettes
        hide leily

#Sequence012

        scene bibliotheque
        with fade

        play music "audio/bibliotheque.WAV" fadeout 1

        show leily neutre with moveinleft:
            xalign 0.55
            yalign 1.0

        "Me voici au huitième étage, qui abrite l’ensemble des livres ayant appartenu au Maître-Ingénieur ainsi qu’une vitrine contenant des effets personnels."

        show leily confiante with dissolve:
            xalign 0.55
            yalign 1.0

        l "Quelle joie d’avoir fait tout ce chemin pour bouquiner et admirer quelques babioles !"

        show leily neutre with dissolve:
            xalign 0.55
            yalign 1.0

        cm "Au lieu de vous plaindre, décrivez-moi plutôt ce qui se trouve dans la vitrine au fond de la salle."

        show leily contrarie with dissolve:
            xalign 0.55
            yalign 1.0


        "Je n’aime pas du tout ce ton directif… Mais on va faire avec si je veux empocher ma récompense !"
        l "J’aperçois une paire de lunettes à soudure, une photo de famille et, oh …"

        show leily surprise with dissolve:
            xalign 0.55
            yalign 1.0

        show montre gousset with zoomin:
            xalign 0.20
            yalign 0.25

        play sound "audio/montre_gousset.WAV"

        l "Une montre à gousset, le couvercle est serti d’une moitié de perle rouge."
        cm "Parfait !"
        cm "Saviez-vous que Conrad Kross avait une fille ?"

        show leily triste with dissolve:
            xalign 0.55
            yalign 1.0

        l "Oui, je vois d’ailleurs une photo de famille dans la vitrine."
        cm "Elle doit avoir à peu près le même âge que vous, aujourd’hui."

        show leily moqueuse with dissolve:
            xalign 0.55
            yalign 1.0

        l "C’est formidable ! Mais je ne vois pas le rapport avec la mission..."
        cm "Selon mes sources, la fille détient l’autre moitié de la perle."

        show leily soucieuse with dissolve:
            xalign 0.55
            yalign 1.0

        cm "Un souvenir que lui a confié son père autrefois."
        cm "Les deux parties rassemblées indiquent l’endroit où est caché le véritable Écosphère, l'atelier secret de Conrad Kross : le Laboratoire englouti."

        l "Je comprends mieux votre intérêt de retrouver l’héritière…"
        l "Mais je doute qu’elle accepte de me remettre un souvenir de son père sans sourciller."

        show leily surprise with dissolve:
            xalign 0.55
            yalign 1.0

        cm "Et j’oubliais, il faudra aussi enlever la fille."
        cm "Le code génétique de Conrad Kross est indispensable pour déverrouiller l'accès au Laboratoire."
        cm "Sa fille en est l’unique dépositaire."

        show leily proteste with dissolve:
            xalign 0.55
            yalign 1.0

        l "De mieux en mieux… Et comment dois-je m’y prendre pour la retrouver, au juste ?"

        show leily soucieuse with dissolve:
            xalign 0.55
            yalign 1.0

        cm "C’est justement pour ça que Conrad lui a remis la moitié de la perle, pour s’assurer qu’elle était en sécurité quand la guerre face au Programme Jénius a éclaté."
        cm "Portez le fragment à votre regard, vous verrez au travers une lueur à l’horizon."
        cm "C’est la signature thermique de l’autre partie, menant ainsi vers l'endroit où elle se trouve."

        show leily confiante with dissolve:
            xalign 0.55
            yalign 1.0

        l "Merveilleux !"

        show leily neutre with dissolve:
            xalign 0.55
            yalign 1.0

        l "De mon côté, je pense pouvoir localiser les coordonnées sur une carte nautique."
        l "Il reste que je dois mettre la main sur cette montre…"

        cm "C’est pourquoi je vous ai fait venir ici, en espérant que vos talents surpassent votre insolence."

        show leily nargue with dissolve:
            xalign 0.55
            yalign 1.0

        l "Je vais prendre cela pour un compliment !"

        show leily neutre with dissolve:
            xalign 0.55
            yalign 1.0

        cm "Je vous recontacterai pour vous indiquer notre point de rencontre."
        cm "Vous devrez m’y rejoindre avec l’Écosphère et l'héritière."
        cm "En échange, vous aurez la récompense convenue."

        play sound "audio/radio.WAV"
        "Le commanditaire a raccroché."

        show leily soupir with dissolve:
            xalign 0.55
            yalign 1.0

        "Quelle plaie ! Je n'avais rien prévu de tel dans mon plan initial… Il était question de dérober l’Écosphère en bas."

        show leily confiante with dissolve:
            xalign 0.55
            yalign 1.0

        "Tant pis, il ne me reste plus qu’à improviser !"

        show leily neutre with dissolve:
            xalign 0.55
            yalign 1.0

        show neptune with zoomin:
            xalign 0.20
            yalign 0.65

        play sound "audio/neptune.WAV"

        "Je dégaine mon arme, le Neptune, et le pointe droit sur la vitrine."
        "Mon Affinité d’Air se met à scintiller."
        "Et une bourrasque jaillit du canon pour faire voler en éclat la vitrine."

        play sound "audio/element_air.WAV"
        with vpunch

        "Je m’empare immédiatement de la montre à gousset."

        hide montre gousset
        hide neptune
        hide leily
        with pixellate

        jump plan018

    label plan018:

        play music "audio/combat.WAV"

        show side leily surprise onlayer overlay:
            pos (0,715)
        "Mais à peine ce fut le cas que l’alarme retentit aussitôt."

        show side leily surprise onlayer overlay:
            pos (0,715)

        g "Ça vient de la Bibliothèque !"

        show gardien 3 at right
        with moveinright

        show romuald at center with moveinleft
        show jack at left with moveinleft

        show side leily surprise onlayer overlay:
            pos (0,715)

        g "Mais vous êtes la pirate de tout à l'heure !"

        show side leily surprise onlayer overlay:
            pos (0,715)

        g "C'est fini pour vous !"

        show side leily confiante onlayer overlay:
            pos (0,715)
        l "Hum ! Les hostilités ne se sont pas faites attendre !"

        $ timeout_label = "plan019"

        menu:

            "Riposter de front":
                jump plan019

            "Fuir avec la montre à gousset":
                jump plan022



    label plan019:

        "Le Gardien à ma droite fait scintiller son Affinité et bande son arc dans ma direction."

        play sound "audio/element_feu.WAV"

        with vpunch

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Il décoche une flèche de feu."

        show side leily defiante onlayer overlay:
            pos (0,715)
        "Je l'esquive sans peine."

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Et je tire aussitôt une salve d’air dans sa direction avec le Neptune, le garde se prend la bourrasque de plein fouet."

        play sound "audio/element_air.WAV"
        with hpunch

        hide gardien 3
        with moveoutbottom

        show side leily contrarie onlayer overlay:
            pos (0,715)
        "Mais je n'ai pas le temps de crier victoire : les deux autres Gardiens sont prêts à en découdre."

        show side leily contrarie onlayer overlay:
            pos (0,715)
        g "Restez où vous êtes !"

        show side leily colere onlayer overlay:
            pos (0,715)
        "Je dois adopter la meilleure stratégie !"

        $ timeout_label = "plan020"

        menu:

            "Se retrancher derrière une rangée de livres":
                jump plan020

            "Tenter une percée":
                jump plan022


    label plan020:

        "Je me précipite derrière l’une des étagères, ils stoppent immédiatement leur assaut."

        show side leily soupir onlayer overlay:
            pos (0,715)
        "Une guerre de position s’annonce… Ils n’osent pas attaquer, de peur d’endommager la collection d’ouvrages."

        show side leily contrarie onlayer overlay:
            pos (0,715)
        "Je dois trouver un moyen de rejoindre le sommet du Mémorial et..."

        play sound "audio/pas_de_course.WAV"
        queue sound "audio/charge.WAV"
        queue sound "audio/celerite.WAV"

        stop music

        show side leily surprise onlayer overlay:
            pos (0,715)
        "Ça ne me dit rien qui vaille..."

        show side leily contrarie onlayer overlay:
            pos (0,715)
        "Je jette un regard à l'extrêmité d'une étagère."

        show romuald at right

        show jack at left

        show minerve colerique:
            xalign 0.65
            yalign 1.0

        show gardien 1 dubitatif:
            xalign 0.30
            yalign 1.0

        with pixellate
        play sound "audio/rassemblement.WAV"

        show side leily contrarie onlayer overlay:
            pos (0,715)
        "Mauvaise surprise… D’autres renforts."

        show side leily contrarie onlayer overlay:
            pos (0,715)
        m "Vous n'avez aucune issue, pirate !"

        show side leily soupir onlayer overlay:
            pos (0,715)
        "Trop nombreux... Je ferais mieux de me rendre."

        hide minerve
        hide gardien 1
        hide romuald
        hide jack

        jump plan021

#Sequence013

    label plan021:

        scene bg sommet memorial
        with fade

        play music "audio/sommet_memorial.WAV" fadeout 1

        show minerve:
            xalign 0.25
            yalign 1.0

        show gardien 1:
            xalign 0.75
            yalign 1.0

        with dissolve

        "Les Gardiens m’ont passé les menottes et m’escortent vers le poste de sécurité."

        show side leily contrarie onlayer overlay:
            pos (0,715)
        "Nous passons par le toit du Mémorial, ils tiennent à éviter que les visiteurs assistent au remue-ménage."

        show side leily desolee onlayer overlay:
            pos (0,715)
        "L’officière Minerve tient dans sa main droite la montre à gousset que j’avais dérobé."

        show side leily amuse onlayer overlay:
            pos (0,715)
        "Mais l'après-midi touche à sa fin. Tout n'est pas perdu..."

        show side leily confiante onlayer overlay:
            pos (0,715)
        l "Dîtes, quelqu’un aurait l’heure ?"

        show minerve irritee:
            xalign 0.25
            yalign 1.0

        show side leily neutre onlayer overlay:
            pos (0,715)

        m "Là où l'on vous enmène, vous n’aurez pas besoin de le savoir."

        show side leily defiante onlayer overlay:
            pos (0,715)
        l "J’insiste."

        show minerve menace:
            xalign 0.25
            yalign 1.0

        show gardien 1 dubitatif:
            xalign 0.75
            yalign 1.0

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Exaspérée, elle fait signe à son collaborateur de répondre."

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Pendant ce temps, je crochète discrètement mes menottes en dissimulant mes mains derrière ma longue chevelure d’ébène."

        play sound "audio/crochetage.WAV"

        show gardien 1:
            xalign 0.75
            yalign 1.0

        show side leily neutre onlayer overlay:
            pos (0,715)

        g "Dix-sept heure pile."

        show minerve hautaine:
            xalign 0.25
            yalign 1.0

        show side leily neutre onlayer overlay:
            pos (0,715)

        m "Voilà, vous êtes contente ?"

        show side leily confiante onlayer overlay:
            pos (0,715)
        l "On ne peut mieux !"

        show minerve surprise:
            xalign 0.25
            yalign 1.0

        show gardien 1 surprise:
            xalign 0.75
            yalign 1.0

        show side leily amuse onlayer overlay:
            pos (0,715)
        "Soudain, un bruit strident se fait entendre. Une salve de boulets de canon se fracasse contre les murs du Mémorial."

        play music "audio/combat_final.WAV"

        with vpunch
        play sound "audio/boulet_canon.WAV"

        show side leily amuse onlayer overlay:
            pos (0,715)
        "C’est mon fidèle équipage !"

        show side leily amuse onlayer overlay:
            pos (0,715)
        "Mes hommes étaient chargés de faire feu avec mon navire, la Rose noire, dix-sept heure précise pour créer une diversion."

        show side leily defiante onlayer overlay:
            pos (0,715)
        "J’avais prévu dans mon plan que j'aurais quelques difficultés avec la sécurité du Mémorial dès que j’aurais voler la montre, ou plutôt l’Écosphère à la base !"

        show side leily colere onlayer overlay:
            pos (0,715)
        "Et justement, je profite de cette occasion pour me précipiter sur Minerve. Elle est abasourdie par l’attaque et je lui prends des mains la montre à gousset."

        with hpunch
        play sound "audio/montre_gousset.WAV"

        show minerve colerique:
            xalign 0.25
            yalign 1.0

        show gardien 1 avertissement:
            xalign 0.75
            yalign 1.0

        show side leily colere onlayer overlay:
            pos (0,715)
        m "Arrêtez-là !"

        "Trop tard ! Je saute dans le vide depuis le sommet du Mémorial."
        "Mes assaillants s’approchent immédiatement pour regarder en contrebas."

        play sound "audio/reptile.WAV"

        "Un pirate, chevauchant un reptile volant, m’a rattrapé en plein vol et fonce à vive allure vers la Rose noire, au large."
        "Les Gardiens sont furieux, je ne peux m’empêcher de leur adresser un dernier sourire !"

        hide minerve
        hide gardien 1

        jump plan023

#Sequence014

    label plan022:

        scene bg bibliotheque

        show romuald at center
        show jack at left

        play sound "audio/coup_de_poing.WAV"
        with vpunch

        "Je repousse l'un des Gardiens et j’emprunte à vive allure l’escalier menant au sommet du Mémorial."

        show side leily colere onlayer overlay:
            pos (0,715)
        "Des visiteurs se trouvent sur mon passage, ils assistent à la scène éberlués."

        show side leily soucieuse onlayer overlay:
            pos (0,715)
        "Les Gardiens à mes trousses s’engagent également vers le sommet."

        scene bg sommet memorial
        with fade

        stop music fadeout 1

        "J’ai maintenant une bonne longueur d’avance sur mes assaillants !"

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Il ne me reste plus qu'à attendre le signal et..."

        play sound "audio/rassemblement.WAV"

        show side leily surprise onlayer overlay:
            pos (0,715)
        "À moins que je n’ai parlé trop vite .. ?"

        show minerve with moveinright:
            xalign 0.65
            yalign 1.0

        show gardien 1 dubitatif with moveinleft:
            xalign 0.30
            yalign 1.0

        show side leily surprise onlayer overlay:
            pos (0,715)
        "L’officière que j’avais croiser à l’entrée m’attends de l’autre côté de la passerelle."

        show minerve hautaine:
            xalign 0.65
            yalign 1.0

        show side leily contrarie onlayer overlay:
            pos (0,715)
        m "Où allez-vous comme ça ?"

        show side leily colere onlayer overlay:
            pos (0,715)
        "Et voilà ceux qui étaient à ma poursuite ! Je me retrouve encerclée..."

        play music "audio/combat_final.WAV" fadeout 1

        show jack at left with moveinleft
        show romuald at right with moveinright

        show minerve satisfaite with dissolve:
            xalign 0.65
            yalign 1.0

        show side leily soucieuse onlayer overlay:
            pos (0,715)

        m "Vous n'irez pas plus loin, pirate !"

        show side leily confiante onlayer overlay:
            pos (0,715)
        l "Permettez-moi d’en douter !"

        show side leily neutre onlayer overlay:
            pos (0,715)
        "J’ouvre la montre à gousset. Incroyable, cette babiole fonctionne encore ! Dix-sept heure précise."

        show side leily amuse onlayer overlay:
            pos (0,715)
        "Ils vont intervenir d’un moment à l’autre."

        show minerve satisfaite:
            xalign 0.65
            yalign 1.0

        show side leily amuse onlayer overlay:
            pos (0,715)

        m "Je n'aime pas l'air qu'elle prend. Elle prépare quelque chose, c'est sûr..."

        show minerve menace:
            xalign 0.65
            yalign 1.0

        with vpunch
        play sound "audio/boulet_canon.WAV"

        show minerve colerique:
            xalign 0.65
            yalign 1.0

        show gardien 1 surprise:
            xalign 0.30
            yalign 1.0

        with dissolve

        show side leily neutre onlayer overlay:
            pos (0,715)
        "Soudain, un bruit strident se fait entendre. Une salve de boulets de canon se fracasse contre les murs du Mémorial."

        show side leily amuse onlayer overlay:
            pos (0,715)
        "C’est mon équipage ! Mes hommes étaient chargés de faire feu avec mon navire, la Rose noire, dix-sept heure précise pour créer une diversion."

        show side leily defiante onlayer overlay:
            pos (0,715)
        "J’avais prévu dans mon plan que j'aurais quelques difficultés avec la sécurité du Mémorial dès que j’aurais voler la montre, ou plutôt l’Écosphère à la base !"

        show minerve colerique:
            xalign 0.65
            yalign 1.0

        show gardien 1 avertissement:
            xalign 0.30
            yalign 1.0

        show side leily neutre onlayer overlay:
            pos (0,715)
        m "Arrêtez-là !"

        with hpunch

        "Trop tard ! Je saute dans le vide depuis le sommet du Mémorial."
        "Mes assaillants s’approchent immédiatement pour regarder en contrebas."

        play sound "audio/reptile.WAV"

        "Un pirate, chevauchant un reptile volant, m’a rattrapé en plein vol et fonce à vive allure vers la Rose noire, au large."
        "Les Gardiens sont furieux, je ne peux m’empêcher de leur adresser un dernier sourire !"

        hide minerve
        hide gardien 1
        hide jack
        hide romuald

        jump plan023

#Sequence015

    label plan023:

        scene bg la rose noire
        with fade

        play music "audio/la_rose_noire.MP3" fadeout 1

        show leily neutre at center
        with ease

        "Je bondis du reptile volant, il m'a ramené à bord de mon bien aimé navire : la Rose noire."
        "Mon équipage dans son entier m’accueille chaleureusement."

        p "Alors Capitaine, notre commanditaire disait vrai ?"

        show leily soupir at center
        with dissolve

        l "Plus ou moins… Léger changement de programme."

        show leily neutre at center
        with dissolve

        "Je saisis la montre à gousset."

        show montre gousset with zoomin:
            xalign 0.20
            yalign 0.25

        "Puis j'en retire le fragment de perle logé sur le couvercle..."

        play sound "audio/fragment_perle.WAV"

        show fragment perle with moveintop:
            xalign 0.20
            yalign 0.25

        hide montre gousset
        with moveoutbottom

        "Afin de le présenter fièrement à l’équipage !"

        show leily amuse at center
        with dissolve

        l "Avec ceci nous allons retrouver la fille du Maître Ingénieur."

        hide leily
        hide fragment perle
        with dissolve

        scene bg generique
        with wiperight
        play sound "audio/generique.WAV" volume 0.5

        show text "{size=+25}{b}{color=000}Crée et écrit par Riocamy." with Pause(3.10)
        show text "{size=+25}{b}{color=000}Character design : VisuStella (Stella Character Generator)." with Pause(3.10)
        show text "{size=+25}{b}{color=000}Backrounds : Space Gecko Studio; Lakay; Rachel Chen." with Pause(3.10)
        show text "{size=+25}{b}{color=000}Musiques et Sound design : Cafofo Music." with Pause(3.10)
        show text "{size=+25}{b}{color=000}Merci d'avoir joué !" with Pause(3.10)


return
