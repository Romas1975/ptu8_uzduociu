import random

deck = []
cards1 = []
count1 = 0
cards2 = []
count2 = 0
cardnum = 29

cardcolour = "R"
for i in range (1,11):
    deck.append(cardcolour+str(i))
cardcolour = "B"
for i in range (1,11):
    deck.append(cardcolour+str(i))
cardcolour = "Y"
for i in range (1,11):
    deck.append(cardcolour+str(i))
    
print("Welcome to Card Game!")
print("Please enter your names.")
name1 = input("Player One: ")
name2 = input("Player Two: ")
print("Hello",name1,"and",name2,"here's how you play.")
print("You will each take a card that have a colour and a number.")
print("If both players pick cards of the same colour, the player with the highest number wins both cards.")
print("If they are different colours, a certain one will win.")
print("Red beats black. Yellow beats Red. Black beats yellow.")
while len(deck) != 0:
    print(name1,"press enter to draw a card.")
    input("> ")
    card1 = deck[random.randint(0,cardnum)]
    deck.remove(card1)
    cardnum = cardnum - 1
    print(name2,"press enter to draw a card.")
    input("> ")
    card2 = deck[random.randint(0,cardnum)]
    deck.remove(card2)
    cardnum = cardnum - 1
    print(name1+": "+card1)
    print(name2+": "+card2)
    if card1[0] == card2[0]:
        if card1[1] > card2[1]:
            print("Your cards are the same colour and "+name1+"'s card has a higher number.")
            print("Player one gets both cards.")
            cards1.append(card1)
            cards1.append(card2)
            count1 = count1 + 2
        else:
            print("Your cards are the same colour and "+name2+"'s card has a higher number.")
            print("Player two gets both cards.")
            cards2.append(card1)
            cards2.append(card2)
            count2 = count2 + 2
    else:
        if card1[0] == "R":
            if card2[0] == "B":
                print("Red beats black,",name1,"wins these cards.")
                cards1.append(card1)
                cards1.append(card2)
                count1 = count1 + 2
            if card2[0] == "Y":
                print("Yellow beats red,",name2,"wins these cards.")
                cards2.append(card1)
                cards2.append(card2)
                count2 = count2 + 2
        if card1[0] == "B":
            if card2[0] == "Y":
                print("Black beats yellow,",name1,"wins these cards.")
                cards1.append(card1)
                cards1.append(card2)
                count1 = count1 + 2
            if card2[0] == "R":
                print("Red beats black,",name2,"wins these cards.")
                cards2.append(card1)
                cards2.append(card2)
                count2 = count2 + 2
        if card1[0] == "Y":
            if card2[0] == "R":
                print("Yellow beats red,",name1,"wins these cards.")
                cards1.append(card1)
                cards1.append(card2)
                count1 = count1 + 2
            if card2[0] == "B":
                print("Black beats yellow,",name2,"wins these cards.")
                cards2.append(card1)
                cards2.append(card2)
                count2 = count2 + 2
if count1 > count2:
    print(name1,"got",count1,"cards out of 30 and wins this game.")
    print("Here are your cards:")
    print(cards1)
elif count2 > count1:
    print(name1,"got",count2," cards and wins this game.")
    print("Here are your cards:")
    print(cards1)
