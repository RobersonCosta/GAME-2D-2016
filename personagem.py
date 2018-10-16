from graphics import *
from fisica import *	
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager, BaseProxy
import operator
import glob

class Personagem():
	def __init__ (self, x, y, window, name, side):
		self.win = window
		self.ani_right = glob.glob("animations/"+str(name)+"/right/frame*.gif")
		self.ani_right.sort()
		self.ani_left = glob.glob("animations/"+str(name)+"/left/frame*.gif")
		self.ani_left.sort()
		self.ani_up_right = glob.glob("animations/"+str(name)+"/up/right/frame*.gif")
		self.ani_up_right.sort()
		self.ani_up_left = glob.glob("animations/"+str(name)+"/up/left/frame*.gif")
		self.ani_up_left.sort()				
		self.ani_max = len(self.ani_right)-1
		if (side == "right"):
			self.personagem = Image(Point(x,y),self.ani_right[0])
		if (side == "left"):
			self.personagem = Image(Point(x,y),self.ani_left[0])
		self.personagem.draw(self.win)
		self.side = side
		self.y = self.personagem.getAnchor().getY()




	def walk(self, key, ratio_walk, ratio_sleep):
		if (key=="Right"):			
			for ani in self.ani_right[1:]:			
				self.personagem = self.personagem.reload_walk(self.win, ani, abs(ratio_walk))
				time.sleep(ratio_sleep)	
				if (self.ani_right[self.ani_max]):
					self.personagem = self.personagem.reload_walk(self.win, self.ani_right[0], abs(ratio_walk))
			self.side = "right"
		if (key=="Left"):
			for ani in self.ani_left[1:]:				
				self.personagem = self.personagem.reload_walk(self.win, ani, ratio_walk)
				time.sleep(ratio_sleep)	
				if (self.ani_left[self.ani_max]):
					self.personagem = self.personagem.reload_walk(self.win, self.ani_left[0], ratio_walk)
			self.side = "left"

	def jump(self,range_jump, ratio_sleep):
		if(self.side == "right"):
			ani_up = self.ani_up_right
		elif(self.side == "left"):
			ani_up = self.ani_up_left	
		self.personagem = self.personagem.reload_jump(self.win, ani_up, range_jump, ratio_sleep)

	def jump_side(self, key, range_side, range_jump, ratio_sleep):
		if(key == "Right"):
			ani_up = self.ani_up_right
		elif(key == "Left"):
			ani_up = self.ani_up_left	
		self.personagem = self.personagem.reload_jump_side(self.win, key, ani_up, range_side, range_jump, ratio_sleep)

	def draw(self, x, y, side):
		if (side == "Right"):
			ani = self.ani_right[0]
		elif(side == "Left"):
			ani = self.ani_left[0]
		self.personagem = Image(Point(x,y), ani)
		self.personagem.draw(self.win)




class Player(Personagem):
	def __init__(self, x, y, window, name, side):		
		Personagem.__init__(self, x, y, window, name, side)
		self.fisica = Fisica(window.getWidth(), window.getHeight())
		self.ani_attack_right = glob.glob("animations/"+str(name)+"/attack/right/frame*.gif")
		self.ani_attack_right.sort()
		self.ani_attack_left = glob.glob("animations/"+str(name)+"/attack/left/frame*.gif")
		self.ani_attack_left.sort()
		self.alvo_pontos = 0
		self.pontos = 0
		self.result = False
		self.contador = 0


	def update(self, keys, rival, vel, ponto_max):
		if (self.alvo_pontos/5>=ponto_max):
			self.result = True
			self.alvo_pontos = 0
		else:
			self.result = False
		walk = ["Right","Left"]
		if (keys):			
			self.contador+=300
			if (keys[0] in walk):
				self.walk(keys[0], -2, vel)
			if (keys[0] == "z"):
				self.attack(0.09, rival)
			if (keys[0] == "Up" and len(keys)>=2 and keys[1] in walk):
				self.jump_side(keys[1], -4.5, -23, 0.020)
			elif(keys[0] == "Up"):
				self.jump(-20, 0.021)

		self.contador+=1


	def attack(self, ratio_sleep, rival):
		if(self.side == "right"):
			ani_attack = self.ani_attack_right
		elif(self.side == "left"):
			ani_attack = self.ani_attack_left
		centro_alvo = rival.personagem.getAnchor()
		x_alvo = centro_alvo.getX()
		alvo_range = rival.personagem.getWidth()
		for ani in ani_attack:
				centro = self.personagem.getAnchor()
				x = centro.getX()
				if (self.fisica.colisao(x_alvo, alvo_range, x, 20)):
					self.alvo_pontos+=1
				if (self.fisica.colisao(x, 20, x_alvo, alvo_range)):
					self.alvo_pontos+=1
				self.personagem = self.personagem.reload_attack(self.win, ani)
				time.sleep(ratio_sleep)
				self.pontos += self.alvo_pontos/5



class Alvo(Personagem):
	def __init__(self, x, y, window, name, side):
		Personagem.__init__(self, x, y, window, name, side)