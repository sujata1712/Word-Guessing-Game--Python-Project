# import random
import random
# define a list of words
words=[
    'apple', 'banana', 'mango', 'jackfruit', 'cherry', 'orange', 'grape', 'avocado', 'papaya', 'plum', 'watermelon', 'pear', 'peach', 'kiwi', 'pineapple', 'strawberry', 
    'blueberry', 'blackberry', 'raspberry', 'pomegranate', 'fig', 'guava', 'coconut', 'lemon', 'lime', 'apricot', 'dragonfruit', 'lychee', 'cranberry', 'tangerine', 
    'mulberry', 'persimmon', 'starfruit', 'passionfruit', 'cantaloupe', 'honeydew'
]
guess_word=random.choice(words)
# print(guess_word)

# make a hint
hint=guess_word[0]+guess_word[-1]
# print(hint)

store=[]            # we crete an empty list to store the words which you will guess .
attemps=4
n=input('Enter your name: ')
print('----------------------------------------')
print(f'Welcome to the word game! {n}.\nIn this game, you have to guess the word.')
print(f'You have {attemps} attemps for gussing the word.')
print('----------------------------------------')

for guess in range(attemps):
    while True:
        letter=input('Guess the letter:')

        if len(letter)==1:
            break
        else:
            print('Please guess a letter.')
    

    if letter in guess_word:
        print('Yes.')
        store.append(letter)
    else:
        print('No.')

    
    if guess==3:
        hint_req=input('Are you want a hint?\nIf \'yes\' then enter \'y\' otherwise enter \'n\'.\n')
        if hint_req.lower()=='y':
            print(f'Hint: The first and last letter of the word is {hint}.')

        else:
            print('Okay, you\'re very confident.')


print(f'Let\'s see what you have guessed so far.\nYou\'ve guessed {len(store)} letters correctly.')
print('These correct letters are: ',store)

word_guess=input('Guess the whole word: ')
if word_guess.lower()==guess_word:
    print('Congrats! You\'re correct.')
else:
    print('Sorry! The correct word is ',guess_word)