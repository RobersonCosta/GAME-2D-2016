class Fisica:
	def __init__ (self, x, y):
		self.x = x
		self.y = y

	def limite (self, ani):
		centro_ani = ani.getAnchor()
		area_ani_left = centro_ani.getX()-ani.getWidth()/2
		area_ani_right = centro_ani.getX()+ani.getWidth()/2
		if (area_ani_left<10):
			return "Left"
		elif(area_ani_right>self.x):
		     return "Right"

	def colisao(self, x_obj, obj_range, x_alvo, alvo_range):
		if ((((x_obj+obj_range) or (x_obj-obj_range)) <= (x_alvo+alvo_range)) and (((x_obj+obj_range) or (x_obj-obj_range)) >= (x_alvo-alvo_range))):
			return True
		else:
			return False