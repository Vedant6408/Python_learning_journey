# fruits = ["Apple","Orange","Strawberry","Blue Berries"]
# vegetables = ["Potato","Tomato","Ginger","Lady's Fingers","Groud","Bitter Groud"]
# Non_veg_items = ["Egg","Meat","Chicken","Fish"]
# matrix = [fruits,vegetables,Non_veg_items]
# print(matrix[2][2])

#We can also define 2dmatrix without defining 3 or move variable 

groceries = [
    ["Close up", "Colgate","Colgate maxfresh"],
    ["Mixture","Biscuit","Kurkure","Chips"],
    ["Wheel","Surf excel"]
]

# print(groceries[2][1]) #third rows are the rows of detergent poweder brand and i acces that surf excel element

#iterating element using for loop
for items in groceries:
    for food in items:
        print(f"--{food}--")