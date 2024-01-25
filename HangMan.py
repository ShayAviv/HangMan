HANGMAN_ASCII_ART = r"""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""
MAX_TRIES = 6
name = input('Please enter your name : ')
HANGMAN_PHOTOS = {
0: """
x-------x""",
1: """
x-------x
|
|
|
|
|""",
2: """
x-------x
|       |
|       0
|
|
|""",
3: """
x-------x
|       |
|       0
|       |
|
|""",
4: """
x-------x
|       |
|       0
|      /|\ 
|
|""",
5: """
x-------x
|       |
|       0
|      /|\ 
|      /
|""",
6: """
x-------x
|       |
|       0
|      /|\ 
|      / \ 
|"""}





def open_screen():
    print(f'{HANGMAN_ASCII_ART}\nHello sir {name},your number of tries : {MAX_TRIES}')
    print('Shay Aviv\'s design: bold, creative, balanced.')


def choose_word(file_path, index):
    with open(file_path, 'r') as words:
        words_data = words.read()
        words_list = words_data.split(' ')
        if index > len(words_list):
            index = 1
        chosen_word = words_list[index - 1].replace('\n', '')
        return chosen_word


def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) != 1:
        print("That is not a one letter, you little cheater!")
        return False
    elif not letter_guessed.isalpha():
        print("Think you are a smartie? That's not an English letter.")
        return False
    elif letter_guessed.lower() in old_letters_guessed:
        print("You already guessed that letter.")
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
    global num_of_tries

    if not check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.sort()
        print(" -> ".join(old_letters_guessed))
    else:
        if letter_guessed.lower() not in secret_word:
            old_letters_guessed.append(letter_guessed.lower())
            num_of_tries += 1
            print(':(')
            print(print_status(num_of_tries))
            print(show_hidden_word(secret_word, old_letters_guessed))
        else:
            old_letters_guessed.append(letter_guessed.lower())
            print(show_hidden_word(secret_word, old_letters_guessed))




def show_hidden_word(secret_word, old_letters_guessed):
    correct_guess = ['']
    for letter in secret_word:
        if letter in old_letters_guessed:
            correct_guess.append(letter + " ")
        else:
            correct_guess.append("_ ")
        result = ''.join(correct_guess)
    return result



def check_win(secret_word, old_letters_guessed):
    if ''.join(show_hidden_word(secret_word, old_letters_guessed).split()) in secret_word:
        print(f'Congratulations!\nLooks like master {name} is our new akinator !!!')
        return True
    return False


def word_len(secret_word):
    return '_ ' * len(secret_word)


def print_status(num_of_tries):
    return (HANGMAN_PHOTOS[num_of_tries])


num_of_tries = 0


def main():
    open_screen()
    global num_of_tries
    secret_word = choose_word(input(r"Please enter file path: ").lower(), int(input(r"Please choose an index: ")))
    old_letters_guessed = []
    print(f'Lets start sir {name} !')
    print(HANGMAN_PHOTOS[num_of_tries])
    print(word_len(secret_word))
    while num_of_tries < MAX_TRIES:
        try_update_letter_guessed(input(f'{name} Please enter a letter: '), old_letters_guessed, secret_word)
        print(f'You have {MAX_TRIES - num_of_tries} tries left.')
        show_hidden_word(secret_word, old_letters_guessed)
        game_status = check_win(secret_word, old_letters_guessed)
        if game_status:
            break
    if not game_status:
        print('GAME OVER!')
        print(f'the word was {secret_word}')

    nextgame = input('Do you want to keep playing? \nPress 1 to continue and 2 to end game ')
    if nextgame == '1':
        main()
    else:
        print(f'It was nice until it was over Mr.{name} ')


if __name__ == "__main__":
    main()
