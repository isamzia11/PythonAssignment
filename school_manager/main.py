
import logging

from school.manager import (
    add_student,
    add_marks,
    find_student,
    report_card,
    class_ranking
)
from school.grades import average
from school.storage import save_students, load_students


DATA_FILE = "school.json"


def main() -> None:
    logging.basicConfig(
        filename="school_manager.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    try:
        students = load_students(DATA_FILE)
    except ValueError as error:
        print(f"Could not load records: {error}")
        logging.error("Failed to load records: %s", error)
        return

    while True:
        print("\n===== SCHOOL MANAGER =====")
        print("1. Add student")
        print("2. Add marks")
        print("3. Show report card")
        print("4. Class ranking")
        print("5. Save and exit")

        choice = input("Choose: ")

        try:
            if choice == "1":
                name = input("Student name: ").strip()
                roll = int(input("Roll number: "))

                add_student(students, name, roll)

                print("Student added successfully!")
                logging.info("Student added: roll %s", roll)

            elif choice == "2":
                roll = int(input("Roll number: "))
                student = find_student(students, roll)

                if student is None:
                    print("Student not found.")
                    continue

                mark = float(input("Enter mark (0-100): "))
                add_marks(student, mark)

                print("Marks added successfully!")
                logging.info("Mark added for roll %s", roll)

            elif choice == "3":
                roll = int(input("Roll number: "))
                student = find_student(students, roll)

                if student is None:
                    print("Student not found.")
                else:
                    print(report_card(student))

            elif choice == "4":
                ranked = class_ranking(students)

                if not ranked:
                    print("No students available.")
                    continue

                print("\n===== CLASS RANKING =====")

                for rank, student in enumerate(ranked, start=1):
                    avg = average(student.marks)

                    print(
                        f"{rank}. {student.name} "
                        f"(Roll {student.roll_number}) "
                        f"- Average: {avg:.2f}"
                    )

            elif choice == "5":
                try:
                    save_students(students, DATA_FILE)
                except OSError as error:
                    print(f"Save failed: {error}")
                    logging.error("Save failed: %s", error)
                    continue

                print("Data saved successfully. Goodbye!")
                logging.info("School data saved")
                break

            else:
                print("Invalid choice. Please select 1-5.")

        except ValueError as error:
            print(f"Invalid input: {error}")
            logging.warning("Invalid input: %s", error)

        except (EOFError, KeyboardInterrupt):
            print("\nInput interrupted. Use Save and exit.")
            logging.warning("User input interrupted")
            break


if __name__ == "__main__":
    main()
