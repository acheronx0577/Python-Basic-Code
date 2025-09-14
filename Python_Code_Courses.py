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



"""
3 📊 Student Grading System with Average Calculation
"""
score = []  # Empty list to store all student scores

# 👥 Grade 4 students
for student in range(1, 5):
    student_score = input(f"\nEnter score for student {student}: ").strip()
    
    if student_score.isdigit():
        score_num = int(student_score)
        score.append(score_num)  # 💾 Add score to list
        
        # 🎯 Grade feedback with emojis
        if score_num >= 90:
            print(f"Good job Student {student}! 🎉")  # 🌟 Excellent
        elif score_num >= 80:
            print(f"Hmm need to work on your practice problems more student {student}! 📚")  # 📖 Needs practice
        elif score_num >= 50:
            print(f"Im sorry but you are failed this class and you are dropped out student {student}! ❌")  # 🚫 Failed
        else:
            print(f"You cant be fr student {student} 😅")  # 😅 Very poor
            
    else:
        print(f"❌ Please enter a valid number for student {student}!\n")  # ⚠️ Invalid input

# 📈 Calculate and display class average
print(f"\n📊 Average student score: {sum(score)/len(score):.1f}/100")  # 🧮 Math magic!

# 🎊 Final message
print("Nice job everyone! ✅\n")  # 👏 Celebration

