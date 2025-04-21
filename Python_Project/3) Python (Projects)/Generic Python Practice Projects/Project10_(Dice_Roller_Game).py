import random

# UniCode Characters
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

dice_art = {
    1: (
            "┌─────────┐",
            "│                    │",
            "│        ●         │",
            "│                    │",
            "└─────────┘"),
    2: (
            "┌─────────┐",
            "│  ●               │",
            "│                    │",
            "│               ●  │",
            "└─────────┘"),
    3: (
            "┌─────────┐",
            "│  ●               │",
            "│         ●        │",
            "│                ● │",
            "└─────────┘"),
    4: (
            "┌─────────┐",
            "│ ●            ●  │",
            "│                    │",
            "│ ●            ●  │",
            "└─────────┘"),
    5: (
            "┌─────────┐",
            "│ ●            ●  │",
            "│        ●          │",
            "│ ●            ●  │",
            "└─────────┘"),
    6: (
            "┌─────────┐",
            "│ ●            ●  │",
            "│ ●            ●  │",
            "│ ●            ●  │",
            "└─────────┘"),
}
collection  = []
user_input = int(input("For how many times you want to roll a dice? : "))
for each_time in range(user_input):
    collection.append(random.randint(1,6))

for index in range(user_input):
    for line in dice_art.get(collection[index], ()):
        print(line)