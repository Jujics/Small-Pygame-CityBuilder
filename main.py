import time

import pygame
import random
import sys
from pygame.locals import *
from random import choice
from math import sqrt


def test_routeV(lig,col):
    # cette fonction teste si on peut poser une route verticale
    # à droite (col+1) et à gauche (col-1) : on ne peut pas avoir de route horizontale ( indice 2), de route sud-est (indice 3), de route sud-ouest (indice 4), de route nord-est (indice 5), de route nord-ouest (indice 6)
    # en haut (lig-1) : on ne peut avoir de route horizontale (indice 2), de route sud-est (indice 3), de route sud-ouest (indice 4)
    # en bas (lig+1) : on ne peut avoir de route horizontale (indice 2), de route nord-est (indice 5), de route nord-ouest (indice 6)
    if (tiles[lig][col+1].typ!=namelist[2] and tiles[lig][col+1].typ!=namelist[3] and tiles[lig][col+1].typ!=namelist[4] and tiles[lig][col+1].typ!=namelist[5]  and tiles[lig][col+1].typ!=namelist[6]):
        if (tiles[lig][col-1].typ != namelist[2] and tiles[lig][col-1].typ!=namelist[3] and tiles[lig][col-1].typ!=namelist[4] and tiles[lig][col-1].typ != namelist[5] and tiles[lig][col-1].typ != namelist[6]):
            if (tiles[lig-1][col].typ != namelist[2] and tiles[lig-1][col].typ != namelist[3] and tiles[lig-1][col].typ != namelist[4]):
                if (tiles[lig+1][col].typ != namelist[2] and tiles[lig+1][col].typ != namelist[5] and tiles[lig+1][col].typ != namelist[6]):
                    return True # on retourne 'vrai' si on peut poser la tile "route verticale"
    return False # sinon on retourne 'faux'

def test_routeH(lig,col):
    # cette fonction teste si on peut poser une route horizontale
    # à droite (col+1) : on ne peut pas avoir de route verticale (indice 1), de route sud-est (indice 3), de route nord-est (indice 5)
    # à gauche (col-1) : on ne peut pas avoir de route verticale (indice 1), de route sud-ouest (indice 4), de route nord-ouest (indice 6)
    # en haut (lig-1) et en bas (lig+1) : on ne peut pas avoir de route horizontale (indice 1), de route sud-est (indice 3), de route sud-ouest (indice 4), de route nord-est (indice 5), de route nord-ouest (indice 6)
    if (tiles[lig][col+1].typ!=namelist[1] and tiles[lig][col+1].typ!=namelist[3] and tiles[lig][col+1].typ!=namelist[5]):
        if (tiles[lig][col-1].typ != namelist[1] and tiles[lig][col-1].typ!=namelist[4] and tiles[lig][col-1].typ!=namelist[6]):
            if (tiles[lig-1][col].typ != namelist[1] and tiles[lig-1][col].typ != namelist[3] and tiles[lig-1][col].typ != namelist[4] and tiles[lig-1][col].typ != namelist[5] and tiles[lig-1][col].typ != namelist[6] ):
                if (tiles[lig+1][col].typ != namelist[1] and tiles[lig+1][col].typ != namelist[3] and tiles[lig+1][col].typ != namelist[4] and tiles[lig+1][col].typ != namelist[5] and tiles[lig+1][col].typ != namelist[6]):
                    return True # on retourne 'vrai' si on peut poser la tile "route horizontale"
    return False # sinon on retourne 'faux'

def test_routeSE(lig,col):
    # cette fonction teste si on peut poser une route sud-est
    # à droite (col+1) : on ne peut pas avoir de route verticale (indice 1), de route sud-est (indice 3), de route nord-est (indice 5)
    # à gauche (col-1) : on ne peut pas avoir de route horizontale (indice 2), de route sud-est (indice 3), de route nord-est (indice 5)
    # en haut (lig-1) : on ne peut avoir de route horizontale (indice 2), de route sud-est (indice 3), de route sud-ouest (indice 4)
    # en bas (lig+1) : on ne peut avoir de route verticale (indice 1), de route sud-est (indice 3), de route sud-ouest (indice 4)
    if (tiles[lig][col+1].typ!=namelist[1] and tiles[lig][col+1].typ!=namelist[3] and tiles[lig][col+1].typ!=namelist[5]):
        if (tiles[lig][col-1].typ != namelist[2] and tiles[lig][col-1].typ!=namelist[3] and tiles[lig][col-1].typ!=namelist[5]):
            if (tiles[lig-1][col].typ != namelist[2] and tiles[lig-1][col].typ != namelist[3] and tiles[lig-1][col].typ != namelist[4]):
                if (tiles[lig+1][col].typ != namelist[1] and tiles[lig+1][col].typ != namelist[3] and tiles[lig+1][col].typ != namelist[4]):
                    return True # on retourne 'vrai' si on peut poser la tile "route sud-est"
    return False # sinon on retourne 'faux'

def test_routeSO(lig,col):
    # cette fonction teste si on peut poser une route sud-ouest
    # à droite (col+1) : on ne peut pas avoir de route horizontale (indice 2), de route sud-ouest (indice 4), de route nord-ouest (indice 6)
    # à gauche (col-1) : on ne peut pas avoir de route verticale (indice 1), de route sud-ouest (indice 4), de route nord-ouest (indice 6)
    # en haut (lig-1) : on ne peut avoir de route horizontale (indice 2), de route sud-est (indice 3), de route sud-ouest (indice 4)
    # en bas (lig+1) : on ne peut avoir de route verticale (indice 1), de route sud-est (indice 3), de route sud-ouest (indice 4)
    if (tiles[lig][col+1].typ!=namelist[2] and tiles[lig][col+1].typ!=namelist[6] and tiles[lig][col+1].typ!=namelist[4]):
        if (tiles[lig][col-1].typ != namelist[1] and tiles[lig][col-1].typ!=namelist[4] and tiles[lig][col-1].typ!=namelist[6]):
            if (tiles[lig-1][col].typ != namelist[2] and tiles[lig-1][col].typ != namelist[3] and tiles[lig-1][col].typ != namelist[4]):
                if (tiles[lig+1][col].typ != namelist[1] and tiles[lig+1][col].typ != namelist[3] and tiles[lig+1][col].typ != namelist[4]):
                    return True # on retourne 'vrai' si on peut poser la tile "route sud-ouest"
    return False # sinon on retourne 'faux'

