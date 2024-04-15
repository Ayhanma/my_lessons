import random, sys
ALL_CLOSED = """
+------+        +------+        +======+
|   1  |        |   2  |        |   3  |
|      |        |      |        |      |
|      |        |      |        |      |
|      |        |      |        |      |
|      |        |      |        |      |
+------+        +------+        +------+
"""
FIRST_GOAT = """
+------+        +------+        +======+
|  ((  |        |   2  |        |   3  |
|  OO  |        |      |        |      |
| /_/|_|        |      |        |      |
|    | |        |      |        |      |
|GOAT| |        |      |        |      |
+------+        +------+        +------+
"""
SECOND_GOAT = """
+------+        +------+        +======+
|   1  |        |  ((  |        |   3  |
|      |        |  OO  |        |      |
|      |        | /_/|_|        |      |
|      |        |    | |        |      |
|      |        |GOAT|||        |      |
+------+        +------+        +------+
"""
THIRD_GOAT = """
+------+        +------+        +------+        
|   1  |        |   2  |        |  ((  |        
|      |        |      |        |  OO  |        
|      |        |      |        | /_/|_|        
|      |        |      |        |    | |        
|      |        |      |        |GOAT|||        
+------+        +------+        +------+        
"""
FIRST_CAR_OTHER_GOAT = """

+------+        +------+        +======+
| CAR! |        |  ((  |        |  ((  |
|     _|        |  OO  |        |  OO  |
|   _/ |        | /_/|_|        | /_/|_|
|  /_ _|        |    | |        |    | |
|    O |        |GOAT|||        |GOAT|||
+------+        +------+        +------+
"""
SECOND_CAR_OTHER_GOAT = """

+------+        +======+        +======+
|  ((  |        | CAR! |        |  ((  |
|  OO  |        |     _|        |  OO  |
| /_/|_|        |   _/ |        | /_/|_|
|    | |        |  /_ _|        |    | |
|GOAT|||        |    O |        |GOAT|||
+------+        +------+        +------+        
"""
THIRD_CAR_OTHER_GOAT = """

+------+        +======+        +======+
|  ((  |        |  ((  |        | CAR! |
|  OO  |        |  OO  |        |     _| 
| /_/|_|        | /_/|_|        |  _/  |
|    | |        |    | |        | /_ __|
|GOAT|||        |GOAT|||        |    O |
+------+        +------+        +======+
"""
input('Press enter to stast:')
swap_wins = 0
swap_loses = 0
stay_wins = 0
stay_loses = 0
while True:
    door_that_has_car = random.randint(1,3)
    print(ALL_CLOSED)
    while True:
        print('pick the door 1,2 or 3 or quit to stop:')
        response = input('> ')
        if response.lower() == 'quit':
            print('Thx for playing')
            sys.exit()
        if response == '1' or response == '2' or response == '3':
            break
    door_pick = int(response)
    while True:
        show_goat_door = random.randint(1,3)
        if show_goat_door != door_pick and show_goat_door != door_that_has_car:
            break
    if show_goat_door == 1:
        print(FIRST_GOAT)
    elif show_goat_door == 2:
        print(SECOND_GOAT)
    elif show_goat_door ==  3:
        print(THIRD_GOAT)
    print(f'door {show_goat_door} contains the goat')
    while True:
        swap = input('Do yo want to swap a door, YES or NO: ')
        if swap.lower() == 'yes' or swap.lower() == 'no':
            break
    if swap.lower() == 'yes':
        if door_pick == 1 and show_goat_door == 2:
            door_pick = 3
        elif door_pick == 2 and show_goat_door == 3:
            door_pick = 2
        elif door_pick == 2 and show_goat_door == 1:
            door_pick = 3
        elif door_pick == 2 and show_goat_door == 3:
            door_pick = 1
        elif door_pick == 3 and show_goat_door == 1:
            door_pick = 2
        elif door_pick == 3 and show_goat_door == 2:
            door_pick = 1
    if door_that_has_car == 1:
        print(FIRST_CAR_OTHER_GOAT)
    elif door_that_has_car == 2:
        print(SECOND_CAR_OTHER_GOAT)
    elif door_that_has_car == 3:
        print(THIRD_CAR_OTHER_GOAT)
    print(f'door {door_that_has_car} has the car')
    if door_pick == door_that_has_car:
        print('YOU WON')
        if swap.lower() == 'yes':
            swap_wins += 1
        elif swap.lower() == 'no':
            stay_wins += 1
    else:
        print('Sorry you lose')
        if swap.lower() == 'yes':
            swap_loses += 1
        if swap.lower() == 'no':
            stay_loses += 1
    total_swaps = swap_wins + swap_loses
    if total_swaps != 0:
        swap_success = round(swap_wins/total_swaps * 100,1)
    else:
        swap_success = 0.0
    total_stays = stay_wins + stay_loses
    if total_stays != 0:
        stays_success = round(stays_success/total_stays *100, 1)
    else:
        stays_success = 0.0
    print(f'swaping:{swap_wins} wins, {swap_loses} loses,succes rades {swap_success}')
    print(f'not swaping:{stay_wins} wins, {stay_loses} lose, stay success {stays_success}')
    input('press enter to continiue')