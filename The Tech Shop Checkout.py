cart_amount=float(input("Enter cart total"))
if cart_amount >= 5000:
   print("Discount applied! Your final bill is: ",cart_amount-0.1*cart_amount)
else:
    print("no discount applied")
    