def test_routeNE(lig,col):
    # cette fonction teste si on peut poser une route nord-est
    # à droite (col+1) : on ne peut pas avoir de route verticale (indice 1), de route sud-est (indice 3), de route nord-est (indice 5)
    # à gauche (col-1) : on ne peut pas avoir de route horizontale (indice 2), de route sud-est (indice 3), de route nord-est (indice 5)
    # en haut (lig-1) : on ne peut avoir de route verticale (indice 1), de route nord-est (indice 5), de route nord-ouest (indice 6)
    # en bas (lig+1) : on ne peut avoir de route horizontale (indice 2), de route nord-est (indice 5), de route nord-ouest (indice 6)
    if (tiles[lig][col+1].typ!=namelist[1] and tiles[lig][col+1].typ!=namelist[3] and tiles[lig][col+1].typ!=namelist[5]):
        if (tiles[lig][col-1].typ != namelist[2] and tiles[lig][col-1].typ!=namelist[3] and tiles[lig][col-1].typ!=namelist[5]):
            if (tiles[lig-1][col].typ != namelist[1] and tiles[lig-1][col].typ != namelist[6] and tiles[lig-1][col].typ != namelist[5]):
                if (tiles[lig+1][col].typ != namelist[2] and tiles[lig+1][col].typ != namelist[6] and tiles[lig+1][col].typ != namelist[5]):
                    return True # on retourne 'vrai' si on peut poser la tile "route nord-est"
    return False # sinon on retourne 'faux'

def test_routeNO(lig,col):
    # cette fonction teste si on peut poser une route nord-ouest
    # à droite (col+1) : on ne peut pas avoir de route horizontale (indice 2), de route sud-ouest (indice 4), de route nord-ouest (indice 6)
    # à gauche (col-1) : on ne peut pas avoir de route verticale (indice 1), de route sud-ouest (indice 4), de route nord-ouest (indice 6)
    # en haut (lig-1) : on ne peut avoir de route verticale (indice 1), de route nord-est (indice 5), de route nord-ouest (indice 6)
    # en bas (lig+1) : on ne peut avoir de route horizontale (indice 2), de route nord-est (indice 5), de route nord-ouest (indice 6)
    if (tiles[lig][col+1].typ!=namelist[2] and tiles[lig][col+1].typ!=namelist[4] and tiles[lig][col+1].typ!=namelist[6]):
        if (tiles[lig][col-1].typ != namelist[1] and tiles[lig][col-1].typ!=namelist[4] and tiles[lig][col-1].typ!=namelist[6]):
            if (tiles[lig-1][col].typ != namelist[1] and tiles[lig-1][col].typ != namelist[5] and tiles[lig-1][col].typ != namelist[6]):
                if (tiles[lig+1][col].typ != namelist[2] and tiles[lig+1][col].typ != namelist[6] and tiles[lig+1][col].typ != namelist[5]):
                    return True # on retourne 'vrai' si on peut poser la tile "route nord-ouest"
    return False # sinon on retourne 'faux'

def demandenom(): # cette fonction demande son nom à l'utilisateur
    screen.fill((0,0,0))                    # on remplit l'écran de noir pour l'effacer
    pygame.mixer.init()                     # on initialise la musique
    pygame.mixer.music.load("Undertale.wav")    # on charge le morceau
    pygame.mixer.music.play(-1)             # on lance le morceau de musique en boucle (-1)

    font = pygame.font.SysFont('tahoma', 24)    # on utilise la font système 'Tahoma' en 25 points

    rectScreen = screen.get_rect()  # on crée un rectangle de la taille de l'écran
    titre = font.render("Merci d'entrer votre nom :", 1, (0, 0, 0)) # on crée un texte lissé (1=antialiasing)en noir (0,0,0)
    titre_rect = titre.get_rect() # on crée un rectangle de la taille du texte
    titre_rect.x=int(640/2)-int(titre_rect.width/2) # on met sa position en x pour le centrer
    titre_rect.y=int(480/2)-50  # on place sa position en y à la moitié de l'écran moins 50 pixels

    # on crée un rectangle au centre autour de la zone de saisie
    contour_inputbox=pygame.Rect(int(rectScreen.width/2)-100, int(rectScreen.height/2)-22, 200, 32)
    # on crée un rectangle au centre pour la zone de saisie
    input_box = pygame.Rect(int(rectScreen.width/2)-100, int(rectScreen.height/2)-22, 200, 32)
    # quand la zone sera inactive, on la coloriera en gris foncé
    color_inactive = pygame.Color('darkgrey')
    # quand la zone sera active, on la coloriera en noir
    color_active = pygame.Color('black')
    # au départ la couleur de la zone sera la couleur inactive
    color = color_inactive
    # la zone est inactive
    active = False
    # texte saisi vide
    text = ''
    # on n'a pas terminé
    done = False

    while not done: # tant qu'on n'a pas terminé
        for event in pygame.event.get(): # boucle des évènements
            if event.type == pygame.QUIT:   # si on clique sur la croix rouge de la fenêtre
                sys.exit() # on a terminé
            if event.type == pygame.MOUSEBUTTONDOWN:    # si un bouton de la souris est pressé.
                if input_box.collidepoint(event.pos): # si on clique dans le champ de saisie
                    active = True # on passe en mode 'active'
                else:
                    active = False # sinon on passe en mode 'inactive'
                # on met dans la couleur à utiliser color_active si active==vrai sinon on y met color_inactive
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:    # si on appuie sur une touche du clavier
                if active:  # si la zone de texte est activée
                    if event.key == pygame.K_RETURN:    # si on appuie sur la touche 'entrée'
                        pygame.mixer.music.stop()   # on arrête la musique
                        font = pygame.font.SysFont('freesansbold.ttf', 12)    #on rétablit la font en 20 points
                        return(text) # on retourne le texte saisi
                    elif event.key == pygame.K_BACKSPACE:# si on appuie sur la touche 'backspace'
                        text = text[:-1]    # on retire le dernier caractère de 'text'
                    else:
                        # sinon on ajoute à 'text' chaque caractère tapé qui n'est ni la touche 'entrée' ni la touche 'backspace'
                        text += event.unicode

        #screen.fill((30, 30, 30))
        bg = pygame.image.load("questions.jpg") # on charge l'image de fond
        screen.blit(bg, (0, 0)) # on l'affiche aux coordonnées (0,0)
        screen.blit(titre, titre_rect) # on affiche 'titre' aux coordonnées de 'titre_rect'

        # on crée une surface où s'affichera le texte saisi (antialiasé et noir)
        txt_surface = font.render(text,1,(0,0,0))
        # on calcule sa largeur
        width = max(200, txt_surface.get_width() + 10)
        # cela devient la largeur de la zone de saisie
        input_box.w = width
        # et celle du contour de la zone de saisie
        contour_inputbox.w=width

        # on dessine le rectangle plein (0) de la zone de saisie en blanc (255,255,255)
        pygame.draw.rect(screen, (255, 255, 255),input_box,0)
        # on dessine le rectangle de la zone de contour, avec 5 pixels de large et dans la couleur déterminée
        pygame.draw.rect(screen, color, contour_inputbox,5)

        # on met à jour la zone de saisie
        screen.blit(txt_surface, (input_box.x + 5, input_box.y))

        pygame.display.flip() # met à jour toute la fenêtre
        clock.tick(30)


