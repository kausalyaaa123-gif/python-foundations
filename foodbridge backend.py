accepted_weights = []

accepting_donations = True
print("--- Food-Bridge Backend System Initialized ---")

while accepting_donations:
    weight_kgs = float(input("\nEnter the weight of food to be donated (kg): "))
    hours = float(input("Enter the hours since the food has been cooked: "))
    
    if weight_kgs > 0 and hours < 4:
        print("Donation Accepted! Routing to nearest NGO.")
        accepted_weights.append(weight_kgs)
    else:
        print("Donation Rejected: Fails health and safety standards.")
        
    # 3. The Exit Strategy
    check_again = input("\nProcess another donation? (yes/no): ").strip().lower()
    if check_again == "no":
        accepting_donations = False
        print("\nSystem shutting down.")
        
        print(accepted_weights)
