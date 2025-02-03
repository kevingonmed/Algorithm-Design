# 1. Name:
#      Kevin Gonzalez
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program determines if a player can build a hotel on Pennsylvania Avenue in Monopoly.
#      It checks various conditions such as ownership of green properties, available houses, and hotels.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this program was obtaining the results after asking the user, because while trying to follow the flowchart, I had to make some changes in order to reach the expected answer without making too many redundancies.
# 5. How long did it take for you to complete the assignment?
#      4-4:30 hours

# Ask for initial inputs
color_group = input("Do you own all the green properties? (y/n): ")
pc = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
nc = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
pa = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
houses = int(input("How many houses are there to purchase?: "))
hotels = int(input("How many hotels are there to purchase?: "))

# Check conditions
if color_group.lower() != 'y':
    print("You cannot purchase a hotel until you own all the properties of a given color group.")
elif pa == 5:
    print("You cannot purchase a hotel if the property already has one.")
elif nc == 5 and pa == 4:
    print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
elif pc == 5 and pa == 4:
    print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
else:
    # Calculate the number of houses needed for each property
    houses_needed_pc = max(0, 4 - pc)  # Houses needed for Pacific Avenue
    houses_needed_nc = max(0, 4 - nc)  # Houses needed for North Carolina Avenue
    houses_needed_pa = max(0, 4 - pa)  # Houses needed for Pennsylvania Avenue

    # Total houses and hotels needed
    total_houses_needed = houses_needed_pc + houses_needed_nc + houses_needed_pa
    total_hotels_needed = 1  # Always need 1 hotel

    # Check if there are enough houses and hotels available
    if houses < total_houses_needed:
        print("There are not enough houses available for purchase at this time.")
    elif hotels < total_hotels_needed:
        print("There are not enough hotels available for purchase at this time.")
    else:
        # Calculate the total cost
        house_cost = total_houses_needed * 200
        hotel_cost = total_hotels_needed * 200
        total_cost = house_cost + hotel_cost

        # Ask for cash
        cash = int(input("How much cash do you have to spend?: "))

        # Check if the user has enough cash
        if cash < total_cost:
            print("You do not have sufficient funds to purchase a hotel at this time.")
        else:
            # Output the purchase details based on the number of houses needed
            if houses_needed_pc > 0 and houses_needed_nc > 0:
                # Purchase A: Houses needed for both Pacific and North Carolina
                print(f"This will cost ${total_cost}.")
                print(f"Purchase 1 hotel and {total_houses_needed} house(s).")
                print("Put 1 hotel on Pennsylvania and return any houses to the bank.")
                print(f"Put {houses_needed_nc} house(s) on North Carolina.")
                print(f"Put {houses_needed_pc} house(s) on Pacific.")
            elif houses_needed_nc > 0:
                # Purchase B: Houses needed for North Carolina only
                print(f"This will cost ${total_cost}.")
                print(f"Purchase 1 hotel and {total_houses_needed} house(s).")
                print("Put 1 hotel on Pennsylvania and return any houses to the bank.")
                print(f"Put {houses_needed_nc} house(s) on North Carolina.")
            elif houses_needed_pc > 0:
                # Purchase C: Houses needed for Pacific only
                print(f"This will cost ${total_cost}.")
                print(f"Purchase 1 hotel and {total_houses_needed} house(s).")
                print("Put 1 hotel on Pennsylvania and return any houses to the bank.")
                print(f"Put {houses_needed_pc} house(s) on Pacific.")
            else:
                # Purchase D: No houses needed for Pacific or North Carolina
                print(f"This will cost ${total_cost}.")
                print(f"Purchase 1 hotel and {total_houses_needed} house(s).")
                print("Put 1 hotel on Pennsylvania and return any houses to the bank.")