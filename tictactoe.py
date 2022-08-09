#Tic-Tac-Toe

import pprint, random

theBoard = {
	'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
	'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
	'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
} 

def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] )
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def userMove(move):
	if theBoard[move] == ' ':
		theBoard[move] = 'X'
	
	

print('Lets flip a coin to see who goes first')
coin = random.randint(1,2)
print('Select 1 for Heads or 2: for Tails')

print('DEBUG: coin is: ' +str(coin))


guess = int(input())
if guess == coin:
	turn = 'X'
	print('Darn you guessed correct.')
	print('You go first.')
else:
	turn = 'O'
	print('Sorry, you guessed wrong.')
	print('''I'll go first.''')


printBoard(theBoard)
for i in range(9):
	if turn == 'X':
		print('make a move (top-, mid-, low- & L, M, R)')
		#take input
		move = input()
		# add x
		userMove(move)
		printBoard(theBoard)
