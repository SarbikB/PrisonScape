"""This code was inspired by the mind that seeks for an escape from everyday life....
 where no matter what.... each day can seem to be harder and harder and sometimes....
 it is just luck that allows you to win that day! Enjoy the escape from the prison of the mind
 ***Other inspirations come from GOT and LOTR.
 ***only the easy version can be played in the allotted 4 minutes excluding the intro
 ***Path for quickest finish in easy: Act sick, straight-straight-right at junction, look around - pick up - most likely you will beat the knight in 3 moves
 ***Thus far the game is incomplete as I was not able to successfully code for hard which includes level 5
 P.S no real past of coding experience :(
 ENJOY!!!! :D
 """
import time

def intro():
    global name
    print("""
     ██▓███   ██▀███   ██▓  ██████  ▒█████   ███▄    █      ██████  ▄████▄   ▄▄▄       ██▓███  ▓█████ 
    ▓██░  ██▒▓██ ▒ ██▒▓██▒▒██    ▒ ▒██▒  ██▒ ██ ▀█   █    ▒██    ▒ ▒██▀ ▀█  ▒████▄    ▓██░  ██▒▓█   ▀ 
    ▓██░ ██▓▒▓██ ░▄█ ▒▒██▒░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██░ ██▓▒▒███   
    ▒██▄█▓▒ ▒▒██▀▀█▄  ░██░  ▒   ██▒▒██   ██░▓██▒  ▐▌██▒     ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ 
    ▒██▒ ░  ░░██▓ ▒██▒░██░▒██████▒▒░ ████▓▒░▒██░   ▓██░   ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██▒ ░  ░░▒████▒
    ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▓  ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░
    ░▒ ░       ░▒ ░ ▒░ ▒ ░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░   ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░▒ ░      ░ ░  ░
    ░░         ░░   ░  ▒ ░░  ░  ░  ░ ░ ░ ▒     ░   ░ ░    ░  ░  ░  ░          ░   ▒   ░░          ░   
                ░      ░        ░      ░ ░           ░          ░  ░ ░            ░  ░            ░  ░
                                                                   ░                                                                                                 
    --------------------------------------------------------------------------------------------------
    Hello Gamer and Welcome to Prison Scape [enter dramatic sound]
    This is an interactive game where you have to escape from the castle prison. 
    Solve problems and escape the treacherous castle. 
            HINT : There are more ways than one to leave the castle but not all 
            paths are created equal so tread carefully :O 
            *For the best gaming experience you need to be creative.*
            **Remember this is a castle and there are hidden treasures everywhere 
            but be careful and don't get caught or else you will be thrown back 
            into prison :( **
    So let the games begin!!!!!!!
    --------------------------------------------------------------------------------------------------
    Before we start, pick your character name. Then we can begin your escape from 
    the trecherous confines of this castle [thun thun thunnnnnnnn]!!!!""")
    time.sleep (4)

    name = input(f'\nInput Character name: ')
    print(f'\nWelcome {name}')

    happy = input(f'\nAre you happy with this name? (y/n) ')
#this allows the player to try to input the code again
    while 'n' in happy:
        name = input(f'\nOkay lets try this again, shall we? \nInput Character name: ')
        print(f'\nWelcome {name}')
        happy = input(f'\nAre you happy with this name? (y/n) ')
        if 'y' in happy:
            continue
    name = name.capitalize()
    print(f'\nI am glad we got your name sorted {name}! Welcome to Prison Scape!!!')
    print(f"""\nNow lets choose your difficulty 
        *Remember the harder the level you choose the more possible rewards you can get....""")
    difficulty()

def difficulty():
    time.sleep(3)
    global difficulty
    difficulty = input(f"""\nWhat difficulty would you like?
    1)Easy
    2)Medium
    3)Hard
    (Please select 1,2 or 3)""")
    while difficulty not in ['1','2','3']:
        print ('Sorry you selcted something invalid')
        difficulty = input(f"""\nWhat difficulty would you like?
            1)Easy
            2)Medium
            3)Hard
            (Please select 1,2 or 3)""")
    sure = input(f'\nAre you up to the challenge of this difficulty? (y/n)')
    while 'n' in sure:
        difficulty = input(f"""\nOkay lets try this again, shall we? \nWhat difficult would you like?
                    1) Easy
                    2) Medium
                    3) Hard 
                    (please state 1,2 or 3)""")
        print(f'\nYou have selected {difficulty}')
        sure = input(f'\nAre you up to the challenge for this difficulty? (y/n) ')
        if 'y' in sure:
            continue
    if '1' in difficulty or 'E' in difficulty or 'e' in difficulty:
        difficulty = 'easy'
    elif '2' in difficulty or 'M' in difficulty or 'm' in difficulty:
        difficulty = 'medium'
    elif '3' in difficulty or 'H' in difficulty or 'h' in difficulty:
        difficulty = 'hard'
    else:
        print(f'\nI am sorry, that was an invalid response, please run the program again :(')
    print(f"""\nAlright {name} let's get started with prison escape on dificulty level {difficulty} 
    before you start to regret your decision....muhahahahaha!!!!!""")
    time.sleep(2)
    level_1()

def level_1():
    time.sleep(3)
    global inventories
    print(f"""
    --------------------------------------------------------------------------------------------------------------------
    \n\n....pant ...... pant
    [GASP!!!] ughhhh.... I thought I was stuck in a prison cell in a castle....
    [opens eyes] Wait what???? What are those bars doing here? Where am I?
    \nWhat is happening? [Screams]
    (Guard yells: Keep quiet in there, the King is sleeping!!)
    \nKing? What? Where am I???
    (Guard approaches: You are in prison, {name}, or should I rather call you filth!)
    Okay I have to get out of here as soon as ... I have to think.... what can I do?""")

    decision_1 = input("""So in my mind I have 3 options:
    1)Call the guard and try to over power him...
    2)Wait and see what happens... or
    3)Act sick....\n(please select 1, 2 or 3)\n""")
    decision_1 = decision_1.upper()

    while decision_1 not in ['1', '2', '3', 'call', 'wait', 'act', 'act sick']:
        print('I can\'t do that .... I can only do the other one')
        decision_1 = input("""So in my mind I have 3 options:
        1)Call the guard and try to over power him...
        2)Wait and see what happens... or
        3)Act sick....\n(please select 1, 2 or 3)\n""")
        decision_1 = decision_1.upper()
