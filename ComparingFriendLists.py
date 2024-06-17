paul_friends = ["Mary", "Tim", "Mike", "Henry"]
tina_friends = ["Tim", "Susan", "Mary", "Josh"]

combined_friends = []

for paul_name in paul_friends:
    for tina_name in tina_friends:
        if paul_name == tina_name:
            combined_friends.append(paul_name)
            
print(combined_friends)