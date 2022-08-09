#Tic-Tac-Toe

#import pprint, random

#theBoard = {
#	'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#	'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#	'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
#} 

#def printBoard(board):
#	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] )
#	print('-+-+-')
#	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#	print('-+-+-')
#	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

#def userMove(move):
#	if theBoard[move] == ' ':
#		theBoard[move] = 'X'
	
	

#print('Lets flip a coin to see who goes first')
#coin = random.randint(1,2)
#print('Select 1 for Heads or 2: for Tails')

#print('DEBUG: coin is: ' +str(coin))


#guess = int(input())
#if guess == coin:
#	turn = 'X'
#	print('Darn you guessed correct.')
#	print('You go first.')
#else:
#	turn = 'O'
#	print('Sorry, you guessed wrong.')
#	print('''I'll go first.''')


#printBoard(theBoard)
#for i in range(9):
#	if turn == 'X':
#		print('make a move (top-, mid-, low- & L, M, R)')
#		#take input
#		move = input()
#		# add x
#		userMove(move)
#		printBoard(theBoard)

#sudo code 
# board
# display Board
# start game
# check win
	#check rows
	#check columns
	#check diagonals
# check tie
# togle player turn 


#---------Global Vars----------------
gameIsStillGoing = True
winner = None

#whos turn is it
currentPlayer = 'X'

#board
board = {
	'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
	'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
	'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
} 

#display board
def displayBoard():
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] )
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

#play game
def playGame():
	displayBoard()
	while gameIsStillGoing:
		handleTurn(currentPlayer)
		checkGameOver()
		changeTurn()

	#game has ended
	if winner == 'X' or winner == 'O':
		print(winner + 'won!!!')
	elif winner == None:
		print('Game has ended in a draw...')


def handleTurn(player):
	position = input('make a move (top-, mid-, low- & L, M, R): ')
	board[position] = 'X'
	displayBoard()

def checkGameOver():
	checkForWinner()
	checkTie()

def checkForWinner():
	#set global variables
	global winer

	#check rows
	rowWinner = checkRows()
	#check columns
	columnWinner = checkColumns()
	#check diagonals
	diagonalsWinner = checkDiagonals()

	if rowWinner:
		winner = rowWinner
	elif columnWinner:
		winner = columnWinner
	elif diagonalsWinner:
		winner = diagonalsWinner
	return 

def checkRows():
	global gameIsStillGoing
	row1 = board['top-L'] == board['top-M'] == board['top-R'] != ' '
	row2 = board['mid-L'] == board['mid-M'] == board['mid-R'] != ' '
	row3 = board['low-L'] == board['low-M'] == board['low-R'] != ' '

	if row1 or row2 or row3:
		gameIsStillGoing = false
	if row1:
		return board['top-L']
	elif row2:
		return board['mid-L']
	elif row3:
		return board['low-L']
	return

def checkColumns():
	global gameIsStillGoing
	column1 = board[] == board[3] == board[6] != ' '
	column2 = board[1] == board[4] == board[7] != ' '
	column3 = board[2] == board[5] == board[8] != ' '

	if column1 or column2 or column3:
		gameIsStillGoing = false
	if column1:
		return board[0]
	elif column2:
		return board[1]
	elif column3:
		return board[2]
	return

def checkDiagonals():
	global gameIsStillGoing
	diagonal1 = board[0] == board[4] == board[8] != ' '
	diagonal2 = board[6] == board[4] == board[2] != ' '

	if column1 or column2 or column3:
		gameIsStillGoing = false
	if diagonal1:
		return board[0]
	elif diagonal2:
		return board[6]
	return

def changeTurn():
	return

def checkTie():
	return

def changTurn():
	return



#the game
playGame()

