"""
1. Your First Step! 🚀 Let's start by printing a message.
"""
print("Hello World!")  # This prints "Hello World!" to the screen 👋🌍
print("*" * 10)  # This creates a visual separator ✨


"""
2. 🎸 Welcome to the Band Name Generator! 🎸
"""
print("Where is the city you were born in? 🌍")

def has_numbers(text):
    return any(char.isdigit() for char in text)

# City input section with emoji feedback
while True:
    city = input("City: ").strip()  # 🏙️ Please enter your city name
    if not city:
        print("❌ Please enter a correct city! 🏙️")  # 🚫 Empty input error
    elif has_numbers(city):
        # Number detection
        print("❌ Numbers are not allowed! Please use letters only! 🔠")
    else:
        print("✅ City accepted!")  # 🎯 Validation passed
        break

# Pet name input section with emoji feedback
while True:
    pet = input("Pet Name: ").strip()  # 🐕🐈 Please enter your pet's name
    if not pet:
        # 🚫 Empty input error
        print("❌ Please enter an appropriate pet name! 🐶🐱")
    elif has_numbers(pet):
        # � Number detection
        print("❌ Numbers are not allowed! Please use letters only! 🔠")
    else:
        print("✅ Pet name accepted!")  # 🎯 Validation passed
        break

# Final result with celebration emojis
print(f"🎉 Your awesome band name is: {city} {pet}! 🎸✨")  # Band name revealed
print("🤘 Rock on! 🤘")  # Celebration message