def init_tiles():   # cette fonction réinitialise la liste 'tiles' avec des cases considérées comme vides
    for lig in range(0, 16):
        for col in range(0, 21):
            tiles[lig][col].typ="rien"

def remplissage():  # remplissage aléatoire de la carte
    k=0
    x=5
    y=10
    new = []    # initialisation de la liste new
    # ces deux vboucles vont créer et initialiser la liste 'tiles' à 2 dimensuions
    for lig in range(0, 16):    # 15 lignes
        for col in range(0, 21): # 20 colonnes  # oncrée 20 tiles dans la liste new
            new.append(Tile((0, 0), tilelist[0], 'rien'))  # on crée une nouvelle tile dans la liste qui aura comme type 'rien' (considérée comme vide)
        tiles.append(new) # on ajoute la liste new à la liste tiles
        new = []    # on remet new à vide
    nb_ilots=random.randint(2,5)    # on tire un nombre d'ilots entre 2 et 5
    for i in range(nb_ilots):   # on va créer des ilots
        nb=random.randint(100,150)  # nombre de tiles par ilot entre 100 et 150
        # on divise le plan de jeu selon le nombre d'ilots (exemple : si 3 ilots : un entre ls tiles 0 à 6, un entre les tiles 6 à 13 et un entre les tiles 14 à 20)
        numx = random.randint(int(i*(20/nb_ilots)), int(i*(20/nb_ilots)+(20/nb_ilots))) # tirage aléatoire de la coordonnée en x du centre de l'ilot
        numy = random.randint(int(i*(15/nb_ilots)), int(i*(15/nb_ilots)+(15/nb_ilots))) # tirage aléatoire de la coordonnée en y du centre de l'ilot

        for j in range(nb): # on va créer les 'nb' tiles
            while True: # boucle pour s'assurer que le x tiré aléatoirement soir bien entre les limites
                x=int(random.gauss(numx,3)) # on tire aléatoirement selon une répartition de gauss par rapport à 'numx' la coordonnée en x
                if (x>=0 and x<=19):    # si la valeur de x est dans les bornes
                    break               # on sort de la boucle while
            while True: # boucle pour s'assurer que le y tiré aléatoirement soir bien entre les limites
                y = int(random.gauss(numy,3)) # on tire aléatoirement selon une répartition de gauss par rapport à 'numy' la coordonnée en y
                if (y>=3 and y<=15):    # si la valeur de x est dans les bornes
                    break               # on sort de la boucle while

            if (tiles[y][x].typ=='rien'):   # s'il n'y a pas déjà une tile
                tiles[y][x] = Tile((x*32, y*32), tilelist[0], 'Grass')   # on ajoute une tile de type 'Grass'

