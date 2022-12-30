from art import logo, vs
from game_data import data

#print(logo)
#print(data[0].get('name'))
#print(len(data))
#print(f"Compare A: ")
count = 0

for star in range(0, len(data)-1):
    name = data[star]['name']
    follower_count = data[star]['follower_count']
    description = data[star]['description']
    country = data[star]["country"]
    print(logo)

    print(f"Compare A: {name}, a {description} from {country}")
    next_name = data[star + 1]['name']
    next_follower_count = data[star + 1]['follower_count']
    next_description = data[star + 1]['description']
    next_country = data[star + 1]["country"]

    print(vs)
    print(f"Against B: {next_name}, a {next_description} from {next_country}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ")

    if user_choice == "A":
        if follower_count > next_follower_count:
            count += 1
            print(f"You're right. Current score: {count}.")

        else:
            print(f"you lost on count: {count}.")
            break

    elif user_choice == "B":
        if next_follower_count > follower_count:
            count += 1
            print(f"You're right. Current score: {count}. ")
        else:
            print(f"You lost on count {count}.")
            break
    else:
        print("Please, enter valid entry.")
        break
