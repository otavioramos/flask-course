friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]

# without list comprehensions
starts_s_standard = []

for friend in friends:
    if (friend.lower().startswith("s")):
        starts_s_standard.append(friend)

print(f"without list comprehensions: {starts_s_standard}")

# with list comprehensions
starts_s = [friend for friend in friends if friend.lower().startswith("s")]

print(f"with list comprehensions: {starts_s}")