def boutons_choix():    # gère le choix pour le terrain de jeu
    font = pygame.font.SysFont('tahoma', 25)    # on utilise la font système Tahoma en 25 points
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 640, 96), 0) # on trace le cartouche noir en haut de la fenêtre
    titre=font.render('Souhaitez-vous conserver ce terrain ?', 1, (255, 255, 255))   # le texte de la quesiton à afficher en blanc (255,255,255) antialiasé (1)
    ok = font.render('OK', 1, (255, 255, 255)) # le texte du bouton 'OK' en blanc (255,255,255) antialiasé (1)
    no = font.render('NON', 1, (255, 255, 255)) # le texte du bouton 'NON' en blanc (255,255,255) antialiasé (1)
    titre_rect=titre.get_rect() # on crée un rectangle pour la question
    rectScreen = screen.get_rect()  # on récupère le rectangle de la fenêtre entière
    titre_rect.center=rectScreen.center # on centre le rectangle de la question par rapport au centre de la fenêtre
    ok_rect=ok.get_rect() # on crée un rectangle pour le texte du bouton 'OK'
    ok_rect.center=(180,35) # on le centre en (180,35)
    no_rect = no.get_rect() # on crée un rectangle pour le texte du bouton 'NON'
    no_rect.center = (450, 35) # on le centre en (450,35)
    clic = False    # clic=faux tant qu'on n'a pas cliqué sur 'OK', vrai sinon
    # récupération des rectangles des textes des boutons
    bouton_oui = pygame.rect.Rect(130, 10, 100, 50)
    bouton_non = pygame.rect.Rect(400, 10, 100, 50)
    # dessin des rectangles vides (2) et au coins arrondis (3) des boutons
    pygame.draw.rect(screen, (255, 255, 255), bouton_oui, 2, 3)
    pygame.draw.rect(screen, (255, 255, 255), bouton_non, 2, 3)
    # dessin des boutons et de la question
    screen.blit(ok, ok_rect)
    screen.blit(no, no_rect)
    screen.blit(titre, (110,65,200,20))
    pygame.display.flip() # mise à jour de la fenêtre
    while not clic: # tant qu'on n'a pas cliqué sur 'OK'
        for e in pygame.event.get():    # gestion des évènements
            if e.type == QUIT:  # si on clique sur la croix rouge
                exit()          # on ferme le programme
            if e.type == MOUSEBUTTONDOWN:  # bouton enfoncé
                if e.button == 1:   # si c'est le bouton de gauche
                    if bouton_oui.collidepoint(e.pos):  # Si la position du curseur est dans le rectangle du bouton 'OK'
                        # petite animation du bouton 'OK' pressé
                        pygame.draw.rect(screen, (0, 0, 0), bouton_oui, 2,3)
                        pygame.draw.rect(screen, (255, 255, 255), (bouton_oui.x+1,bouton_oui.y+1,bouton_oui.width,bouton_oui.height), 2, 3)
                    if bouton_non.collidepoint(e.pos): # Si la position du curseur est dans le rectangle du bouton 'NON'
                        # petite animation du bouton 'NON' pressé
                        pygame.draw.rect(screen, (0, 0, 0), bouton_non, 2,3)
                        pygame.draw.rect(screen, (255, 255, 255), (bouton_non.x+1,bouton_non.y+1,bouton_non.width,bouton_non.height), 2, 3)
                    pygame.display.flip()
            if e.type == MOUSEBUTTONUP:  # bouton relâché
                if e.button == 1:   # si c'est le bouton de gauche
                    if bouton_oui.collidepoint(e.pos): # Si la position du curseur est dans le rectangle du bouton 'OK'
                        # petite animation du bouton 'OK' relâché
                        pygame.draw.rect(screen, (0, 0, 0),(bouton_oui.x + 1, bouton_oui.y + 1, bouton_oui.width, bouton_oui.height), 2,3)
                        pygame.draw.rect(screen, (255, 255, 255),bouton_oui, 2,3)
                        # on met 'clic' à vrai
                        clic = True
                        break
                    if bouton_non.collidepoint(e.pos): # Si la position du curseur est dans le rectangle du bouton 'NON'
                        # petite animation du bouton 'NON' relâché
                        pygame.draw.rect(screen, (0, 0, 0), (bouton_non.x+1,bouton_non.y+1,bouton_non.width,bouton_non.height), 2, 3)
                        pygame.draw.rect(screen, (255, 255, 255), bouton_non, 2, 3)
                        init_tiles()    # on réinitialise le plateau de jeu
                        remplissage()   # on le remplit de nouveau
                        affichage()     # on l'affiche

