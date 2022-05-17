# Task: Open reminders.txt, which contains a list of reminders, and print a random one out.
import random
import yaml

with open('reminders.txt') as f: categories = yaml.load(f.read(), Loader=yaml.FullLoader)

category_names = list(categories.keys())
category_name = random.choice(category_names)

lines = categories[category_name]
line = lines[random.randint(0, len(lines) - 1)]
print(line.strip() + " #" + category_name.replace(' ', ''))
