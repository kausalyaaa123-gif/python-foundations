balance_amount=10000
withdrawal_amount=float(input("enter withdrawal amount"))
if withdrawal_amount<=0:
    print("Invalid amount entered.")
elif withdrawal_amount>balance_amount:
    print("Insufficient funds.")
else:
    remaining_balance=balance_amount-withdrawal_amount
    print(f"Transaction Successfull.Remaining balance:{remaining_balance}")

