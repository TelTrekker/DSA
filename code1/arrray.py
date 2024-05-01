users_onboard = []
users_onlobby = []

def join(user):
    users_onlobby.append(user)

def cancel_join():
    users_onlobby.pop()

def admit_all():
    for i in range(len(users_onlobby)):
        users_onboard.append(users_onlobby[i])
    users_onlobby.clear()

def admit():
    for i in range(len(users_onlobby)):
        print(f'user_id: {i}, user_name: {users_onlobby[i]}')
    id = input('select user_id to admit: ')
    id = int(id)

    user = users_onlobby[id]
    users_onboard.append(user)
    users_onlobby.remove(user)

def kick(user):
    users_onboard.remove(user)

def end_call():
    users_onboard.clear()

join('chris')
join('rafael')
join('mj')
join('jay')

print(users_onlobby)
print(users_onboard)

admit()

print(users_onlobby)
print(users_onboard)

