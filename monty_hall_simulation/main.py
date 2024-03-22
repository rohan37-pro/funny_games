import random
from person import strategy



def generate_doors(d=3):
    car = random.randint(0,d-1)
    doors = {}
    doors[car] = True
    for i in range(d):
        if i!= car:
            doors[i] = False
    return doors



def open_doors(player_choice, d):
    if doors[player_choice] == True:
        doo = list(doors.keys())
        doo.pop(player_choice)
        ch = random.choice(doo)
    else:
        ch = player_choice
    for i in doors:
        if doors[i] ==True:
            original = i
    closed = [ch, original]
    swap = random.randint(0,1)
    if swap ==1:
        closed[0], closed[1] = closed[1], closed[0]
    return closed


def final_selection(strategy, d):
    remains = open_doors(strategy[0], d)
    if strategy[1] == False:
        return strategy[0]
    elif strategy[1] == True:
        if remains[0] == strategy[0]:
            return remains[1]
        else:
            return remains[0]
    





if __name__=="__main__":
    d = int(input("enter number of doors: "))
    play = input("play game(p)/simulate(s): ").strip().lower()
    if play=='s':
        random_count_win = 0
        random_count_lose = 0
        stick_count_win = 0
        stick_count_lose = 0
        switch_count_win = 0
        switch_count_lose = 0
        print(f"simulating game for {d*1000} cases")
        for i in range(d*1000):
            doors = generate_doors(d)
            ran_strategy = strategy._random_(d)
            stick = strategy.sick_to_original_choice(d)
            switch = strategy.always_switch(d)
            ran_select = final_selection(ran_strategy, d)
            stick_select = final_selection(stick, d)
            switch_select = final_selection(switch, d)
            if doors[ran_select]==True:
                random_count_win+=1
            else:
                random_count_lose+=1
            if doors[stick_select]==True:
                stick_count_win+=1
            else:
                stick_count_lose+=1
            if doors[switch_select]==True:
                switch_count_win+=1
            else:
                switch_count_lose+=1
        result = f"""random strategy:
win {random_count_win}
lose {random_count_lose}

always stick to the choice strategy:
win {stick_count_win}
lose {stick_count_lose}

always switch strategy:
win {switch_count_win}
lose {switch_count_lose}"""
            # print(result, end='\r')
        print(result)
    if play =='p':
        win = 0
        lose = 0
        while True:
            doors = generate_doors(d)
            player_choice = int(input(f"enter door number to open(0,{d-1}): "))
            closed = open_doors(player_choice, d)
            print(f"except {closed[0]} and {closed[1]} all the other doors have goat")
            switch = input("do you want to switch(y/n): ").strip().lower()
            if switch == 'n':
                final_choice = player_choice
            elif switch == 'y':
                if closed[0] == player_choice:
                    final_choice = closed[1]
                else:
                    final_choice = closed[0]
            print(f"final choice is {final_choice}")
            if doors[final_choice] == True:
                print("congratulations !!!")
                print("you win ")
                win+=1
                print(f"score : win {win}, lose {lose}")
                # print(doors)
                print()
            else :
                lose +=1
                print("sorry !!!")
                print("you lose")
                # print(doors)
                print()
            play_again = input("do you want to play again?(y/n)")
            if play_again == 'n':
                break

        print("\nthank you for playing ...")
        print("your score:")
        print(f"win: {win}\nlose: {lose}")
        print()

