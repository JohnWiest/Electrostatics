import pygame
import math
import random
import sys

pygame.init()

screen = pygame.display.set_mode((2560,1440))

charge = pygame.image.load("basketball.jpg")
charge_fixed = pygame.image.load("basketball.jpg")

def updateScreen((x_c,y_c),(x_cf,y_cf)):
	screen.fill((0,0,0))
	screen.blit(charge,(x_c,y_c))
	screen.blit(charge_fixed,(x_cf,y_cf))
	pygame.display.update()
	return

def forceGravity(m):
	a_g = 9.8
	F_g = m*a
	return F_g

def forceElectricX(x_c,y_c,x_cf,y_cf,q_c,q_cf,k):
	F_ex = (k*q_c*q_cf*(x_c-x_cf))/(((x_c-x_cf)^2+(y_c-y_cf)^2)^(3/2))
	return F_ex

def forceElectricY(x_c,y_c,x_cf,y_cf,q_c,q_cf,k):
	F_ey = (k*q_c*q_cf*(y_c-y_cf))/(((x_c-x_cf)^2+(y_c-y_cf)^2)^(3/2))
	return F_ey

def velocityX(m,F_ex,v_x):
	v_x += F_ex/m 
	return v_x

def velocityY(m,F_g,F_ey,v_y):
	v_y += (F_g+F_ey)/m
	return v_y

def updatePosition(x_c,y_c,v_x,v_y):
	x_c += v_x
	y_c += v_y
	return (x_c,y_c)

def main():
	x_c = 1280
	y_c = 0
	x_cf = 1280
	y_cf = 1000
	v_x = 0
	v_y = 0
	m = 1
	k = //
	q_c = //
	q_cf = //
	Run = True
	while Run:
		pygame.time.delay(1)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()

		if pygame.mouse.get_pressed() == //:
		 x_c = pygame.mouse.get_pos()[0]
		 y_c = pygame.mouse.get_pos()[1]
		 updateScreen((x_c,y_c),(x_cf,y_cf))

		if keys[pygame.K_Q]:
			q_c = input("What is the charge value of the free charge?")
			q_cf = input("What is the charge value of the fixed charge?")
		
		if keys[pygame.K_P]
			x_c = input("What is the value of free charge's x coordinate?")
			y_c = input("What is the value of free charge's y coordinate?")
			x_cf = input("What is the value of fixed charge's x coordinate?")
			y_cf = input("What is the value of fixed charge's y coordinate?")
			updateScreen((x_c,y_c),(x_cf,y_cf))

		if keys[pygame.K_M]:
			m = input("what is the mass of your charge?")

		if keys[pygame.K_K]:
			k = input("what is your electrostatic constant?")

		else:
			F_g = forgeGravity(m)
			F_ex = forceElectricX(x_c,y_c,x_cf,y_cf,q_c,q_cf,k)
			F_ey = forceElectricY(x_c,y_c,x_cf,y_cf,q_c,q_cf,k)
			v_x = velocityX(m,F_ex,v_x)
			v_y = velocityY(m,F_g,F_ey,v_y)
			updateScreen(updatePosition(x_c,y_c,v_x,v_y),(x_cf,y_cf))

	return
