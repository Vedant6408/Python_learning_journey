print("="*30)
wel = "WELCOME"
print(f"{wel.center(30,"-")}")
print("="*30)
stock_list_inp = input("do you wanna se what we've in stock?(y/n)")
# fruit_listand_price = ["Mango","Guava","Banana","Apple","Grapes"]
fruit_listand_price = {"Mango":5, "Guava":4, "Banana":3,"Apple":6,"Grapes":2 }
customer_list = []
running = True
while running:
    if stock_list_inp.capitalize() == "Y":
        for f, p in fruit_listand_price.items():
            print(f"{f}: ${p}")      


        
        while running:
            print("Wanna buy something Plz Add in the cart:(if you've finished type (stop)) ")
            item_cart = input("--->> ")
            if item_cart.capitalize() in fruit_listand_price:
                noof_item = int(input("How much ??(1piece/2peice...)\n--->> "))
                customer_list.append({item_cart.capitalize(): noof_item})
                print(f"{noof_item}x {item_cart} added to cart !")
            elif item_cart.lower() == "stop":
                print("\n-----Your Cart-----")
                for item in customer_list:
                    for item, qty in item.items():
                        total = 0
                        price = fruit_listand_price[item]
                        amount = price * qty
                        total += amount
                        print(f"{item} x{qty} = ${amount}")
                print(f"Your Total amount is: {total}")
                running = False
                
            
            else:
                print(f"{item_cart} is not in our stock !, PLZ SEE THE LIST BELOW !!")
                for f, p in fruit_listand_price.items():
                    print(f"{f}: ${p}")                 
        

    elif stock_list_inp.capitalize() == "N":
       while running:
            print("Okay then add items to cart !!(if you've finished type (stop))  ")
            item_cart = input("--->> ")
            if item_cart.capitalize() in fruit_listand_price:
                noof_item = int(input("How much ??(1piece/2peice...)\n--->> "))
                customer_list.append({item_cart.capitalize(): noof_item})
                print(f"{noof_item}x {item_cart} added to cart !")
            elif item_cart.lower() == "stop":
                print("\n-----Your Cart-----")
                for item in customer_list:
                    for item, qty in item.items():
                        total = 0
                        price = fruit_listand_price[item]
                        amount = price * qty
                        total += amount
                        print(f"{item} x{qty} = ${amount}")
                print(f"Your Total amount is: {total}")
                running = False

            else:
                print(f"{item_cart} is not in our stock !, PLZ SEE THE LIST BELOW !!")
                for f, p in fruit_listand_price.items():
                    print(f"{f}: ${p}")
        
       
            

    else:
        print("Invalid Input TRY AGain!")
        stock_list_inp = input("do you wanna see what we've in stock?(y/n)")
        continue
        
# Note: There are many error in this program, if we run this program simply
#  then it will run without any error if we do something  wrong input then it will
#  through error sometime it will handle but not all the time
# Note: There are many features are not given in this program 
