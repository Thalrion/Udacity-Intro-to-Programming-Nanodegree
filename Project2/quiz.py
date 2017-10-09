# Feel free to use the interactive environment from trinket.io:
# https://trinket.io/python/cce59a9364

import sys  # sys package is used to exit when user is keeping using invalid choices
            # when hes asked for difficulty

# A list of replacement words to be passed in to the play game function.
gap_names  = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__", "__8__"]

# Easy text-string
blockchain_string_blanket = """A __1__ is a continuously growing list of records which are linked and secured using __2__. A blockchain can serve as an open, __3__ ledger. The biggest cryptocoin (by market capitalisation) based on blockchain is __4__. The second biggest cryptocoin-project is __5__.""" # Easy
blockchain_string = """A blockchain is a continuously growing list of records which are linked and secured using cryptography. A blockchain can serve as an open, distributed ledger. The biggest cryptocoin (by market capitalisation) based on blockchain is bitcoin. The second biggest cryptocoin-project is ethereum.""" # Easy

# medium text-string
web_string_blanket = """The __1__ opens a web browser. The user commands the __2__ to do something and the browser sends a signal over the __3__ ("the world's largest computer network"). __4__, an applications protocol, takes the signals and sends them to __5__ that host the __6__. The __7__ then send __8__ back along the chain of command.""" # Medium
web_string = """The user opens a web browser. The user commands the browser to do something and the browser sends a signal over the internet ("the world's largest computer network"). HTTP, an applications protocol, takes the signals and sends them to servers that host the content. The servers then send information back along the chain of command.""" # Medium

# superhard text-string
german_string_blanket = """Die deutsche Sprache ist doch super! Wir lieben es, alltaegliche Gegenstaende lange, aufwendige Namen zu geben. Wo die Welt einen pen sieht, sehen wir einen __1__ und wo Andere einen sanften butterfly sehen, kennen wir den Begriff nur unter __2__. Aber hey, wenigstens gibt es bei uns einen Begriff, um den Tag nach morgen zu bennenen: __3__ (Im englishen gibt es lediglich die Umschreibung "The day after tomorrow"). Achja.. deutsche Sprache, schoene __4__!""" # superhard
german_string = """Die deutsche Sprache ist doch super! Wir lieben es, alltaegliche Gegenstaende lange, aufwendige Namen zu geben. Wo die Welt einen pen sieht, sehen wir einen KUGELSCHREIBER und wo Andere einen sanften butterfly sehen, kennen wir den Begriff nur unter SCHMETTERLING. Aber hey, wenigstens gibt es bei uns einen Begriff, um den Tag nach morgen zu bennenen: UEBERMORGEN (Im englishen gibt es lediglich die Umschreibung "The day after tomorrow").Achja.. deutsche Sprache, schoene SPrache!""" # superhard

# to better access them later, i put all strings in one list
blanked_strings = [blockchain_string_blanket, web_string_blanket, german_string_blanket]
strings_list = [blockchain_string, web_string, german_string]
solution_list = [["blockchain", "cryptography", "distributed", "bitcoin", "ethereum"], # Easy
             ["user", "browser", "internet", "HTTP", "servers", "content", "servers", "information"], # Medium
             ["KUGELSCHREIBER", "SCHMETTERLING", "UEBERMORGEN", "SPRACHE"]] # Hard

# Checks if a word in gap_names is a substring of the word passed in.
def word_in_pos(word, gap_names):
    """ Check if inputted word is part of the gap-name-list

    Args:
        (str) A single word in gapped-text
        (list) List of gap names (like "__1__")
    Returns:
        (none) If both words dont match, it returns none
        (str) If both words match, it returns the word (i.e. the gap-name -like __1__)
    """
    for pos in gap_names:
        if pos in word:
            return pos
    return None

def difficulty():
    """ Asks the user for a difficulty-level

    Args:
        none.
    Returns:
        (int): Difficulty-level
    """
    print  "Choose a difficulty (easy / medium / superhard)!"
    trys = 3
    for retry in range(trys):
        user_input = raw_input("> ")
        if user_input == "easy":
            print "You have choosen " + user_input
            return 0
            break
        if user_input == "medium":
            print "You have choosen " + user_input
            return 1
            break
        if user_input == "superhard":
            print "You have choosen " + user_input
            print "ATTENTION: 'superhard' means a german fill-in-the-gap text! Good luck :)"
            return 2
            break
        print "Wrong submission. Trys left: " + str(trys - retry - 1)
    else:
        print "You keep making invalid choices, exiting."
        sys.exit(1)

def define_length(word, max_sol):
    """ Calculate the length of the middle column to define a dynamic table

    Args:
        (str) The solution-keyword
        (int) Length of the biggest solution-keyword inplay
    Returns:
        (int) Difference between length of biggest solution-keyword and length of
              asked solution-keyword
    """
    len_word = len(word)
    difference = max_sol - len_word
    return difference

