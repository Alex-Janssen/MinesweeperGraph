import random
from collections import defaultdict
import numpy as np
from PIL import Image
import math

class board:
	def __init__(self, origin, probability):
		self.origin = origin #tuple positions
		self.board = defaultdict(lambda: -1)
		self.board[origin] = 1
		self.queue = []
		self.queue.append(origin)
		self.probability = probability
	def empty_neighbors(self, p):
		#Returns empty neighbors of a position
		neighbor_list = []
		if self.board[(p[0]-1,p[1])] == -1:
			neighbor_list.append((p[0]-1,p[1]))
		if self.board[(p[0]+1,p[1])] == -1:
			neighbor_list.append((p[0]+1,p[1]))		
		if self.board[(p[0],p[1]-1)] == -1:
			neighbor_list.append((p[0],p[1]-1))
		if self.board[(p[0],p[1]+1)] == -1:
			neighbor_list.append((p[0],p[1]+1))
		return neighbor_list
	def cycle(self):
		#Cycles through neighbors
		new_queue = []
		for p in self.queue:
			neighs = self.empty_neighbors(p)
			for n in neighs:
				if random.random() < self.probability: #then activate and add to queue
					self.board[n] = 1
					new_queue.append(n) #add n to queue
				else:
					self.board[n] = 0
		self.queue = new_queue
class knight_board(board):
	def __init__(self, origin, probability):
		super().__init__(origin,probability)
	def empty_neighbors(self,p):
		#Returns empty neighbors of a position
		neighbor_list = []
		if self.board[(p[0]-2,p[1]-1)] == -1:
			neighbor_list.append((p[0]-2,p[1]-1))
		if self.board[(p[0]-2,p[1]+1)] == -1:
			neighbor_list.append((p[0]-2,p[1]+1))
		if self.board[(p[0]+2,p[1]-1)] == -1:
			neighbor_list.append((p[0]+2,p[1]-1))
		if self.board[(p[0]+2,p[1]+1)] == -1:
			neighbor_list.append((p[0]+2,p[1]+1))
		if self.board[(p[0]-1,p[1]-2)] == -1:
			neighbor_list.append((p[0]-1,p[1]-2))
		if self.board[(p[0]-1,p[1]+2)] == -1:
			neighbor_list.append((p[0]-1,p[1]+2))
		if self.board[(p[0]+1,p[1]-2)] == -1:
			neighbor_list.append((p[0]+1,p[1]-2))
		if self.board[(p[0]+1,p[1]+2)] == -1:
			neighbor_list.append((p[0]+1,p[1]+2))
		return neighbor_list		


#B = board((0,0), .59125)
B = knight_board((0,0), .27)
while len(B.queue)> 0:
	B.cycle()

pic_array = []
min_x = float(math.inf)
max_x = -float(math.inf)
min_y = float(math.inf)
max_y = -float(math.inf)
#color_losers = True

for b in B.board.keys():
	if b[0] > max_x:
		max_x = b[0]
	if b[0] < min_x:
		min_x = b[0]
	if b[1] > max_y:
		max_y = b[1]
	if b[1] < min_y:
		min_y = b[1]        
for y in range(max_y - min_y + 1):
	pic_array.append([])
	for x in range(max_x - min_x + 1):
		if B.board[x  + min_x, y  + min_y] == 1:
			pic_array[y].append(0)
		#elif color_losers and B.board[x  + min_x, y  + min_y] == -1 and random.random() < B.probability:
			#pic_array[y].append(150)
		else:
			pic_array[y].append(255)

pic_array = np.uint8(np.array(pic_array))
pic = Image.fromarray(pic_array, mode = "L")
pic.save("aleatory_process.png")
print("Done!")
                        