def menu(): # affiche et gère le menu
    button=False
    font = pygame.font.SysFont('Tahoma', 25)
    boutonplay=False # gère le bouton 'jouer' : si boutonplay==faux, il n'apparait pas

    while (not button):
        letsplay = False       # permet de lancer le jeu s'il est à vrai
        # color=((255,0,0))
        # screen.fill((2, 110, 200))

        rectScreen = screen.get_rect()
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 640, 480), 0)
        # fond d'écran
        bg = pygame.image.load("ville-isometrie_small.jpg")
        screen.blit(bg, (0, 0))
        # logo du jeu
        logo = pygame.image.load('logo.gif').convert()
        screen.blit(logo, (-5, -75))
        # bouton "plateau de jeu"
        creerplateau = font.render('Créer le plateau de jeu', 1, (255, 255, 255))
        rectPlateau = creerplateau.get_rect()
        rectPlateau.center = rectScreen.center
        pygame.draw.rect(screen,(0,0,0),(rectPlateau.x-10,rectPlateau.y-10,rectPlateau.width+20,rectPlateau.height+20))
        pygame.draw.rect(screen, (255, 255, 255),(rectPlateau.x - 10, rectPlateau.y - 10, rectPlateau.width + 20, rectPlateau.height + 20),2)
        # bouton "Entrer votre nom"
        askname = font.render('Entrer votre nom', 1, (255, 255, 255))
        rectName = askname.get_rect()
        rectName.center = rectScreen.center
        rectName.y=rectName.y-50
        pygame.draw.rect(screen,(0,0,0),(rectPlateau.x-10,rectName.y-10,rectPlateau.width+20,rectName.height+20))
        pygame.draw.rect(screen, (255, 255, 255),(rectPlateau.x - 10, rectName.y - 10, rectPlateau.width + 20, rectName.height + 20),2)
        # bouton "jouer"
        if boutonplay:  # si boutonplay==vrai alors on affiche le bouton 'jouer'
            playname = font.render('Jouer', 1, (255, 255, 255))
            rectPlay = playname.get_rect()
            rectPlay.center = rectScreen.center
            rectPlay.y = rectPlay.y + 50
            pygame.draw.rect(screen, (0, 0, 0),(rectPlateau.x - 10, rectPlay.y - 10, rectPlateau.width + 20, rectPlay.height + 20))
            pygame.draw.rect(screen, (255, 255, 255),(rectPlateau.x - 10, rectPlay.y - 10, rectPlateau.width + 20, rectPlay.height + 20), 2)
            screen.blit(playname, rectPlay)
        screen.blit(creerplateau, rectPlateau)
        screen.blit(askname, rectName)

        pygame.display.flip()
        button=False    # True si on a appuyé sur le bouton gauche de la souris, False sinon
        generation=False    # True si on a cliqué sur le nouton "générer terrain", False sinon
        nom=False   # True si on a cliqué sur le nouton "nouveau nom", False sinon
        newname=False   # True si on a entré un nouveau nom, False sinon

        # Tant qu'on n'a pas appuyé sur le bouton droit de la souris et qu'on n'a pas entré un nouveau nom et qu'on n'a pas pressé le bouton 'jouer'
        while not button and not newname and not letsplay:
            pygame.display.flip()
            for e in pygame.event.get():
                if e.type==QUIT:
                    sys.exit()
                if e.type==MOUSEBUTTONDOWN: # bouton enfoncé
                    if e.button==1: # si bouton gauche
                        mse = pygame.mouse.get_pos()    # on récupère la position du curseur de la souris
                        # bouton génération
                        if rectPlateau.collidepoint(e.pos): # si la position de la souris se trouve dans le bouton "generation"
                            # petite animation du bouton
                            pygame.draw.rect(screen, (0, 0, 0), (rectPlateau.x - 10, rectPlateau.y - 10, rectPlateau.width + 20, rectPlateau.height + 20), 2)
                            pygame.draw.rect(screen, (255, 255, 255), (rectPlateau.x - 8, rectPlateau.y - 8, rectPlateau.width + 20, rectPlateau.height + 20), 2)
                            # on met le booléen 'generation' à vrai
                            generation=True
                        # bouton nom
                        if rectName.collidepoint(e.pos): # si la position de la souris se trouve dans le bouton "nom"
                            # petite animation du bouton
                            pygame.draw.rect(screen, (0, 0, 0), (rectPlateau.x - 10, rectName.y - 10, rectPlateau.width + 20, rectName.height + 20), 2)
                            pygame.draw.rect(screen, (255, 255, 255), (rectPlateau.x - 8, rectName.y - 8, rectPlateau.width + 20, rectName.height + 20), 2)
                            # on met le booléen 'nom' à vrai
                            nom=True
                        # bouton play
                        if boutonplay and rectPlay.collidepoint(e.pos):  # si la position de la souris se trouve dans le bouton "Jouer"
                            # petite animation du bouton
                            pygame.draw.rect(screen, (0, 0, 0), (rectPlateau.x - 10, rectPlay.y - 10, rectPlateau.width + 20, rectPlay.height + 20), 2)
                            pygame.draw.rect(screen, (255, 255, 255), (rectPlateau.x - 8, rectPlay.y - 8, rectPlateau.width + 20, rectPlay.height + 20), 2)
                            # on met le booléen 'button' à vrai
                            button = True
                            # on rétablit une font normale
                            font = pygame.font.Font('freesansbold.ttf', 20)

                if e.type == MOUSEBUTTONUP: # bouton relâché
                    if e.button == 1: # si bouton gauche
                        if generation: # le bouton generation a été pressé auparavant
                            # petite animation du  bouton relâché
                            pygame.draw.rect(screen, (0, 0, 0),(rectPlateau.x - 8, rectPlateau.y - 8, rectPlateau.width + 20, rectPlateau.height + 20), 2)
                            pygame.draw.rect(screen, (255, 255, 255), (rectPlateau.x - 10, rectPlateau.y - 10, rectPlateau.width + 20, rectPlateau.height + 20), 2)
                            # on remet 'genaration' à faux pour pouvoir éventuellement recommencer
                            generation=False
                            remplissage()   # on remplit le plateau de jeu
                            affichage()     # on l'affiche
                            boutons_choix() # on appelle la fonction pour choisir si c'est bon ou pas
                            letsplay=True # L'utilisateur a choisi un plateau de jeu donc on peut jouer
                            boutonplay=True # L'utilisateur a choisi un plateau de jeu donc on peut afficher le bouton 'jouer'
                        if nom: # le bouton 'nom' a été pressé auparavant
                            # on affiche le bouton relâché
                            pygame.draw.rect(screen, (0, 0, 0), (rectPlateau.x - 8, rectName.y - 8, rectPlateau.width + 20, rectName.height + 20), 2)
                            pygame.draw.rect(screen, (255, 255, 255), (rectPlateau.x - 10, rectName.y - 10, rectPlateau.width + 20, rectName.height + 20), 2)
                            # on remet 'nom' à faux pour pouvoir éventuellement recommencer
                            nom = False
                            nom_lu=demandenom() # on récupère la valeur retournée par la fonction de saisie du nom
                            # On change le titre de la fenêtre
                            pygame.display.set_caption('Bienvenue '+nom_lu+' !')
                            # on a entré un nouveau nom donc on va redessiner le menu
                            newname=True
# fin fonction menu

def affichage():
    # on dessine le terrain de jeu en bleu clair (2,110,200)
    pygame.draw.rect(screen, (2, 110, 200), (0, 96, 640, 480), 0)
    # Dessin du grid
    color = (0, 0, 255)  # dessin en bleu foncé
    for colonne in range(0, 640, 32):  # lignes horizontales
        pygame.draw.line(screen, color, (colonne, 96), (colonne, 480))
    for ligne in range(96, 480, 32):  # lignes verticales
        pygame.draw.line(screen, color, (0, ligne), (640, ligne))

    #on parcourt toutes les tiles
    for colonne in range(21):
        for ligne in range(16):
            t=tiles[ligne][colonne]     # t est la tile en cours d'analyse
            if t.spr==water1 or t.spr==water2:  # pour les ports on affiche une animation
                if tileframe>999:   # SI ON EST 0 PLUS DE
                    t.spr=water1    # on met dans la tile le sprite 'water1'
                else:
                    t.spr=water2    # on met dans la tile le sprite 'water2'
            if t.spr==power1 or t.spr==power2:  # pour les power plants on affiche une animation
                if tileframe>999:
                    t.spr=power1    # on met dans la tile le sprite 'POWer1'
                else:
                    t.spr=power2    # on met dans la tile le sprite 'water2'
            if (t.typ!="rien"):             # si la tile n'est pas vide
                screen.blit(t.spr,t.pos)    # on affiche le sprite contenu dans la tile
    pygame.display.flip() # on met à jour la fenêtre
# fin fonction affichage

#######################
# PROGRAMME PRINCIPAL #
#######################
#initialisations de pygame
pygame.init()
font=pygame.font.SysFont('freesansbold.ttf', 20)
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption('Town Lite alpha version')
clock=pygame.time.Clock()