# first nested loop that leads the user to one correct decision
    if '1' in decision_1 or 'CALL' in decision_1 or 'OVER POWER' in decision_1:
        print(f'Guard Shouts: Shut up {name}!!! (nothing happens)')
        decision_11 = input("""So clearly that didn't work...do I can either...
        1)Wait or 2)Act sick \n(please select 1 or 2)\n""")
        decision_11 = decision_11.upper()

        while decision_11 not in ['1', '2', 'WAIT', 'ACT SICK', 'SICK', 'ACT']:
            print('I can\'t do that... try to select again')
            decision_11 = input("""So clearly that didn't work...do I can either...
            1)Wait or 2)Act sick \n(please select 1 or 2)\n""")
            decision_11 = decision_11.upper()

        if '1' in decision_11 or 'WAIT' in decision_11:
            print("""The guard approached the cell but then he left....
            guess I have to act sick....
            \n ..... cough.....cough.....(it is working, he is coming close)
            [Guard asks: Hey! Whats going on? What is happening?]
            (I need to take it further)
            ...(role on the floor and scream in agonizing pain)
            [Guard enters the cell]""")
            time.sleep(2)
            print ("""\n \n (I quickly get up and over power the guard and knock the guard down)
            Phew that was a close one!
            \nToo bad his clothes are too small, it would make it super easy to escape, guess I need to sneak out....""")

        elif '2' in decision_11 or 'ACT SICK' in decision_11 or 'ACT' in decision_11:
            print("""\n ..... cough.....cough.....(it is working, he is coming close)
            [Guard asks: Hey! Whats going on? What is happening?]
            (I need to take it further)
            ...(role on the floor and scream in agonizing pain)
            [Guard enters the cell]""")
            time.sleep(2)
            print ("""\n \n (I quickly get up and over power the guard and knock the guard down)
            Phew that was a close one!
            \nToo bad his clothes are too small, it would make it super easy to escape, guess I need to sneak out....""")

        else:
            print('Something went wrong.... :O')

    elif '2' in decision_1 or 'WAIT' in decision_1:
        print('The guard approached the cell but then he left....')
        decision_12 = input("""I guess I can then either call him or act sick...
        What should I do?\n1)Call Him or 2)Act Sick?\n""")
        decision_12 = decision_12.upper()
        while decision_12 not in ['1', '2', 'CALL HIM', 'CALL', 'ACT', 'SICK', 'ACT SICK']:
            print('I can\'t do that action unfortunately so let\'s select again')
            decision_12 = input("""I guess I can then either call him or act sick...
            What should I do?\n1)Call Him or 2)Act Sick?\n""")

        if '1' in decision_12 or 'CALL' in decision_12:
            print(f"""Guard Shouts: Shut up {name}!!! (nothing happens)
            sooooo I guess I will act sick then""")
            input('<Press Enter to Continue>')
            print("""\n ..... cough.....cough.....(it is working, he is coming close)
            [Guard asks: Hey! Whats going on? What is happening?]
            (I need to take it further)
            ...(role on the floor and scream in agonizing pain)
            [Guard enters the cell]
            \n \n (I quickly get up and over power the guard and knock the guard down)
            Phew that was a close one!
            \nToo bad his clothes are too small, it would make it super easy to escape, guess I need to sneak out....""")

        elif '2' in decision_12 or 'ACT' in decision_12 or 'SICK' in decision_12:
            print("""\n ..... cough.....cough.....(it is working, he is coming close)
            [Guard asks: Hey! Whats going on? What is happening?]
            (I need to take it further)
            ...(role on the floor and scream in agonizing pain)
            [Guard enters the cell]
            \n \n (I quickly get up and over power the guard and knock the guard down)
            Phew that was a close one!
            \nToo bad his clothes are too small, it would make it super easy to escape, guess I need to sneak out....""")

        else:
            print('something went wrong')

    elif '3' in decision_1 or 'ACT' in decision_1 or 'SICK':
        print("""\n ..... cough.....cough.....(it is working, he is coming close)
            [Guard asks: Hey! Whats going on? What is happening?]
            (I need to take it further)
            ...(role on the floor and scream in agonizing pain)
            [Guard enters the cell]
            \n \n (I quickly get up and over power the guard and knock the guard down)
            Phew that was a close one!
            \nToo bad his clothes are too small, it would make it super easy to escape, guess I need to sneak out....""")

    else:
        print('something went wrong')
#1st eater egg
    decision2 = input(f"""What should I do next?
    1)Search the guard
    2)Walk out of the prison \n """)
    if '1' in decision2 or 'search' in decision2:
        inventories = []
        inventories.append('rustykey')
        print('Hmmmmm I found a rusty key....wonder where I can use this')
        input('<Press Enter to Continue>\n')
    elif '2' in decision2 or 'W' in decision2 or 'w' in decision2:
        inventories = []
        print('<Press Enter to Continue>\n')
    else:
        print('Something went wrong, you might need to resart the code :( ')

    print(f"""
    --------------------------------------------------------------------------------------------------------------------
    GOOD JOB {name.upper()} in completing level 1!!!!""")
    level_2()

def level_2():
    time.sleep(2)
    print(f"""The next stage is THE STAIRCASES OF DOOM!!!! ... \n[this is going to take some walk]
    You see some writing next to the staircase....

    (there's something written on it, "If you want to know how to climb the stairs.....

    Get a step by step tutorial")..... okay that was funny but there's more 

    (The path you seek isn't straight neither is it all twisted, remember to not get lost)

    Well that was encouraging.... at least there are only 3 options for now but \n it probably gets complicated""")

    path_1 = input(f"""Which way should I go? \n1)Left \n2)Straight \n3)Right \n""")
    path_1 = path_1.upper()
    while path_1 not in ['1', '2', '3', 'LEFT', 'RIGHT', 'STRAIGHT']:
        print('That was not a valid response, please try again :)')
        path_1 = input(f"""Which way should I go? \n1)Left \n2)Straight \n3)Right \n""")
        path_1 = path_1.upper()
