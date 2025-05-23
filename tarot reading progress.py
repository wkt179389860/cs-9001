import random

# Tarot card meanings
tarot_cards = {
    "The Fool": {
        "upright": "New beginnings, adventure, innocence",
        "reversed": "Recklessness, irresponsibility, lack of planning"
    },
    "The Magician": {
        "upright": "Action, willpower, manifestation",
        "reversed": "Deception, manipulation, wasted potential"
    },
    "The High Priestess": {
        "upright": "Intuition, mystery, subconscious",
        "reversed": "Secrets, confusion, ignoring inner voice"
    },
    "The Empress": {
        "upright": "Fertility, creativity, nurturing",
        "reversed": "Dependence, laziness, creative block"
    },
    "The Emperor": {
        "upright": "Authority, stability, protection",
        "reversed": "Tyranny, rigidity, loss of control"
    },
    "The Hierophant": {
        "upright": "Tradition, guidance, structure",
        "reversed": "Rebellion, unconventionality, restriction"
    },
    "The Lovers": {
        "upright": "Relationships, harmony, choices",
        "reversed": "Temptation, conflict, separation"
    },
    "The Chariot": {
        "upright": "Victory, willpower, control",
        "reversed": "Aggression, lack of direction, obstacles"
    },
    "Strength": {
        "upright": "Courage, inner strength, patience",
        "reversed": "Fear, weakness, impulsiveness"
    },
    "The Hermit": {
        "upright": "Reflection, solitude, wisdom",
        "reversed": "Isolation, loneliness, avoidance"
    },
    "Wheel of Fortune": {
        "upright": "Change, luck, destiny",
        "reversed": "Bad luck, resistance to change, stagnation"
    },
    "Justice": {
        "upright": "Fairness, truth, law",
        "reversed": "Injustice, bias, avoidance of responsibility"
    },
    "The Hanged Man": {
        "upright": "Pause, letting go, new perspective",
        "reversed": "Stalling, martyrdom, useless sacrifice"
    },
    "Death": {
        "upright": "Transformation, endings, renewal",
        "reversed": "Resistance to change, stagnation"
    },
    "Temperance": {
        "upright": "Balance, healing, moderation",
        "reversed": "Imbalance, extremes, conflict"
    },
    "The Devil": {
        "upright": "Addiction, materialism, bondage",
        "reversed": "Freedom, breaking chains, enlightenment"
    },
    "The Tower": {
        "upright": "Sudden change, awakening, chaos",
        "reversed": "Avoiding disaster, fear of change"
    },
    "The Star": {
        "upright": "Hope, inspiration, peace",
        "reversed": "Despair, disconnection, false hopes"
    },
    "The Moon": {
        "upright": "Illusion, intuition, dreams",
        "reversed": "Confusion, deception, anxiety"
    },
    "The Sun": {
        "upright": "Joy, success, vitality",
        "reversed": "Delay, ego, false positivity"
    },
    "Judgement": {
        "upright": "Awakening, reflection, reckoning",
        "reversed": "Doubt, self-judgment, denial"
    },
    "The World": {
        "upright": "Completion, achievement, wholeness",
        "reversed": "Incomplete goals, delays, stagnation"
    }
}

# draw a single card
def daily_card():
    print("🔮 Daily Tarot Draw")
    card, meanings = random.choice(list(tarot_cards.items()))
    orientation = random.choice(["upright", "reversed"])
    meaning = meanings[orientation]
    print(f"\nToday's card: {card} ({orientation})")
    print(f"Message: {meaning}")
    print("🌞 Reflect on how this message applies to your day.\n")

# draw a full 3-card spread
def three_card_reading():
    print("What is your question about?")
    print("1. Love 💕")
    print("2. Career 💼")
    print("3. Health 🍀")
    print("4. Relationships 🤝")
    topic = input("Choose a number (1-4): ")
    topic_dict = {"1": "Love", "2": "Career", "3": "Health", "4": "Relationships"}
    topic_str = topic_dict.get(topic, "General")

    input(f"\nFocus on your {topic_str.lower()} question and press Enter to draw cards...")

    drawn = random.sample(list(tarot_cards.items()), 3)
    positions = ["Past", "Present", "Future"]
    upright_count = 0

    print(f"\n✨ {topic_str} Tarot Reading ✨")
    for i, (card, meanings) in enumerate(drawn):
        orientation = random.choice(["upright", "reversed"])
        meaning = meanings[orientation]
        if orientation == "upright":
            upright_count += 1
        print(f"\n{positions[i]}: {card} ({orientation})")
        print(f"Meaning: {meaning}")

    print("\nSummary:")
    if upright_count >= 2:
        print("Positive energies dominate. Things are likely working in your favor.")
    else:
        print("Challenges are ahead. Take time to reflect and adapt your mindset.")
    print("🌌 Tarot is a mirror. Trust your intuition as you interpret your reading.\n")

def main():
    print("🔮 Welcome to the Tarot Reader")
    print("1. Daily Single Card")
    print("2. 3-Card Spread (Past, Present, Future)")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        daily_card()
    elif choice == "2":
        three_card_reading()
    else:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()