#sprites
grassspr=pygame.image.load('grass.png').convert()
roadvspr=pygame.image.load('road_v.png').convert()
roadhspr=pygame.image.load('road_h.png').convert()
roadsespr=pygame.image.load('se.png').convert()
roadsospr=pygame.image.load('so.png').convert()
roadnespr=pygame.image.load('ne.png').convert()
roadnospr=pygame.image.load('no.png').convert()
roadnocpr=pygame.image.load('crossroad.png').convert()
forestspr=pygame.image.load('forest.png').convert()
water1=pygame.image.load('water1.png').convert()
water2=pygame.image.load('water2.png').convert()
power1=pygame.image.load('power1.png').convert()
power2=pygame.image.load('power2.png').convert()
res=pygame.image.load('res.png').convert()
house1_0=pygame.image.load('house1_0.png').convert()
house1_1=pygame.image.load('house1_1.png').convert()
policehub=pygame.image.load('police.png').convert()
pompierhub=pygame.image.load('pompiernggggg.png').convert()
res.set_alpha(215)

# Variables et listes
tilelist=[grassspr,roadvspr,roadhspr,roadsespr,roadsospr,roadnespr,roadnospr,roadnocpr,water1,house1_1,power1,policehub,pompierhub]
namelist=['Grass','Road_V','Road_H','Road_SE','Road_SO','Road_NE','Road_NO','intersection','Water','home','Power Plant','Police','Fire Fighter']
costlist=[5,10,10,10,10,10,10,10,20,100,250,50,50]
poplist=[0,0,0,0,0,0,0,0,0,10,0,0,0]
tiles=[]
sel=1
money=10000
mse=(0,0)
tileframe=2000
pop=0
month=1
year=1
monthtime=0
R=1
C=1
I=1

class Tile(object):     # classe Tile qui définit la strucuture d'une tile
    def __init__(self,pos,spr,typ): # constructeur de Tile
        self.typ=typ
        self.spr=spr
        self.pos=pos
        self.rect=pygame.rect.Rect(pos[0],pos[1],32,32)
        self.adv=0
        self.haspower=0

# origine affichage tiles
base=100

menu()
pygame.mixer.init()  # on initialise la musique
pygame.mixer.music.load("undertale-ost-071-undertale.wav")  # on charge le morceau
pygame.mixer.music.play(-1)  # on lance le morceau de musique en boucle (-1)

while True:
    #remplissage de la fenêtre avec du bleu clair
    screen.fill((2,110,200))
    # cartouche noir en haut de la fenêtre
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 640, 96), 0)

    # Dessin du grid
    color=(0,0,255) # dessin en bleu foncé
    for colonne in range(0,640,32): # lignes horizontales tous les 32 pixels
        pygame.draw.line(screen,color,(colonne,96),(colonne,480))
    for ligne in range(96,480,32): # lignes verticales
        pygame.draw.line(screen,color,(0,ligne),(640,ligne))

    # affichage des tiles disponibles en haut de la fenêtre
    pos = [base, 5]
    color=(255,255,255)
    for numliste in range(1,13):
        pygame.draw.rect(screen, color, pygame.Rect(pos[0]-1, 4, 34, 34), 2)
        iconrect = tilelist[numliste].get_rect()
        iconrect = iconrect.move(pos)
        screen.blit( tilelist[numliste], iconrect)
        pos[0] = pos[0] + 40

    # cadre rouge sur la tile sélectionnée
    color=(255,0,0)
    pygame.draw.rect(screen,color,pygame.Rect(100+40*(sel-1)-1,4,34,34),2)

    # affichage des données
    moneydraw = font.render('Funds: ' + str(money), 1, (255, 255, 255))
    yeardraw = font.render('Year: ' + str(year), 1, (255, 255, 255))
    monthdraw = font.render('Month: ' + str(month), 1, (255, 255, 255))
    popdraw = font.render('Pop: ' + str(pop), 1, (255,255,255))
    namedraw = font.render(namelist[sel], 1, (255, 255, 255))
    screen.blit(moneydraw, (5, 2))
    screen.blit(namedraw, (5, 18))
    screen.blit(yeardraw, (5, 34))
    screen.blit(monthdraw, (5, 50))
    screen.blit(popdraw,(5, 66))

    #key=pygame.key.get_pressed()

    for e in pygame.event.get(): #gestion des évènements
        if e.type==QUIT:    # si on clique sur la croix rouge de la fenêtre
            sys.exit()  # ça ferme le programme
        if e.type==MOUSEBUTTONDOWN: # si on appuie sur un bouton de la souris
            # sélection des tiles
            x,y=e.pos       # position où a été cliqué le bouton de la souris
            # selon la position, on met dans 'sel' le numéro de la case de la tile sélectionnée
            if (x>base and x<base+32 and y>5 and y<37):             # tile[1]=route verticale
                sel=1
            if (x >base+40  and x<base+72 and y > 5 and y < 37):    # tile[2]=route horizontale
                sel=2
            if (x >base+80 and x<base+112 and y > 5 and y < 37):    # tile[3]=route sud-est
                sel=3
            if (x >base+120 and x<base+152 and y > 5 and y < 37):   # tile[4]=route sud-ouest
                sel=4
            if (x >base+160 and x<base+192 and y > 5 and y < 37):   # tile[5]=route nord-est
                sel=5
            if (x >base+200 and x <base+212 and y > 5 and y < 37):  # tile[6]=route nord-ouest
                sel=6
            if (x >base+240 and x <base+272 and y > 5 and y < 37):  # tile[7]=forêt
                sel=7
            if (x >base+280 and x <base+312 and y > 5 and y < 37):  # tile[8]=port
                sel=8
            if (x >base+320 and x <base+352 and y > 5 and y < 37):  # tile[9]=résidentiel
                sel=9
            if (x >base+360 and x <base+392 and y > 5 and y < 37):  # tile[10]=éolienne
                sel=10
            if (x >base+400 and x<base+452 and y > 5 and y <37):
                sel=11
            if (x >base+440 and x<base+492 and y > 5 and y <37):
                sel=12
            if (x >base+480 and x<base+512 and y > 5 and y <37):
                sel=13