# this is a maze and thus has 4 levels of nested loops
    if '1' in path_1 or 'LEFT' in path_1:
        print('You walked onto the left staircase, now you only have two options. Straight or Right')
        path_11 = input(f'Which way should I go? \n1)Straight or 2)Right? \n')
        path_11 = path_11.upper()
        while path_11 not in ['1', '2', 'STRAIGHT', 'RIGHT']:
            print('Your entry was invalid, try again')
            print('You walked onto the left staircase, now you only have two options. Straight or Right')
            path_11 = input(f'Which way should I go? \n1)Straight or 2)Right? \n')
            path_11 = path_11.upper()

        if '1' in path_11 or 'STRAIGHT' in path_11:
            print('After walking straight, it seems like there is only one option left and that is to go right.')
            input('<Press Enter to Continue>\n')
            path_111 = input("""After walking for a while, you have two options again.
            \n 1) Left or \n2)Right... \n what do you choose? \n""")
            path_111 = path_111.upper()
            while path_111 not in ['1', '2', 'LEFT', 'RIGHT']:
                print('This is something that I can\'t do :(')
                path_111 = input(f"""After walking for a while, you have two options again.
                \n 1) Left or \n2)Right... \nWhat do you choose? \n""")
                path_111 = path_111.upper()

            if '1' in path_111 or 'LEFT' in path_111:
                print('You walked left but......\n'
                    'Seems like this is a dead end and there is a sharp right turn. \nBut I feel like I am going back. \n There is another right... now I am definitely going back')
                path_1111 = input(f"""So it seems like there are two options 
                one that goes sharp right back but I think I just came from there so I will go left. \nPlus there is some light coming from there.
                \n \n<Press Enter to Continue>\n""")
                print('Yayyyyyyy at least I crossed the staircases of doom!!! :O')
                # go to level 3
                level_3()

            elif '2' in path_111 or 'RIGHT' in path_111:
                print('You walked right and....'
                    'hmmmmm I think I am almost there.... I can see some light coming from the path that continues to the right')
                path_1112 = input("""So do I take the place with the light or do I take the path that goes left?
                \n 1) Go straight or \n2)Go left? \n""")
                path_1112 = path_1112.upper()
                while path_1112 not in ['1', '2', 'STRAIGHT', 'LEFT']:
                    print('that is something I can\'t do')
                    path_1112 = input("""So do I take the place with the light or do I take the path that goes left?
                    \n 1) Go straight or \n2)Go left? \n""")
                    path_1112 = path_1112.upper()

                if '1' in path_1112 or 'Straight' in path_1112:
                    print('After walking towards the light....I think I have finally escaped the staircases of doom!!!!')
                    # go to level three
                    level_3()

                elif '2' in path_1112 or 'L' in path_1112:
                    print("""Woooooowwww this way is long .... oops I came back to where I started....
                    I am sick of these staircases.... guess I have to go straight! 
                    Where did my choices go? """)
                    input('<Press Enter to Continue>')
                    print('I walked towards the light. At least I escaped the Staircases of doom!!!!! :O')
                    # go to level 3
                    level_3()

                else:
                    print('something went wrong')

            else:
                print('something went wrong')

        elif '2' in path_11 or 'RIGHT' in path_11:
            print('Seems like the staircase bends a corner to the left despite starting of towards the right....\nseems like there is only one path....')
            path_112 = input(
                f"""After walking for a while you get to a junction.... hmmmmm \n which way should I go?
            \nI can either go \n1)Left or \n2)Right \n""")
            path_112 = path_112.upper()
            while path_112 not in ['1', '2', 'LEFT', 'RIGHT']:
                print('I cannot do that')
                path_112 = input(
                    f"""After walking for a while you get to a junction.... hmmmmm \n which way should I go?
                \nI can either go \n1)Left or \n2)Right \n""")
                path_112 = path_112.upper()

            if '1' in path_112 or 'L' in path_112:
                print(
                    'Seems like this is a dead end and there is a sharp right turn. \nBut I feel like I am going back. \n There is another right... now I am definitely going back')
                path_1121 = input(f"""So it seems like there are two options 
                one that goes sharp right back but I think I just came from there so I will go left. \nPlus there is some light coming from there.
                \n \n <Press Enter to Continue>""")
                print('At least I have escaped from the Staircases of DOOM!!!!! :O')
                # go to level 3
                level_3()

            elif '2' in path_112 or 'R' in path_112:
                print(
                    'hmmmmm I think I am almost there.... I can see some light coming from the path that continues to the right')
                path_1122 = input("""So do I take the place with the light or do I take the path that goes left?
                \n 1) Go straight or \n2)Go left? \n""")
                path_1122 = path_1122.upper()
                while path_1122 not in ['1', '2', 'STRAIGHT', 'LEFT']:
                    print('I don\'t think I can do that!')
                    path_1122 = input("""So do I take the place with the light or do I take the path that goes left?
                    \n 1) Go straight or \n2)Go left? \n""")
                    path_1122 = path_1122.upper()

                if '1' in path_1122 or 'Straight' in path_1122:
                    print('I think I have finally escaped the staircases of doom!!!!')
                    # go to level three
                    level_3()

                elif '2' in path_1122 or 'R' in path_1122:
                    print("""Woooooowwww this way is long .... oops I came back to where I started....
                    I am sick of these staircases.... guess I have to go straight! 
                    Where did my choices go? """)
                    input('<Press Enter to Continue>\n')
                    print('Atleast I completed the STAIRCASES OF DOOM!!!!!')
                    # go to level 3
                    level_3()

                else:
                    print('something went wrong')

        else:
            print('Something went wrong')

    elif '2' in path_1 or 'STRAIGHT' in path_1:

        print('After walking straight, you reach a three-way junction.')
        path_12 = input(
            f"""You can go in three directions. \n1)Left \n2)Keep going straight or \n3)Go right \n \n""")
        path_12 = path_12.upper()
        while path_12 not in ['1', '2', '3', 'LEFT', 'STRAIGHT', 'RIGHT']:
            print('I don\'t think I can do that!')
            path_12 = input(
                f"""You can go in three directions. \n1)Left \n2)Keep going straight or \n3)Go right \n \n""")
            path_12 = path_12.upper()

        if '1' in path_12 or 'LEFT' in path_12:
            print('Seems like I can only go right from here .... so much for my choices.... (click)')
            door1 = 1
            input('<Press Enter to Continue>')
            path_121 = input(
                'You come to a junction, where you can go 1)left or 2)right. \nWhat do you choose? \n')
            path_121 = path_121.upper()
            while path_121 not in ['1', '2', 'LEFT', 'RIGHT']:
                print('I can\'t do that I think :(')
                path_121 = input(
                    'You come to a junction, where you can go 1)left or 2)right. \nWhat do you choose? \n')
                path_121 = path_121.upper()

            if '1' in path_121 or 'L' in path_121:
                print('Hmmmmm I kept going and there doesn\'t seem to be a way but a hidden door appears...')
                h_door = input(
                    'Hmmmmm should I try the door? What should I do? \n1)Try to open door or\n2)Keep walking?\n')
                h_door = h_door.upper()
                while h_door not in ['1', '2', 'OPEN', 'WALK', 'WALKING']:
                    print('I don\'t think I can do that! :O')
                    h_door = input(
                        'Hmmmmm should I try the door? What should I do? \n1)Try to open door or\n2)Keep walking? \n')
                    h_door = h_door.upper()
