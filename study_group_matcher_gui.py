"""A Tkinter graphical interface for matching study groups."""

import tkinter as tk
from dataclasses import dataclass
from tkinter import messagebox, ttk


@dataclass
class Student:
    """A student profile used by the matcher."""

    name: str
    department: str
    course: str
    availability: set[str]


def find_groups(students: list[Student]) -> list[list[Student]]:
    """Match students with the same class and at least one common meeting time."""
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


class StudyGroupMatcherApp:
    """Window and event handlers for the Study Group Matcher."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Study Group Matcher")
        self.root.geometry("760x610")
        self.root.minsize(650, 500)
        self.students: list[Student] = []

        self.name_var = tk.StringVar()
        self.department_var = tk.StringVar()
        self.course_var = tk.StringVar()
        self.availability_var = tk.StringVar()
        self._create_widgets()

    def _create_widgets(self) -> None:
        """Build the app's visible controls."""
        main_frame = ttk.Frame(self.root, padding=18)
        main_frame.pack(fill="both", expand=True)

        ttk.Label(
            main_frame,
            text="Study Group Matcher",
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w")
        ttk.Label(
            main_frame,
            text="Add student profiles, then find classmates with a shared meeting time.",
        ).pack(anchor="w", pady=(0, 14))

        form = ttk.LabelFrame(main_frame, text="Add Student", padding=12)
        form.pack(fill="x")

        fields = [
            ("Name", self.name_var),
            ("Department", self.department_var),
            ("Course", self.course_var),
            ("Available times (separate with commas)", self.availability_var),
        ]
        for row, (label, variable) in enumerate(fields):
            ttk.Label(form, text=f"{label}:").grid(row=row, column=0, sticky="w", padx=(0, 8), pady=4)
            ttk.Entry(form, textvariable=variable, width=52).grid(row=row, column=1, sticky="ew", pady=4)

        form.columnconfigure(1, weight=1)
        ttk.Button(form, text="Add Student", command=self.add_student).grid(
            row=len(fields), column=1, sticky="e", pady=(8, 0)
        )

        list_frame = ttk.LabelFrame(main_frame, text="Student Profiles", padding=8)
        list_frame.pack(fill="both", expand=True, pady=14)
        self.student_list = tk.Listbox(list_frame, height=8)
        self.student_list.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.student_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.student_list.configure(yscrollcommand=scrollbar.set)

        actions = ttk.Frame(main_frame)
        actions.pack(fill="x")
        ttk.Button(actions, text="Remove Selected", command=self.remove_selected).pack(side="left")
        ttk.Button(actions, text="Clear All", command=self.clear_all).pack(side="left", padx=8)
        ttk.Button(actions, text="Find Study Groups", command=self.show_matches).pack(side="right")

        results_frame = ttk.LabelFrame(main_frame, text="Matches", padding=8)
        results_frame.pack(fill="both", expand=True, pady=(14, 0))
        self.results = tk.Text(results_frame, height=9, wrap="word", state="disabled")
        self.results.pack(fill="both", expand=True)

    def add_student(self) -> None:
        """Validate the form, save the profile, and update the list."""
        name = self.name_var.get().strip()
        department = self.department_var.get().strip().upper()
        course = self.course_var.get().strip().upper()
        availability = {
            time.strip().casefold()
            for time in self.availability_var.get().split(",")
            if time.strip()
        }

        if not all((name, department, course, availability)):
            messagebox.showwarning(
                "Missing information",
                "Enter a name, department, course, and at least one available time.",
            )
            return

        student = Student(name, department, course, availability)
        self.students.append(student)
        times = ", ".join(sorted(availability))
        self.student_list.insert("end", f"{name} — {department} {course} — {times}")

        self.name_var.set("")
        self.department_var.set("")
        self.course_var.set("")
        self.availability_var.set("")

    def remove_selected(self) -> None:
        """Remove the selected profile from the application."""
        selection = self.student_list.curselection()
        if not selection:
            messagebox.showinfo("Select a student", "Select a student profile to remove.")
            return

        index = selection[0]
        del self.students[index]
        self.student_list.delete(index)
        self._set_results("")

    def clear_all(self) -> None:
        """Remove every profile and every displayed result."""
        self.students.clear()
        self.student_list.delete(0, "end")
        self._set_results("")

    def show_matches(self) -> None:
        """Calculate and display the current study-group matches."""
        if not self.students:
            messagebox.showinfo("No profiles", "Add at least one student profile first.")
            return

        lines = []
        group_number = 1
        for group in find_groups(self.students):
            first_student = group[0]
            if len(group) == 1:
                lines.append(
                    f"No match yet: {first_student.name} "
                    f"({first_student.department} {first_student.course})"
                )
                continue

            shared_times = set.intersection(*(student.availability for student in group))
            names = ", ".join(student.name for student in group)
            times = ", ".join(sorted(shared_times))
            lines.append(
                f"Group {group_number}: {first_student.department} {first_student.course}\n"
                f"Members: {names}\nShared availability: {times}"
            )
            group_number += 1

        self._set_results("\n\n".join(lines))

    def _set_results(self, text: str) -> None:
        """Replace the read-only contents of the matches panel."""
        self.results.configure(state="normal")
        self.results.delete("1.0", "end")
        self.results.insert("1.0", text)
        self.results.configure(state="disabled")


def main() -> None:
    """Start the Tkinter event loop."""
    root = tk.Tk()
    StudyGroupMatcherApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
