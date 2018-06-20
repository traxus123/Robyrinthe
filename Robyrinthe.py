#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os
import glob

#Déclaration des constantes
AVANT_DROIT_AVANT = 12
AVANT_DROIT_ARRIERE = 16
AVANT_GAUCHE_AVANT = 6
AVANT_GAUCHE_ARRIERE = 13
ARRIERE_DROIT_AVANT = 20
ARRIERE_DROIT_ARRIERE = 21
ARRIERE_GAUCHE_AVANT = 19
ARRIERE_GAUCHE_ARRIERE = 26
DETECTEUR_AVANT = 4
DETECTEUR_GAUCHE = 17
DETECTEUR_DROIT = 18

#Initialise les ports GPIO
def setGPIO():
	#Initialisation GPIO
	GPIO.setmode(GPIO.BCM)

	#Deffinition des sorties GPIO

	#Avant Droit
	GPIO.setup(AVANT_DROIT_AVANT,GPIO.OUT)
	GPIO.setup(AVANT_DROIT_ARRIERE,GPIO.OUT)
	#Avant Gauche
	GPIO.setup(AVANT_GAUCHE_AVANT,GPIO.OUT)
	GPIO.setup(AVANT_GAUCHE_ARRIERE,GPIO.OUT)

	#Arrière Droit
	GPIO.setup(ARRIERE_DROIT_AVANT,GPIO.OUT)
	GPIO.setup(ARRIERE_DROIT_ARRIERE,GPIO.OUT)
	#Arrière Gauche
	GPIO.setup(ARRIERE_GAUCHE_AVANT,GPIO.OUT)
	GPIO.setup(ARRIERE_GAUCHE_ARRIERE,GPIO.OUT)

	#Deffinition des entrées GPIO

	#Detecteur Haut
	GPIO.setup(DETECTEUR_AVANT,GPIO.IN)
	#Detecteur Gauche
	GPIO.setup(DETECTEUR_GAUCHE,GPIO.IN)
	#Detecteur Droit
	GPIO.setup(DETECTEUR_DROIT,GPIO.IN)

#Déaloue les différents ports GPIO
def unsetGPIO():
	 GPIO.cleanup()

#Fonction de contrôle du robot

#Arret complet du robot
def Stop():
	#Mise a 0 Avancer
	GPIO.output(AVANT_DROIT_AVANT, 0)
	GPIO.output(AVANT_GAUCHE_AVANT, 0)
	GPIO.output(ARRIERE_DROIT_AVANT, 0)
	GPIO.output(ARRIERE_GAUCHE_AVANT, 0)

	#Mise a 0 Reculer
	GPIO.output(AVANT_DROIT_ARRIERE, 0)
	GPIO.output(AVANT_GAUCHE_ARRIERE, 0)
	GPIO.output(ARRIERE_DROIT_ARRIERE, 0)
	GPIO.output(ARRIERE_GAUCHE_ARRIERE, 0)


#Marche avant du robot
def Avancer():
	Stop()

	GPIO.output(AVANT_DROIT_AVANT, 1)
	GPIO.output(AVANT_GAUCHE_AVANT, 1)
	GPIO.output(ARRIERE_DROIT_AVANT, 1)
	GPIO.output(ARRIERE_GAUCHE_AVANT, 1)

#Marche arrière du robot
def Reculer():
	Stop()

	GPIO.output(AVANT_DROIT_ARRIERE, 1)
	GPIO.output(AVANT_GAUCHE_ARRIERE, 1)
	GPIO.output(ARRIERE_DROIT_ARRIERE, 1)
	GPIO.output(ARRIERE_GAUCHE_ARRIERE, 1)

#Tourner a droite durant n ms
def Droite(n):
	Stop()

	#Mise en marche avant des moteurs gauche
	GPIO.output(AVANT_GAUCHE_AVANT, 1)
	GPIO.output(ARRIERE_GAUCHE_AVANT, 1)
	#Mise en marche arrière des moteurs droite
	GPIO.output(AVANT_DROIT_ARRIERE, 1)
	GPIO.output(ARRIERE_DROIT_ARRIERE, 1)

	time.sleep(n)

	Stop()

#Tourner a gauche durant n ms
def Gauche(n):
	Stop()

	#Mise en marche avant des moteurs droite
	GPIO.output(AVANT_DROIT_AVANT, 1)
	GPIO.output(ARRIERE_DROIT_AVANT, 1)
	#Mise en marche arrière des moteurs gauche
	GPIO.output(AVANT_GAUCHE_ARRIERE, 1)
	GPIO.output(ARRIERE_GAUCHE_ARRIERE, 1)

	time.sleep(n)

	Stop()


#Fonctions Capteurs

#Renvoie un bouléen en fonction de la présence d'un mur devant
def murDevant():
	if(GPIO.input(DETECTEUR_AVANT)):
		return True
	else:
		return False

#Renvoie un bouléen en fonction de la présence d'un mur a gauche
def murGauche():
	if(GPIO.input(DETECTEUR_GAUCHE)):
		return True
	else:
		return False

#Renvoie un bouléen en fonction de la présence d'un mur a droite
def murDroit():
	if(GPIO.input(DETECTEUR_DROIT)):
		return True
	else:
		return False

def main():
	setGPIO()
	while True:
		
		if(murGauche()):
			if(mureDroit()):
				Droite(6)
			else:
				Gauche(3)
		else:
			Droit(3)
		
		end = False
		while end:
			Avancer()
			time.sleep(0.1)
			if(murDevant()):
				end = True
		Stop()