#second easter egg
                if '1' in h_door or 'T' in h_door or 'O' in h_door or 'D' in h_door:
                    if 'rustykey' in inventories:
                        print('The door opens..... wowwwwww I found some treasure!!!!')
                        inventories.append('treasure')
                        time.sleep(2)
                        print('I kept walking and I bend a corner and suddenly I saw light coming from the left!'
                              'I walked towards the light and I escaped the Staircases of Doom!! :)')
                        time.sleep(1)
                        # go to level 3
                        level_3()
                    else:
                        print('Oh it looks like I don\'t have the key for this door :(')

                elif '2' in h_door or 'K' in h_door or 'W' in h_door:
                    print('Looks like I am gonna keep walking...... Oh dang..... I came back to the same place')
                    path_1212 = input(
                        'Looks like I will have to go right this time... \n<Press Enter to Continue>')
                    print(
                        'hmmmmm I think I am almost there.... I can see some light coming from the path that continues to the right')
                    path_1212 = input("""So do I take the place with the light or do I take the path that goes left?
                    \n 1) Go straight or \n2)Go left? \n""")
                    path_1212 = path_1212.upper()
                    while path_1212 not in ['1', '2', 'STRAIGHT', 'LEFT']:
                        print('I can\'t take that action ')
                        path_1212 = input("""So do I take the place with the light or do I take the path that goes left?
                        \n 1) Go straight or \n2)Go left? \n""")
                        path_1212 = path_1212.upper()

                    if '1' in path_1212 or 'Straight' in path_1212:
                        print('I think I have finally escaped the staircases of doom!!!!')
                        # go to level three
                        level_3()

                    elif '2' in path_1212 or 'l' in path_1212:
                        print("""Woooooowwww this way is long .... oops I came back to where I started....
                        I am sick of these staircases.... guess I have to go straight! 
                        Where did my choices go? """)
                        input('<Press Enter to Continue>')
                        print('Yayyyyy I finally finished the Staircases of Doom!!! :O')
                        # go to level 3
                        level_3()

                    else:
                        print('something went wrong')

                else:
                    print('Something went wrong')

            elif '2' in path_121 or 'R' in path_121:
                print('Hmmmmm I can almost see the light coming from the path that continues to go straight')
                path_1212 = input("""Hmmmm do I go towards the light or do I try my luck with the left?
                1)Go straight or \n2)Go left? \n""")
                path_1212 = path_1212.upper()

                if '1' in path_1212 or 'S' in path_1212:
                    print('Seems like this is it!!! WOOOOHOOOOOO I made it out of the staircase of doom')
                    # go to level 3
                    level_3()

                elif '2' in path_1212 or 'L' in path_1212:
                    # maybe add a timer
                    print('Wow this is a long walk and I keep going round and round')
                    print("""Ohhhhhhh wait a minute......
                    How did I end up back here? 

                    CURSEEEEEE YOUUUUUU STAIRCASE OF DOOOOOOOOOOO!!!!!!""")
                    input('Guess I will keep straight and go towards the light! \n<Press Enter to Continue>\n')
                    print('Seems like this is it!!! WOOOOHOOOOOO I made it out of the staircase of doom')
                    # go to level 3
                    level_3()

                else:
                    print('Something went wrong')

            else:
                print('something went wrong :(')


        elif '2' in path_12 or 'STRAIGHT' in path_12:
            print('So I continued on straight... I guess I don\'t have to think too much about this')
            path_122 = input('<Press Enter to Continue>')
            print('Wait what was that? I felt like I stepped on something! I hope I didn\'t trap myself')
            path_1222 = input("""Hmmmm interesting, I have reached a junction.
            I can either go 1)Left or 2)Right\n""")
            path_1222 = path_1222.upper()
            while path_1222 not in ['1', '2', 'LEFT', 'RIGHT']:
                print('I can\'t do that unfortunately')
                path_1222 = input("""Hmmmm interesting, I have reached a junction.
                I can either go 1)Left or 2)Right\n""")
                path_1222 = path_1222.upper()
