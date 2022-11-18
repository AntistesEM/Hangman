import random
word_list = ['цифра', 'характер', 'новость', 'практика', 'круг', 'возвращение',
             'студент', 'золото', 'момент', 'государство']

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def get_word():
    return random.choice(word_list).upper()

def play(word):
    word_completion = '_' * len(word)  
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print('Давайте играть в угадайку слов!')
    print(display_hangman(6))
    print(word)
    print(word_completion, f'В слове {len(word)} букв')
    while tries != 0:
        letter = input('Введите букву или слово целиком: ').upper() 
        if len(letter) == 1 and 1040 <= ord(letter) <= 1071:
            if letter in guessed_letters:
                print('Вы уже вводили данную букву!') 
                continue
            else:
                guessed_letters += letter  
        elif len(letter) > 1 and len(letter) == len(word) and letter.isalpha():           
            if letter == word:
                return f'Поздравляем, вы угадали слово: {word}! Вы победили!'
            elif letter in guessed_words:
                print('Вы уже вводили данное слово!')
                continue                
            else:
                guessed_words.append(letter)                
        else:
            print('Введеные данные не являются буквой или корректным словом.')
            continue 
        if letter in word:             
            for i in range(len(word)):                
                if letter == word[i]:
                    word_completion = word_completion[:i] + letter + word_completion[i + 1:]    
                if word_completion == word:
                    return f'Поздравляем, вы угадали слово: {word}! Вы победили!'
            print(word_completion)
        elif letter not in word or letter != word:
            tries -= 1
            if tries == 0:
                print(display_hangman(tries))
                return f'Вы исчерпали все свои попытки! Загаданное слово: {word}'
            else:
                print(display_hangman(tries))                    

while True:
    print(play(get_word()))
    answer = input('Желаете продолжить? (да/нет): ')
    if answer == 'да':
        continue
    if answer == 'нет':
        print('До новых встреч!')
        break

    