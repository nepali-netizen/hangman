import random
import os
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = "abruptly absurd abyss affix askew avenue awkward axiom azure bagpipes bandwagon banjo bayou beekeeper bikini blitz blizzard boggle bookworm boxcar boxful buckaroo buffalo buffoon buxom buzzard buzzing buzzwords caliph cobweb cockiness croquet crypt curacao cycle daiquiri dirndl disavow dizzying duplex dwarves embezzle equip espionage euouae exodus faking fishhook fixable fjord flapjack flopping fluffiness flyby foxglove frazzled frizzled fuchsia funny gabby galaxy galvanize gazebo giaour gizmo glowworm glyph gnarly gnostic gossip grogginess haiku haphazard hyphen iatrogenic icebox injury ivory ivy jackpot jaundice jawbreaker jaywalk jazziest jazzy jelly jigsaw jinx jockey jogging joking jovial joyful juicy jukebox jumbo kayak kazoo keyhole khaki kilobyte kiosk kitsch kiwifruit klutz knapsack larynx lengths lucky luxury lymph marquis matrix megahertz microwave mnemonic mystify naphtha nightclub nowadays numbskull nymph onyx ovary oxidize oxygen pajama peekaboo phlegm pixel pizazz pneumonia polka pshaw psyche puppy puzzling quartz queue quips quixotic quiz quizzes quorum razzmatazz rhubarb rhythm rickshaw schnapps scratch shiv snazzy sphynx spritz squawk staff strength strengths stretch stronghold"
data = words.split(" ")
total_data = len(data)
word = data[random.randint(0,total_data-1)]
# print(word)
print('\n')
#Display dashes :
dash = []
for i in range(0,len(word)):
    dash += '_'

#Replace guess word in dash :
win = False
loss_counter = 0
guesses = ''
print("WELCOME TO HANGMAN\n")
while not win:
    print(f"{len(dash)} letter word : \n")
    print(*dash)
    print("\n")
    print(hangman[6-loss_counter])
    guess = input("Enter guess letter : ")
    guesses += guess
    print(guesses)
    print('\n')
    
    wrong = True
    for i in range(0,len(word)):
        if word[i] == guess:
            dash[i] = guess
            wrong = False
    
    if wrong == True:
        loss_counter += 1
    
    
    count = 0
    for i in range(0,len(dash)):
        if dash[i] == '_':
            count += 1


    if count == 0:
        print("\n-----'YOU WIN'-----\n")
        win = True
    elif loss_counter == 6:
        print("\n-----'YOU LOSE'-----\n")
        print(f"The word was {word}")
        win = True