#3rd easter egg
            if '1' in path_1222 or 'L' in path_1222:
                print('Interesting!! It just seems to keep going .... wait there is a hidden door that appears')
                h_door1 = input("""So it seems that I can try to open this door or keep walking
                What do I do? \n1)Try to open the door or \n2)Keep Walking\n""")
                h_door1 = h_door1.upper()
                while h_door1 not in ['1', '2', 'OPEN', 'WALK']:
                    print('I can\'t make this action')
                    h_door1 = input("""So it seems that I can try to open this door or keep walking
                    What do I do? \n1)Try to open the door or \n2)Keep Walking\n""")
                    h_door1 = h_door1.upper()

                if '1' in h_door1 or 'O' in h_door1 or 'D' in h_door1:
                    if 'rustykey' in inventories:
                        print('Oh my god, this was not expected!!!!')
                        # Escape in easy
                        completed()
                        # Go to level 4 in medium and hard
                        if difficulty == 'medium' or difficulty == 'hard':
                            level_4()
                        else:
                            print('Something went wrong')

                    else:
                        print(
                            'You tried to open but to no avail.... guess I have to keep walking and I ended back in the same place')
                        h_door1 = '2'

                elif '2' in h_door1 or 'K' in h_door1 or 'W' in h_door1:
                    print('Okay so now I can\'t go back the same way since it got locked')
                    path_1222 = '2'
                    input('I guess I am going right then. \n<Press Enter to Continue>\n')

                else:
                    print('Something went wrong.... you caught me :( ')

            elif '2' in path_1222 or 'R' in path_1222:
                print('I think I am almost there.... I can see some light from the path that goes straight')
                path_12222 = input("""Hmmmm so I can either go towards the light or go left
                Should I go 1)Straight or 2)Left? \n""")
                path_12222 = path_12222.upper()
                while path_12222 not in ['1', '2', 'STRAIGHT', 'LEFT']:
                    print('I don\'t think I can do that!')
                    path_12222 = input("""Hmmmm so I can either go towards the light or go left
                    Should I go 1)Straight or 2)Left? \n""")
                    path_12222 = path_12222.upper()

                if '1' in path_12222 or 'S' in path_12222:
                    print('I think I am there.... yessssss.... woohoooo.... I have escaped the staircase of doom')
                    # go to level 3
                    level_3()

                elif '2' in path_12222 or 'L' in path_12222:
                    print('wait what the???? I just ended up at the same place')
                    input("""I guess I will go straight then..... well it\'s no fun to not loop :(
                           \n<Press Enter to Continue>""")
                    print('Finally I have escaped the staircases of DOOM and now onto a brightly lit room!')
                    # go to level 3
                    level_3()

                else:
                    print('Whoops 404 ERROR')

            else:
                print('404... entry invalid :(')


        elif '3' in path_12 or 'RIGHT' in path_12:
            while '3' in path_12 or 'RIGHT' in path_12:
                print('Right seems right! oh well.... these staircases are a bit of a hassle!')
                path_123 = input('<Press Enter to Continue>')
                print(
                    'As you continued to walk, you reach a deadend.... oh well.... I guess I have to head-back \n ugggghhhhhh')
                path_12 = input(
                    f"""You can still go in three directions. \n1)Left \n2) Keep going straight or \n3)Go right \n \n""")
                path_12 = path_12.upper()

            if '1' in path_12 or 'L' in path_12:
                print('Oh I guess I will keep walking and walking, the path goes and bends the corner')
                path_121 = input("""Okay so I get to a junction, now what?
                I can either go 1)Left or I can 2)Right\n""")
                path_121 = path_121.upper
                while path_121 not in ['1', '2', 'LEFT', 'RIGHT']:
                    print('I cannot take that action I think')
                    path_121 = input("""Okay so I get to a junction, now what?
                    I can either go 1)Left or I can 2)Right\n""")
                    path_121 = path_121.upper

                if '1' in path_121 or 'LEF' in path_121:
                    print('Hmmmmmm this path keeps going on and on!!!!')
                    input('<Press Enter to Continue')
                    print('Oh I seem to be back where I came from and now the other path has closed')
                    path_121 = 2

                elif '2' in path_121 or 'RIGH' in path_121:
                    print('Hmmmmm I think I am almost out, I can see a light coming out of the way that leads straight')
                    path_1212 = input("""So I can go towards the light or left
                    So should I go 1)Straight or 2)Left\n""")
                    path_1212 = path_1212.upper()
                    while path_1212 not in ['1', '2', 'STRAIGHT', 'LEFT']:
                        print('I cannot make that action')
                        path_1212 = input("""So I can go towards the light or left
                        So should I go 1)Straight or 2)Left\n""")
                        path_1212 = path_1212.upper()

                    if '1' in path_1212 or 'STRAI' in path_1212:
                        print('The light is getting brighter.... wohoooooooo I am out')
                        input('<Press Enter to Continue>')
                        # go to level 3
                        level_3()

                    elif '2' in path_1212 or 'LEF' in path_1212:
                        print('Hmmmm okay this path is longggggg.... oh wait what? I am back to where I came from!')
                        input('<Press Enter to Continue>')
                        print('I guess I will go towards the light then, well atleast I escaped the staircases of doom')
                        # go to level 3
                        level_3()

                    else:
                        print('404 ERROR')

                else:
                    print('Something went wrong... but can you still give me an A? Really tried with these loops')

            elif '2' in path_12 or 'STRAI' in path_12:
                print('Oh I guess I will just keep walking and for some reason I arrived at a junction')
                input(
                    'Strange.... the path to the left is blocked.... guess I can only go right \n<Press Enter to Continue>\n')
                print('I can see the light from the path that leads straight')
                path_122 = input("""So now two more options? on that goes towards the light or the one that goes left
                Should I go 1)Straight or 2)Left\n""")
                path_122 = path_122.upper()
                while path_122 not in ['1', '2', 'STRAIGHT', 'LEFT']:
                    print('I cannot take that action :O')
                    path_122 = input("""So now two more options? on that goes towards the light or the one that goes left
                    Should I go 1)Straight or 2)Left\n""")
                    path_122 = path_122.upper()

                if '1' in path_122 or 'STRAIGHT' in path_122:
                    print('Finally I can see the light! I am here... I have finished the staircases of doom!!!')
                    input('<Press Enter to Continue')
                    # go to level 3
                    level_3()

                elif '2' in path_122 or 'LEFT' in path_122:
                    print("""As I was about to start my journey up the left staircase.... the ...the....
                    staircase disappeared.... ahhhhhhh.... phewwww that was close""")
                    # could've killed you but didn't
                    # restart in medium and hard
                    input("""I guess I will go straight then.... phewwww.....
                    I barely escaped .... wohoooo I made it!!!
                    I finally crossed the staircases of doom!!!!""")
                    # go to level 3
                    level_3()

                else:
                    print('something went wrong')

            else:
                print('Something went wrong')

        else:
            ('Something went wrong :( ')

    elif '3' in path_1 or 'RIGHT' in path_1:

        print('You walked onto the staircase on the right, now you reach at a place with two options')
        path_13 = input('You can either \n1)Keep going straight or \n2)Turn Left')
        path_13 = path_13.upper()
        while path_13 not in ['1', '2', 'STRAIGHT', 'LEFT', 'TURN LEFT']:
            print('That is not a valid action :(')
            path_13 = input('You can either \n1)Keep going straight or \n2)Turn Left')
            path_13 = path_13.upper()

        if '1' in path_13 or 'STRAIGHT' in path_13:
            print('You have reached a dead end, you can only go back and turn left')
            input('<Press Enter to Continue')
            path_13 = '2'

        elif '2' in path_13 or 'LEFT' in path_13:
            print('Alright I guess I will take my chances turning again.... I hope I am not lost')
            input('<Press Enter to Continue>')
            print('You come to a bend to the right.... wow.... I am so lost.... \nyou reach a two way junction')
            path_131 = input(f"""Okay so there seem to be only two options, \n1)Left or \n2)Right \n
            What do you choose?\n""")
            while path_131 not in ['1', '2', 'LEFT', 'RIGHT']:
                print('That is not something I can do')
                path_131 = input(f"""Okay so there seem to be only two options, \n1)Left or \n2)Right \n
                What do you choose?\n""")

            if '1' in path_131 or 'LEFT' in path_131:
                print("""Hhmmmmm this is interestingly long.... I come to junction
                One which is a hairpin turn left and the other where there is a sharp back turn right""")
                path_1311 = input('Should I go 1)Left or 2)Right? \n')
                path_1311 = path_1311.upper()
                while path_1311 not in ['1', '2', 'LEFT', 'RIGHT']:
                    print('I cannot go that way')
                    path_1311 = input('Should I go 1)Left or 2)Right? \n')
                    path_1311 = path_1311.upper()
                if '1' in path_1311 or 'LEFT' in path_1311:
                    print(' I seeeeeeee the lighttttt!!! Yes I have finally conquered the staircases of doom!')
                    # go to level 3
                    level_3()

                elif '2' in path_1311 or 'RIGHT' in path_1311:
                    print('Wait what, just as soon as I was about to step onto it .... it vanished')
                    input('I guess I am going left \n<Press Enter to Continue>')
                    print('WHOOP WHOOOP I finally finished the staircases of doom!')
                    # go to level 3
                    level_3()

                else:
                    print('Something went wrong')

            elif '2' in path_131 or 'RIGHT' in path_131:
                print('I think I can see the end, there is a light from the straight route')
                path_1312 = input("""Hmmmm so I can either go
                1)Straight or 2)Left. \nWhat should I do? \n""")
                path_1312 = path_1312.upper()
                while path_1312 not in ['1', '2', 'STRAIGHT', 'LEFT']:
                    print('I can\'t make that choice, let\'s try again')
                    path_1312 = input("""Hmmmm so I can either go
                    1)Straight or 2)Left. \nWhat should I do? \n""")
                    path_1312 = path_1312.upper()

                if '1' in path_1312 or 'STRAIGHT' in path_1312:
                    print('YESSSS I see it .... the end of the Staircases of Doom! \nI have cleared it!!!')
                    # go to level 3
                    level_3()

                elif '2' in path_1312 or 'LEFT' in path_1312:
                    print('WOAHHHHHH .... the staircase vanished!!!!!')
                    input('<Press Enter to Continue>')
                    print("""Phewwwww that was close, I guess I am going straight then.
                    Looks like I have done it.... I have cleared the level!!!""")
                    # go to level 3
                    level_3()

                else:
                    print('something went wrong')

            else:
                print('something went wrong')

        else:
            ('Something went wrong')

    else:
        print('something went wrong :( ')

