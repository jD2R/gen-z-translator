import time


def generateDictionaries(d):
	dict, defDict = {}, {}
	file = open(d)

	for line in file:
		new = line.replace('\n', '').split('/')
		dict[new[0].lower()] = new[1].lower()
		defDict[new[0].lower()] = new[2].lower()

	file.close()

	return dict, defDict


def menu(question, choices):

	while True:
		for i in range(1, len(choices) + 1):
			print(f"{i}: {choices[i]}")

		x = input(question)

		if x.isdigit():
			if int(x) in range(1, len(choices) + 1):
				return int(x)
			else:
				print(f"Enter number between {1} and {len(choices+1)}")
		else:
			print(f"input must be an integer")

	raise Exception("warning - menuError")


def translator(dic, defDict, slangCount):

	s = input("Insert your Gen-Z sentence here:\n\n")

	print("\nScanning input text.", end="")
	for i in range(2):
		time.sleep(1)
		print(".", end="")

	print("\n\nAttempting to parse Gen-Z text:")
	print("-" * 20)
	wordsL = s.split()
	for key in dic.keys():
		# print(dic.keys())
		for i in range(0, len(wordsL)):
			if wordsL[i].lower() == key.lower():
				# print("\nkey found:",key)
				# print("value:", dic[key])
				print(
				 f"word {i+1} ({wordsL[i]}) is a slang word, consider changing this word:")
				print(f"definition of {wordsL[i]}: {defDict[key]}")
				wordsL[i] = dic[key]
				slangCount += 1

	output = " ".join(wordsL).strip()
	print("-" * 20)
	print("Attempting to translate Gen-Z slang...")

	print(f"\n\033[1m\033[91mTranslation: \"{output}\"\033[0m")

	print('\n# of Gen-Z slang words found: ', slangCount)

	return


def main():

	# initalize crucial objects
	dic, defDict = generateDictionaries("gen-z-dict.txt")
	slangCount = 0

	print('''
█▀▀ █▀▀ █▄░█ ▄▄ ▀█   ▀█▀ █▀█ ▄▀█ █▄░█ █▀ █░░ ▄▀█ ▀█▀ █▀█ █▀█
█▄█ ██▄ █░▀█ ░░ █▄   ░█░ █▀▄ █▀█ █░▀█ ▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄
	''')
	print("-" * 40)
	print("Welcome to the Gen-Z translator!\n")
	print(
	 "Our mission is to make it easier for you old folk to understand our language.\nSimply insert some text and our program will attempt to identify and translate any gen-z slang words for you!\n\nHow does our program fit this year's theme? Glad you asked!\nChange can be a good thing, but many times it can be a bad thing as well. Take for example the language gap between generations.\nUsing tools like this, you can understand what we say - bridging the gap and bringing us closer together.\n\nWhy not have a go?\n\n"
	)

	# choices = ["Display translation index","Edit translation index","Translate sentence"]

	# match menu(choices,"Enter choice: "):
	# 	case 1:
	# 		print("placeholder")
	# 	case 2:
	# 		print("placeholder")
	# 	case 3:
	translator(dic, defDict, slangCount)


main()
