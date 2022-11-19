#Hangman Game!
import random
import os

hangman1 = """
-----
"""

hangman2 = """ 
|     
|     
|   
|    
|  
|
-----
"""

hangman3 = """ 
-------
|     
|   
|   
|   
|    
|
-----
"""

hangman4 = """
-------
|     |
|     
|   
|     
|    
|
-----
"""

hangman5 = """
-------
|     |
|     0 
|   
|     
|    
|
-----
"""

hangman6 = """
-------
|     |
|     0 
|     |
|     |
|    
|
-----
"""

hangman7 = """
-------
|     |
|     0 
|   --|
|     |
|    
|
-----
"""

hangman8 = """
-------
|     |
|     0 
|   --|--
|     |
|     
|
-----
"""

hangman9 = """
-------
|     |
|     0 
|   --|--
|     |
|    / 
|
-----
"""

hangman10 = """
-------
|     |
|     0 
|   --|--
|     |
|    / \ 
|
-----
"""

while True:

    os.system('clear')
    print("Hangman Game by Pablo!\n")

    words = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"]

    hangman = [hangman1, hangman2, hangman3, hangman4, hangman5, hangman6, hangman7, hangman8, hangman9, hangman10]

    secret_word = list(random.choice(words))

    possible_guesses = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    guesses = []
    correct_guesses = []
    incorrect_guesses = []

    tries = 0

    for letter in secret_word:
        correct_guesses.append(" ")

    for letter in secret_word:
        print("_", end = ' ')
    print("\n")    

    while correct_guesses != secret_word: 
        
        guess = str(input("\nGuess a letter: "))
        os.system('clear')
        
        if guess not in possible_guesses:
            print("Invalid guess, try again!\n")
            print("Incorrect guesses: ", ", ".join(incorrect_guesses))
            print("Tries: " + str(tries), "\n")
            print(" ".join(correct_guesses))
            for letter in secret_word:
                print("_", end = ' ')
            print("\n")
            if incorrect_guesses != []:
                print(hangman[len(incorrect_guesses)-1])
            
        elif guess not in secret_word:
            print("Incorrect guess!\n")
            tries += 1
            guesses.append(guess)
            incorrect_guesses.append(guess)
            possible_guesses.remove(guess)
            print("Incorrect guesses: ", ", ".join(incorrect_guesses))
            print("Tries: " + str(tries), "\n")
            print(" ".join(correct_guesses))
            for letter in secret_word:
                print("_", end = ' ')
            print("\n")        
            print(hangman[len(incorrect_guesses)-1])
            
        elif guess in secret_word:
            print("Correct guess!")
            tries += 1
            guesses.append(guess)
            secret_word_pos = secret_word.index(guess)
            secret_word_num = secret_word.count(guess)
            if secret_word_num >= 2: 
                start_at = -1
                for i in range(secret_word_num):
                     try:
                        secret_word_pos = secret_word.index(guess, start_at+1)
                     except ValueError:
                          break
                     else:
                         correct_guesses.pop(secret_word_pos)
                         correct_guesses.insert(secret_word_pos, guess)
                         start_at = secret_word_pos
            else:    
                correct_guesses.pop(secret_word_pos)
                correct_guesses.insert(secret_word_pos, guess)        
            possible_guesses.remove(guess)
            print("\nIncorrect guesses: ", ", ".join(incorrect_guesses))
            print("Tries: " + str(tries), "\n")
            print(" ".join(correct_guesses))
            for letter in secret_word:
                print("_", end = ' ')
            print("\n")    
            if incorrect_guesses != []:
                print(hangman[len(incorrect_guesses)-1])
            
        if len(incorrect_guesses) >= 10:
            print("\nYou lose!")
            print("The secret word was: ", "".join(secret_word))
            replay = input("\nDo you want to play again? y/n: ")
            if replay == "y":
                break
            elif replay == "n":
                print("\nThanks for playing!")
                quit()
            else:
                print("\nYeet!")
                quit()
            
    if correct_guesses == secret_word:
        print("You win!")
        replay = input("\nDo you want to play again? y/n: ")
        if replay == "y":
            print("\n")
            continue
        elif replay == "n":
            print("\nThanks for playing!")
            break
        else:
            print("\nYeet!")
            break