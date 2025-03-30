from random import randint

def game():
	while True:
		#a = "Game kéo búa bao"
		#b = a.center(50)
		row_1 = '+ {:-<6} + {:-^16} + {:->6} +'.format('','','')
		row_2 = '| {:-<6} | {:-^16} | {:->6} |'.format( '','' ,'' )
		row_3 = '| {:-<6} | {:-^15} | {:->6} |'.format( '', 'GAME KEO BUA BAO' , '')
		row_4 = '| {:-<6} | {:-^16} | {:->6} |'.format( '', '', '')
		row_5 = '+ {:-<6} + {:-^16} + {:->6} +'.format('','','')
		print("\n")
		print(row_1)
		print(row_2)
		print(row_3)
		print(row_4)
		print(row_5)

		print("\n        want out game write 'stop'")
		row_6 = '* {:-<6} | {:-^10} | {:->6} *'.format('', ' bua, bao, keo', '')
		print(row_6)

		press = input("\nPress Enter to star game ")

		if press == "":
			player = input("\nEnter your choose: ")
			computer = randint(1,3)
			if "stop" in player :
				print("see ya")
				break	

			if computer == 1:
				computer = "búa"
			if computer == 2:
				computer = "bao"
			if computer == 3:
				computer = "kéo"

			print("___")
			print("your choose: " + player)
			print("computer choose: " + str(computer))
			print("___")

			if player == computer:
				print("draw")

			else :
				if "kéo" in player:
					if computer == "búa":
						print("loser")
					else: 
						print("win")
							
				elif "búa" in player:
					if computer == "kéo":
						print("win")
					else: print("loser")
					
				elif "bao" in player:
					if computer == "kéo":
						print("loser")
					else: print("win")
		else:
			print("see ya")
value = game()
print(value)

		