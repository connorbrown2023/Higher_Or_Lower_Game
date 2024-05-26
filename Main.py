from Game_Data import data
import random

# Display art.

# Generate a random account from data file.

account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b = random.choice(data)


# Format data into a printable format.

account_name = account_a["Name"]
follower_count = account_a["Follower Count"]
account_description = account_a["Description"]

# Ask user for a guess.

# Check if user is correct.
## Get followers account size
## Use an if statement to check if users guess is higher or lower

# Give user feedback

# Track their score

# Use a while loop to make repeatable

# Replacing position A with B in the printable format

# Clear the screens between rounds.

