import random



def remove_word(word):
    global word_list
    global choose_from
    for i in range(len(word_list)):
        if word_list[i].strip().upper() == word:
            l = word_list.pop(i)
            print(f"'{l.strip()}' is removed")
            break
    if choose_from == '1':
        with open("animals.txt", 'w') as file:
            file.write(''.join(word_list))
    elif choose_from=='2':
        with open("dictionary.txt", 'w') as file:
            file.write(''.join(word_list))



header = """
This is a game to guess the word
choose which one you want to guess
1. animals
2. dictionary
"""
print(header)

choose_from = input("enter: ")
while choose_from not in ['1','2']:
    print('invalid choice !!')
    choose_from = input("enter: ")

if choose_from == '1':
    with open("animals.txt", 'r') as file:
        word_list = file.readlines()
elif choose_from=='2':
    with open("dictionary.txt", 'r') as file:
        word_list = file.readlines()



while True:
    word = random.choice(word_list).strip().upper()
    hint = ['-']*len(word)
    while hint.count('-')>0:
        print('\n',''.join(hint))
        guess = input('Guess the word : ').upper()
        if len(guess)==1:
            if guess in word:
                for w in range(len(word)):
                    if word[w] == guess:
                        hint[w] = guess
            else :
                print(f"the letter '{guess}' is not in the word")
        else:
            if guess == word:
                print("YOU WIN !!!!")
                # rm = input("do you want to remove this word(y/n): ")
                # if rm.lower()=='y':
                #     remove_word(word)
                print()
                break
            else:
                print(f"the word '{guess}' is incorrect")
            
        if hint.count('-')==0 and guess != word:
            print("Sorry you LOSE !!")
            print((f"the word was {word}"))
            rm = input("do you want to remove this word(y/n): ")
            if rm.lower()=='y':
                remove_word(word)
            print()
            break
    play = input("\nDo you want to play again?(y/n): ")
    if play.lower() == 'n':
        quit()
