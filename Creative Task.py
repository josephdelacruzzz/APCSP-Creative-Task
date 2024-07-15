## INTRODUCTION
import math
print(" ")
print("Welcome to my DEPARTMENT store!")
print("You can buy all types of clothing from here!")

## DEFINITIONS OF LISTS
MAIN = [" ", "===============CATEGORIES===============", "Headwear", "Tops", "Bottoms", "Shoes", "Checkout" ]
HEADWEAR = ["Cap - $5.55", "Fedora - $20.20", "Beanie - $10.45", "Beret - $30.15"]
TOPS = ["Shirt - $10.10", "Jacket - $27.27", "Hoodie - $35.35", "Tunic - $18.39"]
BOTTOMS = ["Khakis - $23.23", "Jeans - $25.16", "Leggings - $20.21", "Trousers - $22.22"]
SHOES = ["Heels - $24.24", "Sneakers - $30.33", "Boots - $32.23", "Loafers - $35.53"]
CART = []
CART2 = []
## END OF DEFINITIONS

##CONTINUE
while True:
    print(*MAIN, sep="\n")
    print("----------------------------------------")
    CHOICE = input("Which category will you choose?")
    if CHOICE == "Headwear":
        print("===========HEADWEAR OPTIONS===========")
        print(*HEADWEAR, sep="\n")
        print("--------------------------------------")
        CHOICE2 = input("Choice: ")
        CART.append(CHOICE2)
        if CHOICE2 == "Cap":
            CART2.append(5.55)
        if CHOICE2 == "Fedora":
            CART2.append(20.20)
        if CHOICE2 == "Beanie":
            CART2.append(10.45)
        if CHOICE2 == "Beret":
            CART2.append(30.15)
        print(CART)
        print(CART2)
    elif CHOICE == "Tops":
        print("===========TOPS OPTIONS===========")
        print(*TOPS, sep="\n")
        print("----------------------------------")
        CHOICE2 = input("Choice: ")
        CART.append(CHOICE2)
        if CHOICE2 == "Shirt":
            CART2.append(10.10)
        if CHOICE2 == "Jacket":
            CART2.append(27.27)
        if CHOICE2 == "Hoodie":
            CART2.append(35.35)
        if CHOICE2 == "Tunic":
            CART2.append(18.39)
        print(CART)
        print(CART2)
    elif CHOICE == "Bottoms":
        print("===========BOTTOMS OPTIONS===========")
        print(*BOTTOMS, sep="\n")
        print("-------------------------------------")
        CHOICE2 = input("Choice: ")
        CART.append(CHOICE2)
        if CHOICE2 == "Khakis":
            CART2.append(23.23)
        if CHOICE2 == "Jeans":
            CART2.append(25.16)
        if CHOICE2 == "Leggings":
            CART2.append(20.21)
        if CHOICE2 == "Trousers":
            CART2.append(22.22)
        print(CART)
        print(CART2)
    elif CHOICE == "Shoes":
        print("===========SHOES OPTIONS===========")
        print(*SHOES, sep="\n")
        CHOICE2 = input("Choice: ")
        print("-----------------------------------")
        CART.append(CHOICE2)
        if CHOICE2 == "Heels":
            CART2.append(24.24)
        if CHOICE2 == "Sneakers":
            CART2.append(30.33)
        if CHOICE2 == "Boots":
            CART2.append(32.23)
        if CHOICE2 == "Loafers":
            CART2.append(35.53)
        print(CART)
        print(CART2)
    elif CHOICE == "Checkout":
        break
    else:
        print("That is not a valid option.")

print("")
print("===========SUBTOTAL===========")
Price = sum(CART2)
print("Your subtotal is: $" +str(Price))
ANSWER = input("Would you like to round up to donate?")
if ANSWER == "Yes":
  ROUND = math.ceil(Price)
  print("We added a free bracelet for rounding up!")
  CART.append("Bracelet")

print("")
print("=============CART=============")
print("Here are the items in your cart:")
print(*CART, sep="\n")
print("------------------------------")
print("Your total is: $" + str(ROUND))
print(" - Thank You for Shopping With Us ! -")


