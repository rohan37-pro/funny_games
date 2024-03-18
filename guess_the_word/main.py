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
        with open("word_list/animals.txt", 'w') as file:
            file.write(''.join(word_list))
    elif choose_from=='2':
        with open("word_list/flowers.txt", 'w') as file:
            file.write(''.join(word_list))
    elif choose_from=='3':
        with open("word_list/fruits.txt", 'w') as file:
            file.write(''.join(word_list))



header = """
This is a game to guess the word
choose which one you want to guess
1. animals
2. flowers
3. fruits
"""
print(header)

choose_from = input("enter: ")
while choose_from not in ['1', '2', '3']:
    print('invalid choice !!')
    choose_from = input("enter: ")

if choose_from == '1':
    with open("word_list/animals.txt", 'r') as file:
        word_list = file.readlines()
elif choose_from=='2':
    with open("word_list/flowers.txt", 'r') as file:
        word_list = file.readlines()
elif choose_from=='3':
    with open("word_list/fruits.txt", 'r') as file:
        word_list = file.readlines()


score = 0
while True:
    word = random.choice(word_list).strip().upper()
    hint = [' ' if i==' ' else '-' for i in word]
    chance = 5
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
                score+=1
                print("YOU WIN !!!!")
                print(f"your score is {score}")
                # rm = input("do you want to remove this word(y/n): ")
                # if rm.lower()=='y':
                #     remove_word(word)
                print()
                break
            else:
                print(f"the word '{guess}' is incorrect")
            
        if (hint.count('-')==0 and guess != word) or chance==0:
            print("Sorry you LOSE !!!")
            print((f"the word was {word}"))
            rm = input("do you want to remove this word(y/n): ")
            if rm.lower()=='y':
                remove_word(word)
            print()
            break
        if hint.count('-')<=2:
            print(f"you have {chance} chance remaining")
            chance-=1
    play = input("\nDo you want to play again?(y/n): ")
    if play.lower() == 'n':
        print("Thank you for playing")
        print(f"your score is: {score} !!!")
        quit()
