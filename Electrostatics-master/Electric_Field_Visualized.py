import pygame
import math
import random
import sys
import os

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'

screen = pygame.display.set_mode((2560,1440),)

charge = pygame.image.load("basketball.png")
charge_fixed = pygame.image.load("basketball.png")
backboard = pygame.image.load("backboard.png")
net = pygame.image.load("net.png")

def updateScreen(x_c,y_c,x_cf,y_cf,x_b,y_b,x_n,y_n):
	screen.fill((0,0,0))
	screen.blit(backboard,(x_b,x_b))
	screen.blit(charge,(x_c-35.5,y_c-36))
	screen.blit(charge_fixed,(x_cf-35.5,y_cf-36))
	screen.blit(net,(x_n,y_n))
	pygame.display.update()
	return

def forceGravity(m):
	a_g = 0.33
	F_g = m*a_g
	return F_g

def forceElectricX(x_c,y_c,x_cf,y_cf,q_c,q_cf,k):
	F_ex = (k*q_c*q_cf*(x_c-x_cf))/(((x_c-x_cf)**2+(y_c-y_cf)**2)**(3/2))
	return F_ex

def forceElectricY(x_c,y_c,x_cf,y_cf,q_c,q_cf,k):
	F_ey = (k*q_c*q_cf*(y_c-y_cf))/(((x_c-x_cf)**2+(y_c-y_cf)**2)**(3/2))
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

def hoopMove(x_h,y_h):
	x_h 

def main():
	x_c = 1244
	y_c = 200
	x_cf = 2260
	y_cf = 1140
	x_b = 300
	y_b = 300
	x_n = x_b+60
	y_n = y_b+130
	v_x = 0
	v_y = 0
	m = 1
	k = 200
	q_c = 20
	q_cf = 20
	run = True
	while run:
		pygame.time.delay(1)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()

		if keys[pygame.K_1]:
			x_cf = 1660
			y_cf = 1140

		if keys[pygame.K_2]:
			x_cf = 1960
			y_cf = 1140

		if keys[pygame.K_3]:
			x_cf = 2260
			y_cf = 1140



		if pygame.mouse.get_pressed()[0]:
		 v_x = 0
		 v_y = 0
		 x_c = pygame.mouse.get_pos()[0]
		 y_c = pygame.mouse.get_pos()[1]
		 updateScreen(x_c,y_c,x_cf,y_cf,x_b,y_b,x_n,y_n)
		
		if v_x < -3 and x_c < 20:
				pygame.mixer.music.load("bounce.mp3")
				pygame.mixer.music.play()
				pygame.time.delay(12)
		
		if x_c <= 0:
			v_x = -v_x
			x_c = 0
		
		if v_x > 3 and x_c > 2469:
				pygame.mixer.music.load("bounce.mp3")
				pygame.mixer.music.play()
				pygame.time.delay(12)

		if x_c >= 2489:
			v_x = -v_x
			x_c = 2489
			
		if v_y > 3 and y_c > 1348:
				pygame.mixer.music.load("bounce.mp3")
				pygame.mixer.music.play()
				pygame.time.delay(12)

		if y_c >= 1368:
			v_y = -v_y
			y_c = 1368
	
		if  x_n+11 < x_c < x_n+131 and y_n-4 < y_c < y_n+15 and v_y > 0:
				pygame.mixer.music.load("swish.mp3")
				pygame.mixer.music.play()
				pygame.time.delay(12)


		if keys[pygame.K_UP]:
			x_c = 1244
			y_c = 200
			v_x = 0
			v_y = 0


		#if keys[pygame.K_Q]:
			#q_c = input("What is the charge value of the free charge?")
			#q_cf = input("What is the charge value of the fixed charge?")
		
		#if keys[pygame.K_P]:
			#x_c = input("What is the value of free charge's x coordinate?")
			#y_c = input("What is the value of free charge's y coordinate?")
			#x_cf = input("What is the value of fixed charge's x coordinate?")
			#y_cf = input("What is the value of fixed charge's y coordinate?")
			#updateScreen((x_c,y_c),(x_cf,y_cf))

		#if keys[pygame.K_M]:
			#m = input("what is the mass of your charge?")

		#if keys[pygame.K_K]:
			#k = input("what is your electrostatic constant?")

		#else:
		F_g = forceGravity(m)
		#print(F_g)
		F_ex = forceElectricX(x_c,y_c,x_cf,y_cf,q_c,q_cf,k)
		#print(F_ex)
		F_ey = forceElectricY(x_c,y_c,x_cf,y_cf,q_c,q_cf,k)
		#print(F_ey)
		v_x = velocityX(m,F_ex,v_x)
		#print(v_x)
		v_y = velocityY(m,F_g,F_ey,v_y)
		#print(v_y)
		x_c = updatePosition(x_c,y_c,v_x,v_y)[0]
		#print(x_c)
		y_c = updatePosition(x_c,y_c,v_x,v_y)[1]
		#print(y_c)
		updateScreen(x_c,y_c,x_cf,y_cf,x_b,y_b,x_n,y_n)

	pygame.quit()
	return

main()

#make sound its own function and make it play slightly early
