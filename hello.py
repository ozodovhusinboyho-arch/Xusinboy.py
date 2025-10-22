while True:
    category= input("Enter item category(or'done'to finish):")  
    if category =="done":
        break
    if category=='student':
        price=2
    elif category=='regular':
        price=4
    elif category=='premium':
        price=6
    else:
        print("Other choise.Try again.")
        continue

    subtotal = 0  # Must be outside the loopstudent

    subtotal = subtotal + price
    
# After loop, apply discount if applicable
    discount= 0
    if subtotal >= 15.00:
         discount = subtotal*0.17 #17% # Fixed amount, not a percentage

    final_total = subtotal - discount

print("\n--- Final Result ---")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: -${discount:.2f}")
print(f"Total to Pay: ${final_total:.2f}")
     