from graphics import *
from personagem import *	
from random import randint
import time

def main():
	win = GraphWin("GAME", 1024, 614, autoflush=False)
	fundo = Image(Point(512,307), "background.gif")
	fundo.draw(win)
	jogador = Player(155,495,win, "jogador", "right")
	alvo = Alvo(869,475,win,"alvo", "right")
	pontos = Text(Point(980, 40), "")
	pontos.draw(win)
	pontos.setTextColor("white")
	pontos.setSize(30)
	vidas = Text(Point(40, 40), "")
	vidas.draw(win)
	vidas.setTextColor("red")
	vidas.setSize(30)
	vida = 15
	vel = 0.2
	while (True):
		if (vida == 0):
			break;
		jogador.update(win.checkKey(),alvo, vel, 1)
		pontos.setText(jogador.pontos)
		vidas.setText(vida)
		if (jogador.result or jogador.contador > 2500):	
			if (jogador.pontos<=20):
				if (jogador.contador > 2500):
					vida-=1
				jogador.contador = 0
				random = randint(1,1024)
				alvo.personagem.undraw()
				alvo.draw(random, 475, "Right") 
				if (vel <= 0.1): 
					vel = vel-0.0005
				if (vel <= 0.02):
					vel = 0.02
				else:
					vel = vel-0.001	
			else:
				if (jogador.contador > 2500):
					vida-=1
				jogador.contador = 0
				random = randint(1,1024)
				alvo.personagem.undraw()
				alvo.draw(random, 475, "Left")
				if (vel <= 0.1): 
					vel = vel-0.001
				if (vel <= 0.02):
					vel = 0.02
				else:
					vel = vel-0.01	

		win.update()	
	fundo = Image(Point(512,307), "defeat.gif")
	fundo.draw(win)
	pontos = Text(Point(512, 490), "")
	pontos.draw(win)
	pontos.setTextColor("green")
	pontos.setSize(30)
	pontos.setText(jogador.pontos)
	win.getMouse()

main()
