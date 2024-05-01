# Lists to keep track of users in the lobby and onboard
users_onboard = []
users_onlobby = []


# Function to add a user to the lobby
def join(user):
  users_onlobby.append(user)
  print(f"{user} joined the lobby.")


# Function to cancel a user's join request
def cancel_join():
  if users_onlobby:
    user_canceled = users_onlobby.pop()
    print(f"{user_canceled}'s join request has been canceled.")
  else:
    print("No users in the lobby to cancel.")


# Function to admit all users from the lobby to the onboard list
def admit_all():
  for user in users_onlobby:
    users_onboard.append(user)
  users_onlobby.clear()
  print("All users in the lobby have been admitted.")


# Function to admit a specific user from the lobby
def admit():
  if users_onlobby:
    print("Users in the lobby:")
    for iteration, user in enumerate(users_onlobby):
      print(f"user_id: {iteration}, user_name: {user}")

    user_id = input('Select user_id to admit: ')

    # Convert user input to an integer
    try:
      user_id = int(user_id)
    except ValueError:
      print("Invalid input. Please enter a valid user_id.")
      return

    if 0 <= user_id < len(users_onlobby):
      user = users_onlobby[user_id]
      users_onboard.append(user)
      users_onlobby.remove(user)
      print(f"{user} has been admitted.")
    else:
      print("Invalid user_id. Please select a valid user_id.")
  else:
    print("No users in the lobby to admit.")


# Function to kick a user from the onboard list
def kick(user):
  if user in users_onboard:
    users_onboard.remove(user)
    print(f"{user} has been kicked from the call.")
  else:
    print(f"{user} is not in the call.")


# Function to end the call and clear the onboard list
def end_call():
  users_onboard.clear()
  print("The call has ended.")


# Sample usage of the conferencing app
join('Chris')
join('Rafael')
join('MJ')
join('Jay')

print("\nUsers in the lobby:")
print(users_onlobby)
print("\nUsers onboard:")
print(users_onboard)

admit()

print("\nUsers in the lobby:")
print(users_onlobby)
print("\nUsers onboard:")
print(users_onboard)

# Example of kicking a user
kick('Chris')

print("\nUsers in the lobby:")
print(users_onlobby)
print("\nUsers onboard:")
print(users_onboard)

# Example of ending the call
end_call()

print("\nUsers onboard after ending the call:")
print(users_onboard)
