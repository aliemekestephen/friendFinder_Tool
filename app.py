#This app will have a list of registered user
#Then it will be able to tell if a friend is near by entering his name
#currently the project is just started and will go through many stages

#getting the friends from the console
friends = input('Enter three friends names, separated by commas (no spaces, please): ').split(',')
print(friends)

#reading the registered users from a file later updated to a database
users = open('Users.txt', 'r')
users_nearby = [line.strip() for line in users.readlines()]
users.close()

friends_set = set(friends)
users_nearby_set = set(users_nearby)

friends_nearby_set = friends_set.intersection(users_nearby_set)

nearby_users = open('nearby_users.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_users.write(f'{friend}\n')

nearby_users.close()

#update to database