def pretty_solution(gap_names, solution, guesses):

    """ Print out a pretty game-summary-table

    Args:
        (list) List of all gap names (like __1__, __2__ etc.)
        (list) List of solution-keywords of the choosen difficulty-level
        (list) List of guesses-counts recorded while playing
    Returns:
        (str) A summary displaying the solution to each gap + number of counts
        (str) Text asking player to try again
    """

    length = len(solution)
    len_max_sol = max(len(w) for w in solution)
    len_sol = len("Solution") + 2
    if len_max_sol < len_sol:
        len_multiply = 1
    else:
        len_multiply = define_length("solution", len_max_sol)
    index = 0
    print
    print " "* 5 + "Gap  | Solution " + " "* len_multiply  +   "| Guesses"
    while index < length:
        print " " * 4 + gap_names[index] + " | " + solution[index] + " "* define_length(solution[index], len_max_sol) + " | " + str(guesses[index])
        index += 1
    print
    return "Congrats! Try again :)"

def copy_paragraph(difficulty_index, counter_paragraph):
    """ Print the paragraph with correct replaced answer

    Args:
        (int) Difficulty_index that the player choosed at the start of the game
        (int) Counter_paragraph thats been ingremented while playing everytime
              the for-loop in "play_quiz()" loops over a new word
    Returns:
        (str) Text string containing the whole paragraph up to the right answered word
    """
    text_string = strings_list[difficulty_index]
    text_string_as_list = text_string.split(" ")
    text_paragraph_as_list = text_string_as_list[:counter_paragraph]
    text_paragraph_as_string = " ".join(text_paragraph_as_list)
    return text_paragraph_as_string

def ask_for_trys():
    """ Ask the player how many trys he want to have per answer

    Args:
        None.
    Returns:
        (int) Number of trys selected
    """
    while True:
        try:
            trys = int(raw_input("How many trys do you want to have per answer?: > "))
            return trys
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


def check_answers(difficulty_index, trys, blanked_text, guesses,solution):
    """ Ask and check user-answers and increment all counters if neccessary

    Args:
        (int) Difficulty_index that the player choosed at the start of the game
        (int) Number of trys selected
        (str) The whole text with gaps according to the choosen difficulty-level
        (list) A list containing only "0" equal to the number of solutions inplay
        (list) A list containing all solutions according to the choosen difficulty-level
    Returns:
        (list) A filled list of counted guesses per answer
    """
    index, counter_paragraph = 0, 0
    for word in blanked_text:
        counter_paragraph +=1
        # word_in_pos()-function is been called to look if the word in the
        # blanked_text-list equals something like "__1__" etc.)
        answer = word_in_pos(word, gap_names)
        # Everytime, a blanked (like __1__ etc.) is been found in the text,
        # the user is asked to take a guess.
        if answer != None:
            counter = 0
            # This nested for loop checks if they are any trys left before
            # the game continous.
            for retry in range(trys):
                user_input = raw_input("Fill in the gap: " + answer + ": > ")
                if user_input == solution[index]:
                    # If user input is correct, it breaks the nested for loop
                    # and continue with the first for loop.
                    print copy_paragraph(difficulty_index, counter_paragraph)
                    counter +=1
                    guesses[index] = counter
                    index += 1
                    break
                else:
                    # If answer is incorrect, the game displays how many
                    # trys are left for this answer.
                    # If they are no trys left, it breaks the nested for loop
                    # and continue with the first for loop.
                    print "Incorrect Answer. Trys left: " + str(trys - retry - 1)
                    counter += 1
                    if retry == trys - 1:
                        print "You have no trys left for gap " + str(index) + ". Please try to fill in the next gap:"
                        guesses[index] = counter
                        index += 1
                if index == len(solution):
                    # If index equals the lenght of the solution-list, the
                    # game stops
                    break
    return guesses

def play_quiz(gap_names):
    """ Start the game and call the appropiate functions

    Args:
        (list) List of all gap names (like __1__, __2__ etc.)
    Returns:
        (str) Message showing the solution of the game

    """
    # At the start, the game calls the difficulty()-function.
    # The function returns an integer between 0 and 2, determining
    # the choosen level.
    difficulty_index = difficulty()
    blanked_text = str(blanked_strings[difficulty_index])
    solution = solution_list[difficulty_index]

    trys = ask_for_trys()

    # After user chooses difficulty-level, the game displays the text with
    # blankets.

    print "Here is your text with gaps:"
    print blanked_text.strip('[]')

    # The text is been splitted into a list so the function can loop
    # through it.
    blanked_text = blanked_text.split()
    guesses = ["0"]*len(solution)

    check_answers(difficulty_index, trys, blanked_text, guesses, solution)

    print "Here is the solution:"
    return pretty_solution(gap_names, solution, guesses)

print play_quiz(gap_names)
