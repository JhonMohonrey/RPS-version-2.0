print("==========================================")
print(" Welcome to RPS version 2.0")
print(" Creator: Mohonrey")
print("==========================================")
print("1: Play")
print("2: Exit")
print("Hint: Type Mohon!")

players = "False"
play = "NA"
isExit = "False"

rounds = 5
Bot_name = "Bot"
ai_bot = "default"

DataList = [
    "Mohon", "mohon", "MOHON", "mohonrey", "Mohonrey", "MOHONREY"
]
specialMenu = "regular"

while players == "False" :

    if specialMenu == "regular" :
        print("")
        playerValue = input("Choose an option: ")
        print("")
    
    #this is for special value --------->
    dataList = -1
    checkForSpecialValue = 20

    while dataList < 5 :
        dataList += 1
        convertData = int(dataList)

        if playerValue == DataList[convertData] :
            checkForSpecialValue = 100

        if dataList == 5 and checkForSpecialValue == 20 :
            checkForSpecialValue = 50

#=======================================================================
    if checkForSpecialValue == 100:
        specialMenu = "spacial"
        
        print("==========================================")
        print(" Welcome to Advance Menu")
        print("==========================================")
        print("1: Change Rounds")
        print("2: Bot Rename")
        print("3: Difficulty")
        print("4: Back to regular Menu")
        
        advanceMenuSection = "False"

        while advanceMenuSection == "False" :
            advanceData = [
                "Mohon", "mohon", "MOHON", "mohonrey", "Mohonrey", "MOHONREY"
            ]
            
            if rounds != 5 :
                print("")
                print("==========================================")
                print(" Welcome to Advance Menu")
                print("==========================================")
                print("1: Change Rounds")
                print("2: Bot Rename")
                print("3: Difficulty")
                print("4: Back to regular Menu")

            if Bot_name != "Bot" :
                print("")
                print("==========================================")
                print(" Welcome to Advance Menu")
                print("==========================================")
                print("1: Change Rounds")
                print("2: Bot Rename")
                print("3: Difficulty")
                print("4: Back to regular Menu")

            if ai_bot == "Medium" :
                print("")
                print("==========================================")
                print(" Welcome to Advance Menu")
                print("==========================================")
                print("1: Change Rounds")
                print("2: Bot Rename")
                print("3: Difficulty")
                print("4: Back to regular Menu")

            if ai_bot == "Normal" :
                print("")
                print("==========================================")
                print(" Welcome to Advance Menu")
                print("==========================================")
                print("1: Change Rounds")
                print("2: Bot Rename")
                print("3: Difficulty")
                print("4: Back to regular Menu")

            print("")
            advanceSelect = input("Choose an option: ")
            print("")

            scanAdvance = -1
            justRecognize = "False"

            while scanAdvance < 5 :
                scanAdvance += 1

                if advanceSelect == advanceData[scanAdvance] :
                    print("===============================================")
                    print(' You Enter ' + '"' + advanceSelect + '"' + " Creator name recognized!")
                    print(" But still Invalid please Choose 1 to 5 ")
                    print("===============================================")
                    print("1: Change Rounds ")
                    print("2: Bot Rename")
                    print("3: Difficulty")
                    print("4: Back to regular Menu")

                    justRecognize = "True"

            try :
                AdvanceConvert = int(advanceSelect) 

                if AdvanceConvert >= 5 :
                    print('"' + advanceSelect + '"' + " is not recognized")


                #======(Change Rounds)======>
                while AdvanceConvert == 1 :
                    try :
                        if AdvanceConvert == 1:
                            print("")
                            print("=================================")
                            print("  Change Rounds")
                            print("=================================")
                            print(" Current Rounds: " + '"' + str(rounds) + '"')

                            set_rounds = input(" Set New Rounds: ") or 1

                            if set_rounds == "1"  or set_rounds == 1 or set_rounds == "0" or set_rounds == 0 or set_rounds.isspace() or len(set_rounds) > 3 or int(set_rounds) > 100 or int(set_rounds) < 1 or int(set_rounds) == 5:
                                AdvanceConvert == 1

                                if int(set_rounds) == 5 :
                                    print("")
                                    print(' "' + str(set_rounds) + '"' + " That's Default Round")
                                if int(set_rounds) != 5 :
                                    print("")
                                    print(' "' + str(set_rounds) + '"' + " Choose between 2-100")
                            else :
                                new_round = int(set_rounds)
                                rounds = new_round
                                print("")
                                print("=================================")
                                print(' Round has change to:', str(new_round))
                                print("=================================")
                                AdvanceConvert = 0
                    except :
                        print("")
                        print('"' + set_rounds + '"' + " is not recognize xx")
                        AdvanceConvert == 1
                #======(Change Rounds)======>

                #======(Bot Rename)=========>
                while AdvanceConvert == 2 :
                    try :
                        print("=============================")
                        print("Current Bot name:", Bot_name)
                        print("=============================")
                        print("")
                        user_input_BR = input("New Bot Name: ")

                        if user_input_BR.isnumeric() or user_input_BR.isspace() or len(user_input_BR) < 3 or len(user_input_BR) > 8 or user_input_BR == "Bot":
                            print("")
                            print('"' + user_input_BR + '"' + ' is not recognize')
                            print("")

                            if user_input_BR == "Bot" :
                                print("")
                                print('"' + user_input_BR + '"' + " That's current name!")
                                print("")
                        else :
                            print("")
                            print("=====================================")
                            print('Bot name Successfully Change...')
                            print("=====================================")
                            Bot_name = user_input_BR
                            AdvanceConvert = 0
                    except :
                        print('"' + user_input_BR + '"' + ' is not recognize')
                #======(Bot Rename)=========>
                
                #======(Difficulty)=========>
                while AdvanceConvert == 3 :
                    try :
                        print("=============================")
                        print(" Difficulty Setting")
                        print("=============================")
                        print("1: Normal")
                        print("2: Medium")
                        
                        print("")
                        user_diff = input("Choose an option YP: ")

                        difficulty_convert = int(user_diff)

                        if difficulty_convert > 2 :
                            print("")
                            print('"' + user_diff + '"' + " is not recognized")
                            print("")
                        else :
                            if difficulty_convert == 1 :
                                print("")
                                print("------------------------------")
                                print(" Difficulty Set to normal...")
                                print("------------------------------")
                                ai_bot = "Normal"
                                AdvanceConvert = 0
                                
                            if difficulty_convert == 2 :
                                print("")
                                print("------------------------------")
                                print(" Difficulty Set to Medium...")
                                print("------------------------------")
                                AdvanceConvert = 0
                                ai_bot = "Medium"
                    except :
                        print("")
                        print('"' + user_diff + '"' + "  is not recognize")
                        print("")

                #======(Difficulty)=========>

                if AdvanceConvert == 4 :
                    dataList = -1
                    checkForSpecialValue = 20
                    specialMenu = "regular"
                    advanceMenuSection = "True"
                    print("==========================================")
                    print(" Advance Menu Exit Successful...")
                    print("==========================================")
                    # print("")
                    # print("1: Play")
                    # print("2: Exit")

                    print("==========================================")
                    print(" Welcome to RPS version 2.0")
                    print(" Creator: Mohonrey")
                    print("==========================================")
                    print("1: Play")
                    print("2: Exit")
                    print("Hint: Type Mohon!")
            except :
                if justRecognize == "False" :
                    print('"' + advanceSelect + '"' + " is not recognized")

            # Difficulty Section
