# Personal Diary App

def write_entry():
    entry = input("Write your diary entry:\n")
    with open("diary.txt", "a") as file:
        file.write(entry + "\n")
    print("📝 Entry saved successfully!")

def read_entries():
    print("\n📚 Your diary entries:")
    try:
        with open("diary.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No entries yet. Start writing!")

# App Menu
while True:
    print("\nChoose an option:")
    print("1. Write a new entry")
    print("2. Read your diary")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        write_entry()
    elif choice == "2":
        read_entries()
    elif choice == "3":
        print(" bye!")
        break
    else:
        print("Invalid choice. Try again.")
