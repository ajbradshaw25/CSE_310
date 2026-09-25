"""A command-line study group matcher.

Run this file with Python and follow the prompts to enter student profiles.
Students are grouped by department and course when they share at least one
available meeting time.
"""

from dataclasses import dataclass


@dataclass
class Student:
    """Information used to place a student in a study group."""

    name: str
    department: str
    course: str
    availability: set[str]


def get_nonempty_input(prompt: str) -> str:
    """Prompt until the user provides text, returning it without extra spaces."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def get_student(number: int) -> Student:
    """Collect one student's profile from the terminal."""
    print(f"\nStudent {number}")
    name = get_nonempty_input("Name: ")
    department = get_nonempty_input("Department (for example, CSE): ").upper()
    course = get_nonempty_input("Course number (for example, 310): ").upper()

    print("Enter available times separated by commas (for example, Mon 3 PM, Wed 3 PM).")
    times = get_nonempty_input("Available times: ")
    availability = {time.strip().casefold() for time in times.split(",") if time.strip()}

    return Student(name, department, course, availability)


def find_groups(students: list[Student]) -> list[list[Student]]:
    """Return compatible groups using department, course, and shared time."""
    groups: list[list[Student]] = []
    remaining = students.copy()

    while remaining:
        seed = remaining.pop(0)
        group = [seed]
        shared_times = seed.availability.copy()

        for candidate in remaining[:]:
            same_class = (
                candidate.department == seed.department
                and candidate.course == seed.course
            )
            common_times = shared_times & candidate.availability

            if same_class and common_times:
                group.append(candidate)
                shared_times = common_times
                remaining.remove(candidate)

        groups.append(group)

    return groups


def display_groups(groups: list[list[Student]]) -> None:
    """Print the matched groups in a readable terminal format."""
    print("\n--- Study Group Matches ---")

    for number, group in enumerate(groups, start=1):
        first_student = group[0]
        names = ", ".join(student.name for student in group)

        if len(group) == 1:
            print(f"\nNo match yet: {names} ({first_student.department} {first_student.course})")
            continue

        shared_times = set.intersection(*(student.availability for student in group))
        meeting_times = ", ".join(sorted(shared_times))
        print(f"\nGroup {number}: {first_student.department} {first_student.course}")
        print(f"Members: {names}")
        print(f"Shared availability: {meeting_times}")


def main() -> None:
    """Run the interactive program."""
    print("Welcome to the Study Group Matcher")
    print("Create profiles to find classmates with a shared meeting time.")

    while True:
        try:
            student_count = int(input("\nHow many students would you like to enter? "))
            if student_count > 0:
                break
            print("Enter a whole number greater than zero.")
        except ValueError:
            print("Enter a whole number greater than zero.")

    students = [get_student(number) for number in range(1, student_count + 1)]
    display_groups(find_groups(students))


if __name__ == "__main__":
    main()
