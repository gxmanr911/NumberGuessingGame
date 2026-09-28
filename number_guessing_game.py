# Simple Number Guessing Game
from random import randint
from os import remove
class game():
	def play_round():
		max_num=10
		attempts = 3
		secret_number = randint(1,max_num)

		print(f"\nI am thinking of a number from 1 to {max_num}. 🤖")
		print(f"You have {attempts} attempts.")

		while attempts > 0:
			guess = int(input(f"Enter your guess, {attempts-attempts}: "))

			if guess == secret_number:
				print("Correct! I'm proud of you son! 👍")
				return max_num/attempts

			elif guess < secret_number:
				print("Too low! ❄️")

			else:
				print("Too high! 🔥")

			attempts = attempts - 1

		print("You ran out of attempts. I am very disapointed in you! 💀")
		print("The number was", secret_number, "🙄")

		return 0


	def show_stats(score, wins, rounds):
		print("\n--- PLAYER STATS ---")
		print("Score:", score)
		print("Wins:", wins)
		print("Rounds Played:", rounds)


	def main():
		if file.init():
			score = file.load_score()
			wins = file.load_wins()
			rounds = file.load_rounds()
			game.show_stats(score, wins, rounds)
			userin=input("make new file[y/n]:")
			if userin=="y" or userin=="":
				remove(file.file_name)
				score = 0
				wins = 0
				rounds = 0
		else:
			score = 0
			wins = 0
			rounds = 0
		playing = True

		print("NUMBER GUESSING GAME 🤠")

		while playing:
			points = game.play_round()

			# Update player statistics
			score = score + points
			rounds = rounds + 1

			if points > 0:
				wins = wins + 1

			game.show_stats(score, wins, rounds)
			file.save(score, wins, rounds)
			again = input("\nPlay another round? (yes/no) 🥺: ")

			if again.lower() != "yes" and again.lower() != "y" and again.lower() != "":
				playing = False

		print("\nGAME OVER 👻")
		game.show_stats(score, wins, rounds)

	
class file():
	file_name="irish_save_file.txt"
	def init():
		try:
			open(file.file_name,'x')
			return False
		except:
			return True
	def save(score,win,rounds):
		with open(file.file_name,'w') as f:
			f.write(f'{score},{win},{rounds}')
	def load_score():
		with open(file.file_name,'r') as f:
			text=f.read()
		x=text.split(',')
		return int(x[0])
	def load_wins():
		with open(file.file_name,'r') as f:
			text=f.read()
		x=text.split(',')
		return int(x[1])
	def load_rounds():
		with open(file.file_name,'r') as f:
			text=f.read()
		x=text.split(',')

		return int(x[2])

if __name__=='__main__':
	game.main()