def level_3():
    time.sleep(3)
    from random import randint
    if difficulty == 'easy':
        k_lives = 3
        lives = 3

    elif difficulty == 'medium':
        k_lives = 4
        lives = 3

    elif difficulty =='hard':
        k_lives = 5
        lives = 3

    else:
        print ('something went wrong!')

    print(f"""
    --------------------------------------------------------------------------------------------------------------------
    [YOU ARE NOW ENTERING THE KNIGHTS ARENA AND IN THIS DIFFICULTY
    YOU HAVE {lives} LIVES AND THE KNIGHT HAS {k_lives} LIVES..... TRY TO SURIVE!]

    OH GOD! It's too bright in here, my eyes need to adjust to all the light
    especially after coming from all those dark staircases. 


    (WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOSSSHHHHHH)
    [dodges the swing of a sword]

    [Welcome {name} to my arena, I am the knight of the castle! I can just call the guards but 
    let's have some fun shall we???]

    This guy is crazy, and he is swinging the sword around like it's nothing.... what do I do?""")

    arena_1 = input("""So I guess I have to find something to defend myself with....
    what should I do? \n1)Look around or 2)Stand my ground?\n(please select 1 or 2)\n""")
    arena_1 = arena_1.upper()
    while arena_1 not in ['1', '2', 'LOOK AROUND', 'STAND MY GROUND']:
        print('I am not sure what I am thinking.... I have to make a choice!')
        arena_1 = input("""So I guess I have to find something to defend myself with....
        what should I do? \n1)Look around or 2)Stand my ground?\n(please select 1 or 2)\n""")
        arena_1 = arena_1.upper()
    if '2' in arena_1 or 'STAND' in arena_1 or 'GROUND' in arena_1:
        print('You must be brave or foolish.... tell me which you are!')
        answer = input("""I am .... 1)Brave or 2)Foolish\n(please select 1 or 2)\n""")
        while answer not in ['1', '2']:
            print('I should answer the knight.....')
            answer = input("""I am .... 1)Brave or 2)Foolish\n(1 or 2)\n""")
# fourth easter egg
        if answer == '1':
            print(f'You must be more foolish than I thought {name}')
            print("""Oh no I don't feel good, I guess I should look around for something to protect myself with!""")
            arena_1 = '1'
        elif answer == '2':
            print(
                f"I admire your honesty {name}.... if you win this challenge I will give you my sword\n "
                f"This sword has been handed down for generations and is made of the VALERIAN STEEL!")
            inventories.append('Valerian Sword')
            print('BUT for now look around and fight me !!!!')
            arena_1 = '1'
        else:
            print('Something went wrong')
    if '1' in arena_1 or 'LOOK' in arena_1 or 'AROUND' in arena_1:
        print('I look around and I spot a sword')
        arena_11 = input("Oh there I go. I found a sword! Should I pick it up? (y/n)")
        arena_11 = arena_11.upper()
        while arena_11 not in ['Y', 'N', 'YES', 'NO']:
            print('I don\'t think I am thinking straight! Let me hear myself again!')
            arena_11 = input("Oh there I go. I found a sword! Should I pick it up? (y/n)")
            arena_11 = arena_11.upper()

        while 'N' in arena_11 or 'NO' in arena_11:
            print('Yikes .... the knight is attacking me if I stay still')
            lives -= 1
            print('Oh nooooo! I got hit! I am starting to loose some blood....I can\'t take more of this!!!')
            if lives == 1:
                print(f'I only have {lives} life left!')
            elif lives > 1:
                print(f'I only have {lives} lives left!')
            if lives == 0:
                print('Oh noooooo, I have suffered too much!!! I am loosing conciousness.........')
                choice = input ('Do you want to continue playing? \n(y/n)\n')
                choice = choice.upper()
                while choice not in ['Y','N','YES','NO']:
                    print ('that was an invalid selection please try again')
                    choice = input('Do you want to continue playing? \n(y/n)\n')
                    choice = choice.upper()
                if 'Y' in choice or 'YES' in choice:
                    level_1()
                elif 'N' in choice or 'NO' in choice:
                    print ('Thank you for playing Prison Scape! Have a great day! :D')
                    leave()
                # sent back to the beginning
            else:
                arena_11 = input("Oh there.... I see a sword. I found a sword! Should I pick it up? (y/n)")
                continue

        if 'Y' in arena_11 or 'YES' in arena_11:
            print('I think this is a good option.... I sprint towards the sword')
            input('<Press Enter to Continue>')
            print("""I hurredly pick up the sword and face the knight! I am ready for you!!!!
            (Looks like I have to guess which direction he is going to swing in!)""")