#======================================================================

    if checkForSpecialValue == 50 :
        try :
            playerOption = int(playerValue)

            if playerOption >= 3 :
                print('"' + playerValue + '"' + " is not recognized Type 1 or 2")
                players = "False"
            else :
                if playerOption == 1 :
                    play = "play"
                    players = "True"
                if playerOption == 2 :
                    isExit = "True"
                    players = "True"
        except :
            players = "False"
            print('"' + playerValue + '"' + " is not recognized Type 1 or 2")

    #this is for special value --------->

#====================(Menu)=============>
isRename = False

while play == "play" :
    set_player_name = input("Your name:") or "Player 1"

    for_len = len(set_player_name) < 3
    for_max_len = len(set_player_name) > 8
    for_num = set_player_name.isnumeric()
    for_space = set_player_name.isspace()

    if for_space or for_num or for_len or for_max_len:
        set_player_name = "Player 1"

    player_name = set_player_name
    isRename = True
    break

#=====(Main menu)=====>
while isRename == True :
    print("")
    print("==================================================")
    print(' "' + player_name + '"' + " Welcome to my RPS Game")
    print("==================================================")
    print("1: Rock")
    print("2: Paper")
    print("3: Scissors")

    # Play section =========>
    playing = True 
    current_rounds = 0
    player_score = 0
    Bot_score = 0

    while playing == True and current_rounds < rounds:

        #===(Choices)====
        if current_rounds > 0 :
            print("1: Rock")
            print("2: Paper")
            print("3: Scissors")
        #===(Choices)====

        #===(Players Pick)===
        player_pick = 0
        #===(Players Pick)===

        #===(Player section)===>
        print("")
        player_choice = input("Choose an option: ") or "Nan"
        print("")

        if player_choice == "Nan" :
            player_choice = "Nan"
        
        try :
            convert_player_choice = int(player_choice)

            if convert_player_choice > 3 :
                print('"' + str(convert_player_choice) + '"' + " This value is too much Type 1, 2 or 3")
                convert_player_choice = "Failed"

            if convert_player_choice == 1 :
                player_pick = 1
            if convert_player_choice == 2 :
                player_pick = 2
            if convert_player_choice == 3 :
                player_pick = 3
        except :
            # print("")
            print('"' + player_choice + '"' + " is not recognized")
            # print("")
        #===(Player section)===>

        #===(For Players)===
        if player_pick == 1 :
            current_rounds += 1
            print("==================================")
            print('         ===' + '(' + 'Round ' + str(current_rounds) + ')' + '===')
            print("==================================")
            print( ' "' + player_name + '"' + " Pick: Rock")

        if player_pick == 2 :
            current_rounds += 1
            print("==================================")
            print('         ===' + '(' + 'Round ' + str(current_rounds) + ')' + '===')
            print("==================================")
            print( ' "' + player_name + '"' + " Pick: Paper")

        if player_pick == 3 :
            current_rounds += 1
            print("==================================")
            print('         ===' + '(' + 'Round ' + str(current_rounds) + ')' + '===')
            print("==================================")
            print( ' "' + player_name + '"' + " Pick: Scissors")
        #===(For Players)===

        #===(For AI)===
        if player_pick == 1 or player_pick == 2 or player_pick == 3 :

            #===========(New AI)=========
            rock_bot2 = 0
            paper_bot2 = 0
            scissors_bot2 = 0

            if ai_bot == "Medium" :
                if rock_bot2 < 2 or paper_bot2 < 2 or scissors_bot2 < 2:
                    import random
                    bot_choice = random.randint(1, 3)

                if rock_bot2 > 2 :
                    import random
                    bot_choice = random.randint(2, 3)
                    rock_bot2 = 0

                if paper_bot2 > 2 :
                    import random
                    bot_choice = random.randint(1, 2)
                    paper_bot2 = 0

                    if bot_choice == 2 :
                        bot_choice = 3

                if scissors_bot2 > 2 :
                    import random
                    bot_choice = random.randint(1, 2)
                    scissors_bot2 = 0

                if bot_choice == 1 :
                    # print("rock_bot2")
                    print(' "' + Bot_name + '"' + ' Pick: Rock')
                    rock_bot2 += 1
                
                if bot_choice == 2 :
                    # print("paper_bot2")
                    print(' "' + Bot_name + '"' + ' Pick: Paper')
                    paper_bot2 += 1
                
                if bot_choice == 3 :
                    # print("scissors_bot2")
                    print(' "' + Bot_name + '"' + ' Pick: Scissors')
                    scissors_bot2 += 1
            #===========(New AI)=========

            #============(Normal AI)========*
            if ai_bot == "Normal" or ai_bot == "default":
                import random
                bot_choice = random.randint(1, 3)

                if bot_choice == 1 :
                    print(' "' + Bot_name + '"' + ' Pick: Rock')

                if bot_choice == 2 :
                    print(' "' + Bot_name + '"' + ' Pick: Paper')

                if bot_choice == 3 :
                    print(' "' + Bot_name + '"' + ' Pick: Scissors')
            #============(Normal AI)========*
        #===(For AI)===

        #===(Review Section)===>
        if player_pick == 1 and bot_choice == 1 :
            print("")
            print("  Rock vs Rock: Draw")
            print("==================================")
            print("")

        if player_pick == 1 and bot_choice == 2 :
            Bot_score += 1
            print("")
            print("  Rock vs Paper: You Loss")
            print("==================================")
            print("")

        if player_pick == 1 and bot_choice == 3 :
            player_score += 1
            print("")
            print("  Rock vs Scissors: You Win")
            print("==================================")
            print("")

        if player_pick == 2 and bot_choice == 1 :
            player_score += 1
            print("")
            print("  Paper vs Rock: You Win")

            print("==================================")
            print("")

        if player_pick == 2 and bot_choice == 2 :
            print("")
            print("  Paper vs Paper: Draw")

            print("==================================")
            print("")

        if player_pick == 2 and bot_choice == 3 :
            Bot_score += 1
            print("")
            print("  Paper vs Scissors: You Loss")

            print("==================================")
            print("")

        if player_pick == 3 and bot_choice == 1 :
            Bot_score += 1
            print("")
            print("  Scissors vs Rock: You Loss")

            print("==================================")
            print("")

        if player_pick == 3 and bot_choice == 2 :
            player_score += 1
            print("")
            print("  Scissors vs Paper: You Win")

            print("==================================")
            print("")

        if player_pick == 3 and bot_choice == 3 :
            print("")
            print("  Scissors vs Scissors: Draw")
            print("==================================")
            print("")
        #===(Review Section)===>

    print("")
    print("=====================================")
    print(' "' + player_name + '" Score: ' + str(player_score))
    print(' "' + Bot_name + '" Score: ' + str(Bot_score))
    print("")

    # Who win
    if player_score > Bot_score :
        print(' "' + player_name + '"' + ' Congrats You Win')
    if player_score < Bot_score :
        print(' "' + player_name + '"' + ' Sorry You Loss')
    if player_score == Bot_score :
        print(" ===(Draw)=== ")

    print("=====================================")
    # Play section =========>
    
    # Exit section =========>
    FailedData = True

    while FailedData == True :
        print("")
        print("1: Play again")
        print("2: Exit")

        print("")
        play_again = input("Choose an option: ") or "Empty_value"
        play_again_result = 0

        if play_again == "Empty_value" or play_again.isspace():
            play_again_result = "Letter"
            FailedData = True

            if play_again.isspace() :
                print("")
                print('"' + 'Space' + '"' + " is not recognized Type 1 or 2")

        else :
            try :
                play_again_result = int(play_again)

                if play_again_result > 2 :
                    print("")
                    print('"' + play_again + '"' + " This value is too much Type 1 or 2")
                    play_again_result = 0
            except :
                print("")
                print('"' + play_again + '"' + " is not recognized Type 1 or 2")
        
        if play_again_result == 1 :
            playing = True 
            FailedData = False

        if play_again_result == 2 :
            isExit = "True"
            isRename = False
            playing = False 
            FailedData = False
    # Exit section =========>
#=====(Main menu)=====>

#====================(Menu)=============>
if isExit == "True" :
    print("")
    print("==================================================")
    print(" Thank you for playing my simple RPS game")
    print(" -Mohonrey- ")
    print("                Date created: Dec 8, 2023")
    print("==================================================")
    print("")
    input("Hit Enter...")