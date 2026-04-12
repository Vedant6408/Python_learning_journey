print("="*30)
wel = "WELCOME"
print(f"{wel.center(30,"-")}")
print("="*30)
stock_list_inp = input("do you wanna se what we've in stock?(y/n)")
# fruit_listand_price = ["Mango","Guava","Banana","Apple","Grapes"]
fruit_listand_price = {"Mango":5, "Guava":4, "Banana":3,"Apple":6,"Grapes":2 }
customer_list = []
while True:
    if stock_list_inp.capitalize() == "Y":
        for f, p in fruit_listand_price.items():
            print(f"{f}: ${p}")
        print("Wanna buy something Plz Add in the cart:  ")
        item_cart = input("--->> ")
        if item_cart.capitalize() in fruit_listand_price:
            noof_item = int(input("How much ??(1piece/2peice...)\n--->> "))
            customer_list.append({item_cart.capitalize(): noof_item})
            print(f"{noof_item}x {item_cart} added to cart !")
        else:
            print(f"{item_cart} is not in our stock !")
    elif stock_list_inp.capitalize() == "N":
        print("Okay Then Add items to cart!")
        item_cart = input("--->> ")
        if item_cart.capitalize() in fruit_listand_price:
            noof_item = int(input("How much ??(1piece/2peice...)\n--->> "))
            customer_list.append({item_cart.capitalize(): noof_item})
            print(f"{noof_item}x {item_cart} added to cart !")
    else:
        print("Invalid Input TRY AGain!")
        stock_list_inp = input("do you wanna se what we've in stock?(y/n)")
        continue
        
# print("*"*30)
# print("")
