numbers = []
while 1==1:
    userNum = input("Enter Number or 'stop' to stop: ")
    try:
        if userNum.lower() == "stop":
            sumNum = 0
            for i in numbers:
                sumNum += int(i)
            print("Your sum is: " + str(sumNum))
            break
        elif userNum.isnumeric() == False:
            print("That aint no number")
        else:
            numbers.append(userNum)
    except:
        print("u fucked up lole")

        

        