# Modification des tiles quand la souris est en mouvement
        if e.type==MOUSEMOTION: # si la soruis est en mouvement
            mse=pygame.mouse.get_pos()  # on récupère dans mse[0] sa position en x et dans mse[1] sa position en y
            if (mse[1]>100):    # si y de la souris > 100 (en dessous du cartouche noir)
                # on reporte les coordonnées de la souris sur le grid en divisant par 32
                coordx = int(mse[0] / 32)
                coordy = int(mse[1] / 32)
                t = tiles[coordy][coordx]
                if pygame.mouse.get_pressed()==(1,0,0): # bouton de gauche pressé
                     if (t.typ != "rien" and t.spr == grassspr): # si la tile n'est pas vide et contient de l'herbe
                        if sel == 11: # si la sélection est une tile "Power Plant"
                            money -= costlist[sel]  # on met à jour l'argent
                            pop += poplist[sel]
                            tiles[coordy][coordx].spr = tilelist[sel] # on change le genre de tile avec la sélection
                            tiles[coordy][coordx].typ = namelist[sel] # type de la sélection

                        elif (sel == 1):    # sélection : route verticale
                            possible = test_routeV(coordy, coordx)  # on teste si on peut la poser
                            if (possible):  # si oui
                                money -= costlist[sel]  # on met à jour l'argent
                                pop += poplist[sel]
                                tiles[coordy][coordx].spr = tilelist[sel]  # on change le genre de tile avec la sélection
                                tiles[coordy][coordx].typ = namelist[sel]  # type de la sélection

                        elif (sel == 2):    # sélection : route horizontale
                            possible = test_routeH(coordy, coordx)  # on teste si on peut la poser
                            if (possible):  # si oui
                                money -= costlist[sel]  # on met à jour l'argent
                                pop -= poplist[sel]
                                tiles[coordy][coordx].spr = tilelist[sel]  # on change le genre de tile avec la sélection
                                tiles[coordy][coordx].typ = namelist[sel]  # type de la sélection

                        elif (sel == 3):    # sélection : route sud-est
                            possible = test_routeSE(coordy, coordx)  # on teste si on peut la poser
                            if (possible):  # si oui
                                money -= costlist[sel]  # on met à jour l'argent
                                pop += poplist[sel]
                                tiles[coordy][coordx].spr = tilelist[sel]  # on change le genre de tile avec la sélection
                                tiles[coordy][coordx].typ = namelist[sel]  # type de la sélection

                        elif (sel == 4):    # sélection : route sud-ouest
                            possible = test_routeSO(coordy, coordx)  # on teste si on peut la poser
                            if (possible):  # si oui
                                money -= costlist[sel]  # on met à jour l'argent
                                pop += poplist[sel]
                                tiles[coordy][coordx].spr = tilelist[sel]  # on change le genre de tile avec la sélection
                                tiles[coordy][coordx].typ = namelist[sel]  # type de la sélection

                        elif (sel == 5):    # sélection : route nord-est
                            possible = test_routeNE(coordy, coordx)  # on teste si on peut la poser
                            if (possible):  # si oui
                                money -= costlist[sel]  # on met à jour l'argent
                                pop -= poplist[sel]
                                tiles[coordy][coordx].spr = tilelist[sel]  # on change le genre de tile avec la sélection
                                tiles[coordy][coordx].typ = namelist[sel]  # type de la sélection

                        elif (sel == 6):    # sélection : route nord-ouest
                            possible = test_routeNO(coordy, coordx)  # on teste si on peut la poser
                            if (possible):  # si oui
                                money -= costlist[sel]  # on met à jour l'argent
                                pop += poplist[sel]
                                tiles[coordy][coordx].spr = tilelist[sel]  # on change le genre de tile avec la sélection
                                tiles[coordy][coordx].typ = namelist[sel]  # type de la sélection

                        elif (sel == 10):    # sélection : route nord-ouest
                                money -= costlist[sel]  # on met à jour l'argent
                                pop += poplist[sel]
                                tiles[coordy][coordx].spr = tilelist[sel]  # on change le genre de tile avec la sélection
                                tiles[coordy][coordx].typ = namelist[sel]

                        elif (sel != 8):    # sinon, si la sélection n'est pas le port
                            money -= costlist[sel]  # on met à jour l'argent
                            pop += poplist[sel]
                            tiles[coordy][coordx].spr = tilelist[sel]  # on change le genre de tile avec la sélection
                            tiles[coordy][coordx].typ = namelist[sel]  # type de la sélection

                     elif (t.typ == "rien" and sel == 8): # si on n'est pas sur terre et qu'on a sélectionné un port
                        money -= costlist[sel]  # on met à jour l'argent
                        pop += poplist[sel]
                        tiles[coordy][coordx].spr = tilelist[sel]  # on change le genre de tile avec la sélection
                        tiles[coordy][coordx].typ = 'harbour'

                        tiles[coordy][coordx].pos = (coordx * 32, coordy * 32)
                elif (pygame.mouse.get_pressed()==(0,0,1)): # si on appuie sur le bouton de droite (pour effacer)
                    if (t.typ != "rien" and t.spr != grassspr):
                        money -= 5
                        if (t.typ == "home"):
                            pop -= 10
                            # Si ce n'est pas sur l'eau, et que le type n'est pas 'harbour' et que ce n'est pas de l'herbe
                            if (t.typ != "rien" and t.typ != 'harbour' and t.spr != grassspr):
                                tiles[coordy][coordx].spr = grassspr  # alors on remet de l'herbe pour effacer
                                tiles[coordy][coordx].typ = namelist[0]  # c'est une tile 'Grass''
                            elif (t.typ == "harbour"):  # si la tile est un port
                                tiles[coordy][coordx].typ = 'rien'  # on lui redonne le type 'rien' de l'eau
                        else:
                            # Si ce n'est pas sur l'eau, et que le type n'est pas 'harbour' et que ce n'est pas de l'herbe
                            if (t.typ != "rien" and t.typ != 'harbour' and t.spr != grassspr):
                                tiles[coordy][coordx].spr = grassspr  # alors on remet de l'herbe pour effacer
                                tiles[coordy][coordx].typ = namelist[0]  # c'est une tile 'Grass''
                            elif (t.typ == "harbour"):  # si la tile est un port
                                tiles[coordy][coordx].typ = 'rien'  # on lui redonne le type 'rien' de l'eau
                    else:
                        continue