#random battle depending on battle
            while k_lives > 0:
                if difficulty == 'easy':
                    k_direction = randint(0, 1)
                    k_direction += 1
                    # more random directions with medium and hard!
                    direction = input("""Which direction would he strike from?
                    1)Left or 2)Right? \n(Please enter 1 or 2) \n""")
                    while direction not in ['1', '2']:
                        print('I need to decide!')
                        direction = input("""Which direction would he strike from?
                                    1)Left or 2)Right? \n""")
                elif difficulty == 'medium' or difficulty == 'hard':
                    k_direction = randint(0, 2)
                    k_direction += 1
                    # more random directions with medium and hard!
                    direction = input("""Which direction would he strike from?
                                        1)Left, 2)Right or 3)From up? \n(Please enter 1 or 2 or 3) \n""")
                    while direction not in ['1', '2', '3']:
                        print('I need to decide!')
                        direction = input("""Which direction would he strike from?
                                                                1)Left, 2)Right or 3)From up? \n(Please enter 1 or 2 or 3) \n""")

                if k_direction == int(direction):
                    k_lives -= 1
                    print(f"""You were able to guess the direction right and give a counter blow!
                    Now the knight has {k_lives} live(s) and you still have {lives} live(s) left!""")
                    if k_lives == 0:
                        print('You have defeated the knight!!!!! The door behind him shows the exit from the castle')
                        # finish game in easy
                        if difficulty == 'easy':
                            completed()
                        # go to level 4 in medium and hard
                        elif difficulty == 'medium' or difficulty == 'hard':
                            print('I am now entering level 4!!!!')
                            level_4()

                    else:
                        continue
                elif k_direction != int(direction):
                    lives -= 1
                    print(f"""You were not able to guess the direction right and got struck...noooooo!
                    Now the knight has {k_lives} live(s) and you still have {lives} live(s) left!""")
                    if lives == 0:
                        print('OH NOOOOOOO!!!! I am loosing conciousnesssssss..........')
                        choice = input('Do you want to continue playing? \n(y/n)\n')
                        choice = choice.upper()
                        while choice not in ['Y', 'N', 'YES', 'NO']:
                            print('that was an invalid selection please try again')
                            choice = input('Do you want to continue playing? \n(y/n)\n')
                            choice = choice.upper()
                        if 'Y' in choice or 'YES' in choice:
                            level_1()
                        elif 'N' in choice or 'NO' in choice:
                            print('Thank you for playing Prison Scape! Have a great day! :D')
                            leave()
                else:
                    print('Something went wrong in this long winded nested loop but hey at least I tried to code!')

def level_4():
    time.sleep(3)
    from random import randint
    lives = 3
    steps = 7
    print ('Ohhhhhh a straight path! This is going to be easyyyyy!!!!')
    input('<Press Enter to Continue>')
    print(f"""For this level I think I hae to step on two of the three bricks carefully....
    \none too many wrong moves and I don't know where I will end up
    I think I have {lives} chances to slip up and there are {steps} steps
    I might need to put both my feet onto one stone""")
    time.sleep(2)
    print ("Something is written on the first step...."
           "\nAre you trying to feel terrified and alone. And regret every decision you’ve ever made, drenched in a cold sweat."
           "\nGo to sleep. Maybe you’ve heard of it...."
           "I can't get discouraged now!!!!")
    while steps > 0:
        steps -= 1
        doom_1 = str(randint (1,3))
        doom_2 = str(randint (1,3))
        print (doom_1)
        print (doom_2)
        print('Which two stones should I step on? I should choose it one by one....')
        step_1 = input("My first step?\n(1,2 or 3)\n")
        step_2 = input("My second step?\n(1,2 or 3)\n")
        while step_1 not in ['1','2','3'] and step_2 not in ['1','2','3']:
            print('One of your choices was invalid... please try again')
            step_1 = input("My first step?\n(1,2 or 3)\n")
            step_2 = input("My second step?\n(1,2 or 3)\n")
        if (step_2 == doom_2 or step_2 == doom_1) and (step_1 == doom_1 or step_1 == doom_2):
            time.sleep(1)
            print (f"""Both my guesses were correct! phewwwwww
            I still have {steps} to go""")
        elif (step_1 != doom_1 or step_1 != doom_2) and (step_2 == doom_1 or step_2 == doom_2):
            time.sleep(3)
            print (f"""Phewww I almost slipped!!!! I am getting more and more unnerved I see!
            I still have {steps} to go! """)
            lives -= 0.5
            if lives == 0:
                print('Noooooooooo.... I slipped and fell..... the fall is unbearing!!!\nWait I am back at the staircases!')
                choice = input('Do you want to continue playing? \n(y/n)\n')
                choice = choice.upper()
                while choice not in ['Y', 'N', 'YES', 'NO']:
                    print('that was an invalid selection please try again')
                    choice = input('Do you want to continue playing? \n(y/n)\n')
                    choice = choice.upper()
                if 'Y' in choice or 'YES' in choice:
                    level_2()
                elif 'N' in choice or 'NO' in choice:
                    print('Thank you for playing Prison Scape! Have a great day! :D')
                    leave ()
        elif (step_2 != doom_1 or step_2 != doom_2) and (step_1 == doom_1 or step_1 == doom_2):
            time.sleep(3)
            print (f"""Phewww I almost slipped!!!! I am getting more and more unnerved I see!
            I still have {steps} to go! """)
            lives -= 0.5
            if lives == 0:
                print('Noooooooooo.... I slipped and fell..... the fall is unbearing!!!\nWait I am back at the staircases!')
                choice = input('Do you want to continue playing? \n(y/n)\n')
                choice = choice.upper()
                while choice not in ['Y', 'N', 'YES', 'NO']:
                    print('that was an invalid selection please try again')
                    choice = input('Do you want to continue playing? \n(y/n)\n')
                    choice = choice.upper()
                if 'Y' in choice or 'YES' in choice:
                    level_2()
                elif 'N' in choice or 'NO' in choice:
                    print('Thank you for playing Prison Scape! Have a great day! :D')
                    leave()
            else:
                continue
        elif (step_1 != doom_1 or step_1 != doom_2) and (step_2 != doom_1 or step_2 != doom_2):
            time.sleep(4)
            print (f"""Phewww I slipped but I caught on somehow!!!! I am really unnerved I see!
            I still have {steps} to go! """)
            lives -= 1
            if lives == 0:
                print('Noooooooooo.... I slipped and fell..... the fall is unbearing!!!\nWait I am back at the staircases!')
                choice = input('Do you want to continue playing? \n(y/n)\n')
                choice = choice.upper()
                while choice not in ['Y', 'N', 'YES', 'NO']:
                    print('that was an invalid selection please try again')
                    choice = input('Do you want to continue playing? \n(y/n)\n')
                    choice = choice.upper()
                if 'Y' in choice or 'YES' in choice:
                    level_2()
                elif 'N' in choice or 'NO' in choice:
                    print('Thank you for playing Prison Scape! Have a great day! :D')
                    leave()
            else:
                continue
    if steps == 0:
        print ('I finally made it!!!! Can\'t believe I did! Well let\'s see what comes next! ')
        if difficulty =='medium':
            print ('done!!!')
            completed()
        elif difficulty =='hard':
            print ('Onto the next level')
            level_5()
        else:
            print (404)
    else:
        print ('404')

