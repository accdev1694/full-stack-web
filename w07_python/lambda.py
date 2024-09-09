people = [
    {"name": "oloche", "house": "UK"},
    {"name": "James", "house": "Naija"},
    {"name": "Emma", "house": "USA"}
] 

people.sort(key=lambda person: person["name"])
print(people)