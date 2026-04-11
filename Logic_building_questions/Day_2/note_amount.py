# print("________________________________")
# print("This is notes counting program.")
# print("================================") 
# print("Here is only 10")   
# a = int(input("Enter your amount:"))

def count_notes(amount, denominations=None):
    if denominations is None:
        denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

    denominations.sort(reverse=True)  # largest first
    result = {}

    for note in denominations:
        if amount <= 0:
            break
        count = amount // note      # how many of this note fit?
        if count > 0:
            result[note] = count
            amount -= note * count  # subtract what we used

    return result

# --- Try it ---
amount = 5000
notes = count_notes(amount)

print(f"Amount: ₹{amount}")
print("-" * 25)
total_notes = 0
for note, count in notes.items():
    print(f"₹{note:>5} note  x  {count}")
    total_notes += count
print("-" * 25)
print(f"Total notes: {total_notes}")