def level_5 ():
    time.sleep(2)
    print  ("""
    This is the final level!!! It is the kings room ..... but it doesn't look like much!
    Let's look around.......""")
    time.sleep(2)
    print("""You spot a figure appearing from the shadows......
    The room started to chill down...... 
    (you start to see your breath)""")
    time.sleep(2)
    print ("""It's you!!!! 
    You .... you .... are a white walker!!!!!!!""")
    if 'Valerian Sword' in inventories:
        time.sleep(1)
        print(f"""I know that with this sword!!! I will win this battle!!!!!
        Well done in completing the game!!!! You are now the ruler of the castle... ALL HAIL {name} !

 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄    ▄       ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░▌  ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░▌ ▐░▌      ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌▐░▌       ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌▐░▌░▌        ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░▌         ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌▐░▌░▌         ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌▐░▌            ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▐░▌▐░▌ ▐░▌           ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░░▌▐░▌  ▐░▌          ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
      ▀       ▀         ▀  ▀         ▀  ▀        ▀▀  ▀    ▀            ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀
                                                                                                        """)

        final_decision = input("Would you like to play this game again? \n(y/n)\n")
        final_decision = final_decision.upper()
        while final_decision not in ['Y', 'N', 'YES', 'NO']:
            print('Sorry I don\'t think that would work, please try again!')
            final_decision = input("Would you like to play this game again? \n(y/n)\n")
            final_decision = final_decision.upper()
        if 'Y' in final_decision:
            final_decision_1 = input("Would you like to play this game in a different difficulty? \n(y/n)\n")
            final_decision_1 = final_decision_1.upper()
            while final_decision_1 not in ['Y', 'N']:
                print('Sorry that is not going to work :(')
                final_decision_1 = input("Would you like to play this game in a different difficulty? \n(y/n)\n")
                final_decision_1 = final_decision_1.upper()
            if 'Y' in final_decision_1:
                difficulty()
            elif 'N' in final_decision_1:
                intro()
            else:
                print('something went wrong!')
        else:
            exit()

    else:
        time.sleep(1)
        print ("""Oh nooooooo..... I don't have a valerian sword!!! So no matter what I cannot win but I can keep trying""")
        time.sleep(1)
        print(f'pant.....pant..... looks like this is it!')
        print (f'You fought well {name} .... too bad your time is up!!!!')
        time.sleep(3)
        white_walker()

def completed():
    print('And there you have it! You have escaped the Castle! Thank you for playing the game! :D '
          'Hope you enjoyed the game!')
    print(f'You ended with {inventories}')
    print ("""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄    ▄       ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░▌  ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░▌ ▐░▌      ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌▐░▌       ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌▐░▌░▌        ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░▌         ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌▐░▌░▌         ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌▐░▌            ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▐░▌▐░▌ ▐░▌           ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░░▌▐░▌  ▐░▌          ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
      ▀       ▀         ▀  ▀         ▀  ▀        ▀▀  ▀    ▀            ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀
                                                                                                        """)
    final_decision = input("Would you like to play this game again? \n(y/n)\n")
    final_decision = final_decision.upper()
    while final_decision not in ['Y', 'N', 'YES', 'NO']:
        print('Sorry I don\'t think that would work, please try again!')
        final_decision = input("Would you like to play this game again? \n(y/n)\n")
        final_decision = final_decision.upper()
    if 'Y' in final_decision:
        final_decision_1 = input("Would you like to play this game in a different difficulty? \n(y/n)\n")
        final_decision_1 = final_decision_1.upper()
        while final_decision_1 not in ['Y', 'N']:
            print('Sorry that is not going to work :(')
            final_decision_1 = input("Would you like to play this game in a different difficulty? \n(y/n)\n")
            final_decision_1 = final_decision_1.upper()
        if 'Y' in final_decision_1:
            difficulty()
        elif 'N' in final_decision_1:
            intro()
        else:
            print('something went wrong!')
    else:
        exit()

def leave():
    print ('You have chose to leave the game and did not complete it! Hope you try again soon and thank you!')
    print ("""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄    ▄       ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░▌  ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░▌ ▐░▌      ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌▐░▌       ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌▐░▌░▌        ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░▌         ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌▐░▌░▌         ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌▐░▌            ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▐░▌▐░▌ ▐░▌           ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░░▌▐░▌  ▐░▌          ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
      ▀       ▀         ▀  ▀         ▀  ▀        ▀▀  ▀    ▀            ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀
                                                                                                        """)

def white_walker():
    print("""
    Sorry you became a white walker!!!!! No you live eternally as the new knight of level 3
    MUHAHAHAHAHAHHAHA!!!!!!


 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄    ▄       ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░▌  ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░▌ ▐░▌      ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌▐░▌       ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌▐░▌░▌        ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░▌         ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌▐░▌░▌         ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌▐░▌            ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▐░▌▐░▌ ▐░▌           ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░░▌▐░▌  ▐░▌          ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
      ▀       ▀         ▀  ▀         ▀  ▀        ▀▀  ▀    ▀            ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀""")

    final_decision = input("Would you like to play this game again? \n(y/n)\n")
    final_decision = final_decision.upper()
    while final_decision not in ['Y', 'N', 'YES', 'NO']:
        print('Sorry I don\'t think that would work, please try again!')
        final_decision = input("Would you like to play this game again? \n(y/n)\n")
        final_decision = final_decision.upper()
    if 'Y' in final_decision:
        final_decision_1 = input("Would you like to play this game in a different difficulty? \n(y/n)\n")
        final_decision_1 = final_decision_1.upper()
        while final_decision_1 not in ['Y', 'N']:
            print('Sorry that is not going to work :(')
            final_decision_1 = input("Would you like to play this game in a different difficulty? \n(y/n)\n")
            final_decision_1 = final_decision_1.upper()
        if 'Y' in final_decision_1:
            difficulty()
        elif 'N' in final_decision_1:
            intro()
        else:
            print('something went wrong!')
    else:
        exit()

intro()
