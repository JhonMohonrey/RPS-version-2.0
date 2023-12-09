print("==========================================")
print(" Welcome to RPS version 2.0")
print(" Creator: Mohonrey")
print("==========================================")
print("1: Play")
print("2: Exit")

players = "False"
play = "NA"
isExit = "False"

#this is for special value --------->
DataList = [
    "Mohon", "mohon", "MOHON", "mohonrey", "Mohonrey", "MOHONREY"
]
specialMenu = "regular"
#this is for special value --------->

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
        print("1: Difficulty")
        print("2: Bot Rename")
        print("3: Change Rounds")
        print("4: God Mode")
        print("5: Back to regular Menu")
        
        advanceMenuSection = "False"

        while advanceMenuSection == "False" :
            advanceData = [
                "Mohon", "mohon", "MOHON", "mohonrey", "Mohonrey", "MOHONREY"
            ]

            print("")
            advanceSelect = input("Choose an option ROOT: ")
            print("")

            scanAdvance = -1
            justRecognize = "False"

            while scanAdvance < 5 :
                scanAdvance += 1

                #incase player still type my name :)
                if advanceSelect == advanceData[scanAdvance] :
                    print("===============================================")
                    print(' You Enter ' + '"' + advanceSelect + '"' + " Creator name recognized!")
                    print(" But still Invalid please Choose 1 to 5 ")
                    print("===============================================")
                    print("1: Difficulty")
                    print("2: Bot Rename")
                    print("3: Change Rounds")
                    print("4: God Mode")
                    print("5: Back to regular Menu")

                    justRecognize = "True"

            try :
                AdvanceConvert = int(advanceSelect) 

                if AdvanceConvert >= 6 :
                    print('"' + advanceSelect + '"' + " is not recognized")

                # Continue...
                # if AdvanceConvert == 1 :
                # if AdvanceConvert == 2 :
                # if AdvanceConvert == 3 :
                # if AdvanceConvert == 4 :
                        
                if AdvanceConvert == 5 :
                    dataList = -1
                    checkForSpecialValue = 20
                    specialMenu = "regular"
                    advanceMenuSection = "True"
                    print("==========================================")
                    print(" Advance Menu Exit Successful...")
                    print("==========================================")
                    print("")
                    print("1: Play")
                    print("2: Exit")
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

while play == "play" :
    print("He wants to play!!!!!!!!!!!")
    break

if isExit == "True" :
    print("==================================================")
    print(" Thank you for playing my simple RPS game")
    print(" -Mohonrey- ")
    print("                Date created: Dec 8, 2023")
    print("==================================================")
    print("")
    input("Hit Enter...")