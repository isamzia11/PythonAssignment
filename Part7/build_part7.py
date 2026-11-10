# Name Isam Zia Roll no: TRN-2026-00346 


from datetime import date


def daily_diary():
    while True:
        print("\n===== DAILY DIARY =====")
        print("1. Add today's note")
        print("2. View all notes")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            note = input("Write your note: ")
            today = date.today()

            with open("diary.txt", "a", encoding="utf-8") as file:
                file.write(f"{today}: {note}\n")

            print("Note saved successfully!")

        elif choice == "2":
            try:
                with open("diary.txt", "r", encoding="utf-8") as file:
                    entries = file.read()

                if entries:
                    print("\n===== PAST ENTRIES =====")
                    print(entries)
                else:
                    print("No entries yet")

            except FileNotFoundError:
                print("No entries yet")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Enter 1, 2 or 3.")


daily_diary()
