from art import logo, vs
from game_data import data
import random

#print(logo)
#print(data[0].get('name'))
#print(len(data))
#print(f"Compare A: ")
count = 0

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
  account_b = random.choice(data)
  
name_a = account_a['name']
follower_count_a = account_a['follower_count']
description_a = account_a['description']
country_a = account_a["country"]
print(logo)

should_continue = True

while(should_continue):

  print(f"Compare A: {name_a}, a {description_a} from {country_a}")
  
  name_b = account_b['name']
  follower_count_b = account_b['follower_count']
  description_b = account_b['description']
  country_b = account_b["country"]
  
  print(vs)
  print(f"Against B: {name_b}, a {description_b} from {country_b}")
  
  user_choice = input("Who has more followers? Type 'A' or 'B': ")
  
  if user_choice == "A":
      if follower_count_a > follower_count_b:
          count += 1
          print(f"You're right. Current score: {count}.")
          account_b = random.choice(data)
          if account_a == account_b:
            account_b = random.choice(data)
          
      else:
          print(f"you lost on count: {count}.")
          should_continue = False
            
  elif user_choice == "B":
      if follower_count_b > follower_count_a:
          count += 1
          print(f"You're right. Current score: {count}. ")
          name_a = name_b
          description_a = description_b
          country_a = country_b
          account_b = random.choice(data)
          if account_b == account_a:
            account_b = random.choice(data)
      else:
          print(f"You lost on count {count}.")
          should_continue = False
          
  else:
      print("Please, enter valid entry.")
      should_continue = False
