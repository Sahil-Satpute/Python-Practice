import random
def starte():
    c= input("Enter your choise(choise must be \"snake\",\"water\"and\"gun\"):")
    
    if c == "snake" or c == "water" or  c == "gun":
        return game(c)
    else:
        print("invalid option")
        return starte() 
def game(choise):
    num = random.randint(1,4)
    
    
    ai_choise=""
    # takig ai choise
    if(num == 1):
        ai_choise="snake"
    elif(num == 2):
        ai_choise="gun"
    elif(num == 3):
        ai_choise="water"
    def win():
        print("You Win, Computer loss")
        print("ai choise is ",ai_choise)
    def loss():
        print("You Loss,Computer Wins")
        print("ai choise is ",ai_choise)
    if(ai_choise=="snake" and choise== "water"):
        return loss()
    if(ai_choise=="water" and choise== "gun"):
        return loss()
    if(ai_choise=="gun" and choise== "snake"):
        return loss()

# excute main bolck of code
    if(choise=="snake" and ai_choise== "water"):
        return win()
    if(choise=="water" and ai_choise== "gun"):
        return win()
    if(choise=="gun" and ai_choise== "snake"):
        return win()
    if(ai_choise==choise):
        print("There is draw no one wins")
        print("ai choise is ",ai_choise)
    


starte()