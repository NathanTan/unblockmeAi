#!/bin/python3




class Game:
	def __init__(self):
		self.boardHeight = 6
		self.boardWidth = 6
		self.board = [[0] * 6] * 6



	def printBoard(self):
		for row in self.board:
			print(row)


	def initializeBoard(self):
		for x in range(0, self.boardHeight - 1):
			print(str(x))
			for y in range(0, self.boardWidth - 1):
				print(str(y))
				self.board[self.boardHeight][self.boardWidth].append("X")						


class Puzzle:
	def __init__(self):
		self.boardHeight = 6
		self.boardWidth = 6
		self.board = [[0] * 6] * 6



	# For the end of the puzzle blocks use top/bottom left/right to indicate the ends of the blocks
	def loadTestPuzzle(self):
		print("TODO")






if __name__ == '__main__':

	print("hello world")
	game = Game()
	game.printBoard()
	