# Modification des tiles quand la souris n'est pas en mouvement
# ON NE COMMENTERA PAS LE CODE IDENTIQUE AU CAS Où LA SOURIS EST EN MOUVEMENT, CE SERAIT LA Même CHOSE
        if e.type==MOUSEBUTTONUP: # si un bouton de la souris est pressé
            # mse[0]=position en x de la souris
            # mse[1]=position en y de la souris
            mse = pygame.mouse.get_pos()
            if (mse[1] > 100):
                # on reporte les coordonnées de la souris sur le grid en divisant par 32
                coordx = int(mse[0] / 32)
                coordy = int(mse[1] / 32)
                # on récupère la tile correspondante dans t
                t = tiles[coordy][coordx]
                if e.button==1: # bouton de gauche de la souris pressé
                    # si on est pas sur l'eau, mais sur l'herbe
                    if (t.typ!="rien" and t.spr==grassspr):
                        # si la sélection est une tile "Power Plant"
                        if sel == 9:
                            money -= costlist[sel]
                            pop += poplist[sel]
                            tiles[coordy][coordx].spr = tilelist[sel]
                            tiles[coordy][coordx].typ = namelist[sel]

                        elif (sel==1):
                            possible=test_routeV(coordy,coordx)
                            if (possible):
                                money -= costlist[sel]  # on met à jour l'argent
                                pop += poplist[sel]
                                tiles[coordy][coordx].spr = tilelist[sel]  # on change le genre de tile avec la sélection
                                tiles[coordy][coordx].typ = namelist[sel]  # type de la sélection

                        elif (sel==2):
                            possible = test_routeH(coordy, coordx)
                            if (possible):
                                money -= costlist[sel]  # on met à jour l'argent
                                pop += poplist[sel]
                                tiles[coordy][coordx].spr = tilelist[sel]  # on change le genre de tile avec la sélection
                                tiles[coordy][coordx].typ = namelist[sel]  # type de la sélection
                        elif (sel == 3):
                            possible = test_routeSE(coordy, coordx)
                            if (possible):
                                money -= costlist[sel]  # on met à jour l'argent
                                pop += poplist[sel]
                                tiles[coordy][coordx].spr = tilelist[sel]  # on change le genre de tile avec la sélection
                                tiles[coordy][coordx].typ = namelist[sel]  # type de la sélection
                        elif (sel == 4):
                            possible = test_routeSO(coordy, coordx)
                            if (possible):
                                money -= costlist[sel]  # on met à jour l'argent
                                pop += poplist[sel]
                                tiles[coordy][coordx].spr = tilelist[sel]  # on change le genre de tile avec la sélection
                                tiles[coordy][coordx].typ = namelist[sel]  # type de la sélection
                        elif (sel == 5):
                            possible = test_routeNE(coordy, coordx)
                            if (possible):
                                money -= costlist[sel]  # on met à jour l'argent
                                pop += poplist[sel]
                                tiles[coordy][coordx].spr = tilelist[sel]  # on change le genre de tile avec la sélection
                                tiles[coordy][coordx].typ = namelist[sel]  # type de la sélection
                        elif (sel == 6):
                            possible = test_routeNO(coordy, coordx)
                            if (possible):
                                money -= costlist[sel]  # on met à jour l'argent
                                pop += poplist[sel]
                                tiles[coordy][coordx].spr = tilelist[sel]  # on change le genre de tile avec la sélection
                                tiles[coordy][coordx].typ = namelist[sel]  # type de la sélection
                        elif (sel != 8): # si la sélectio n'est pas une tile "port"
                                money -= costlist[sel] # on met à jour l'argent
                                pop += poplist[sel]
                                tiles[coordy][coordx].spr = tilelist[sel] # on change le genre de tile avec la sélection
                                tiles[coordy][coordx].typ = namelist[sel] # type 'tile' simple
                    elif (t.typ=="rien" and sel==8): # si on a cliqué sur l'eau et qu'on a sélectionné la tile 'port'
                        money -= costlist[sel]  # on met l'argent à jour
                        pop += poplist[sel]
                        tiles[coordy][coordx].spr =tilelist[sel]    # on change le genre de tile avec la sélection
                        tiles[coordy][coordx].typ='harbour' # on lui donne le type 'harbour'
                        tiles[coordy][coordx].pos=(coordx*32,coordy*32) # on lui donne les coordonnées réelles à l'écran
                elif (e.button==3): # appui sur le bouton de droite
                    if (t.typ !="rien" and t.spr !=grassspr):
                        money -= 5
                        if (t.typ == "home"):
                            pop -= 10
                            # Si ce n'est pas sur l'eau, et que le type n'est pas 'harbour' et que ce n'est pas de l'herbe
                            if (t.typ != "rien" and t.typ != 'harbour' and t.spr != grassspr):
                                tiles[coordy][coordx].spr = grassspr  # alors on remet de l'herbe pour effacer
                                tiles[coordy][coordx].typ = namelist[0]  # c'est une tile 'Grass''
                            elif (t.typ == "harbour"):  # si la tile est un port
                                tiles[coordy][coordx].typ = 'rien'  # on lui redonne le type 'rien' de l'eau
                        else:
                            # Si ce n'est pas sur l'eau, et que le type n'est pas 'harbour' et que ce n'est pas de l'herbe
                            if (t.typ != "rien" and t.typ != 'harbour' and t.spr != grassspr):
                                tiles[coordy][coordx].spr = grassspr  # alors on remet de l'herbe pour effacer
                                tiles[coordy][coordx].typ = namelist[0]  # c'est une tile 'Grass''
                            elif (t.typ == "harbour"):  # si la tile est un port
                                tiles[coordy][coordx].typ = 'rien'  # on lui redonne le type 'rien' de l'eau
                    else:
                        continue

    affichage()
    if monthtime<10000:
        monthtime+=1
    else:
        month+=1
        money+=20
        monthtime=0
        if month==13:
            month=0
            year+=1

    clock.tick(999)
    tileframe-=1
    if tileframe==0:tileframe=2000
    pygame.display.flip()
