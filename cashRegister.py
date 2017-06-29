def printMenu(menuItems, leftWidth, rightWidth):
    print('ECITY JAVA'.center(leftWidth + rightWidth, '-'))
    for k, v in menuItems.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
menuItems = {"drip coffee": 2.00, "latte": 3.48, "cappuccino": 3.48,
             "single espresso": 1.57, "double espresso": 2.05,
             "hot tea": 1.77, "chai tea": 3.81, "mocha": 3.81,
             "white mocha": 3.81, "caramel vanilla": 3.81,
             "chocoberry delux": 3.81, "cherrybomb": 3.81,
             "taste of nawlins": 3.81, "white elephant": 4.34,
             "dirty hippie": 3.98, "mint choco-chip": 3.81,
             "electric city surge": 3.57, "shot in the dark": 2.38,
             "black tiger": 4.34, "white tiger": 4.34, "muddy tiger": 4.34,
             "liger": 4.34, "oreo speedwagon": 4.34, "vanilla frosty joe": 3.86,
             "heath mocha frosty joe": 3.86, "fruit smoothie": 3.86,
             "cookie": 0.95, "bagel": 1.90, "danish": 1.90, "muffin": 1.90,
             "soda": 1.43, "water": 1.19
             }
printMenu(menuItems, 40, 12)
itemPrice = []

while True:
    order1 = input("Welcome customer to eCity Java! We are the greatest \
coffee shop in all of Anderson! What can I get for you today? \
(Type 'nothing' to quit) >>> ")
    if order1.lower() == 'nothing':
        break
    if order1.lower() in menuItems:
        print("Wonderful! And what else can I get for you today? >>> ")
        itemPrice.append(menuItems[order1] * 1.05)
        order2 = input()
        if order2.lower() == 'nothing':
            break
        if order2.lower() in menuItems:
            print("Sounds good. Anything else? >>> ")
            itemPrice.append(menuItems[order2] * 1.05)
            order3 = input()
            if order3.lower() == 'nothing':
                break
            if order3.lower() in menuItems:
                print("Gotcha. Would you like anything else? A cookie, maybe? >>> ")
                itemPrice.append(menuItems[order3] * 1.05)
                order4 = input()
                if order4.lower() == 'nothing':
                    break
                if order4.lower() in menuItems:
                    print("Okay fella. I'm going to have to cut you off there.")
                    itemPrice.append(menuItems[order4] * 1.05)
                    break
    else:
        print("Umm...well—that isn't on the menu. Let's start over, okay?")
        print()
        print()
        print()


total = 0
for int in itemPrice:
    total = total + int


thanks = input("Give me a moment and I'll make that for you! (Say thank you) >>> ")
if thanks.lower() == "thank you" or "thanks":
    print("You are most welcome! Please wait.")
    print("...")
    print("...")
    print("...")
    print("...")
    print("...")
else:
    print("Well aren't you something... Hold on.")
    print("...")
    print("...")
    print("...")
    print("...")
    print("...")
    print("Please be aware that this may affect your total. Jerk.")


print("...")
print("...")
print("...")
print("...")
print("...")
print("...")
print("...")

print("Okay! Here you are. Let me get your total.")

print("...")
print("...")
print("...")
print("...")
print("...")
print("...")
print("...")
print("...")
print("...")
print("...")
print("...")
print("...")

while True:
    payment = str(input("That comes out to $" + str(format(total, '.2f')) +
      ". And how will you be paying for that today? (card, cash, or check?) >>> "))
    
    if payment.lower() == "card":
        signature = input("Okay. Let me swipe that...\
And if you could just sign this for me, please? (sign your name) >>> ")
        print("Thank you " + signature +
              ". Here are your drinks. Enjoy, and have a wonderful day!")
        break
    
    elif payment.lower() == "cash":
        print("Okay. That looks like a $20? Your change comes out to $"
              + str(format(20 - total, '.2f')) +
              ". Thank you for coming to eCity Java!")
        break
    
    elif payment.lower() == "check":
        print("I'll...okay. I'll take that. *Looks at check* \
Just...I'll figure out what to do with this. Buh-bye.")
        break
    else:
        print("We don't take that kind of moon-man money. \
Give me something I can actually use. >>> ")
        print()
