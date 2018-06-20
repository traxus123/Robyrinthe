#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os
import glob

#Initialise les ports GPIO
def setGPIO():
	#Initialisation GPIO
	GPIO.setmode(GPIO.BCM)

	#Deffinition des sorties GPIO

	#Avant Droit
	GPIO.setup(12,GPIO.OUT)
	GPIO.setup(16,GPIO.OUT)
	#Avant Gauche
	GPIO.setup(	,GPIO.OUT)
	GPIO.setup(13,GPIO.OUT)

	#Arrière Droit
	GPIO.setup(20,GPIO.OUT)
	GPIO.setup(21,GPIO.OUT)
	#Arrière Gauche
	GPIO.setup(19,GPIO.OUT)
	GPIO.setup(26,GPIO.OUT)

	#Deffinition des entrées GPIO

	#Detecteur Haut
	GPIO.setup(4,GPIO.IN)
	#Detecteur Gauche
	GPIO.setup(17,GPIO.IN)
	#Detecteur Droit
	GPIO.setup(18,GPIO.IN)

#Déaloue les différents ports GPIO
def unsetGPIO():
	 GPIO.cleanup()

#Fonction de contrôle du robot

#Arret complet du robot
def Stop():
	#Mise a 0 Avancer
	GPIO.output(12, 0)
	GPIO.output(16, 0)
	GPIO.output(6, 0)
	GPIO.output(13, 0)

	#Mise a 0 Reculer
	GPIO.output(20, 0)
	GPIO.output(21, 0)
	GPIO.output(19, 0)
	GPIO.output(26, 0)


#Marche avant du robot
def Avancer():
	Stop()

	GPIO.output(12, 1)
	GPIO.output(16, 1)
	GPIO.output(6, 1)
	GPIO.output(13, 1)

#Marche arrière du robot
def Reculer():
	Stop()

	GPIO.output(20, 1)
	GPIO.output(21, 1)
	GPIO.output(19, 1)
	GPIO.output(26, 1)

#Tourner a droite durant n ms
def Droite(n):
	Stop()

	#Mise en marche avant des moteurs gauche
	GPIO.output(6, 1)
	GPIO.output(13, 1)
	#Mise en marche arrière des moteurs droite
	GPIO.output(20, 1)
	GPIO.output(21, 1)

	time.sleep(n)

	Stop()

#Tourner a gauche durant n ms
def Gauche(n):
	Stop()

	#Mise en marche avant des moteurs droite
	GPIO.output(12, 1)
	GPIO.output(16, 1)
	#Mise en marche arrière des moteurs gauche
	GPIO.output(19, 1)
	GPIO.output(26, 1)

	time.sleep(n)

	Stop()


#Fonctions Capteurs

#Renvoie un bouléen en fonction de la présence d'un mur devant
def murDevant():
	if(GPIO.input(4)):
		return True
	else:
		return False

#Renvoie un bouléen en fonction de la présence d'un mur a gauche
def murGauche():
	if(GPIO.input(17)):
		return True
	else:
		return False

#Renvoie un bouléen en fonction de la présence d'un mur a droite
def murDroit():
	if(GPIO.input(18)):
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
