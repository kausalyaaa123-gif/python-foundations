accepting_donations=True
while accepting_donations:

    weight_kgs=float(input("enter the weight of food to be donated:  "))
    hours=float(input("Enter the hours since the food hass been cooked: "))
    if weight_kgs > 0 and hours < 4:
        print("Donation Accepted! Routing to nearest NGO.")
    else:
        print("Donation Rejected: Fails health and safety standards.")
    check_again=input("can we process another donation(yes/no)").strip().lower()
    if check_again=="no":
        accepting_donations=False
        print("done for the day")
    else:
        accepting_donations=True
