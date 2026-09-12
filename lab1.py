class Student:
    def __init__(self, student_id, student_name, course, year_level):
        self.student_id = student_id
        self.student_name = student_name
        self.course = course
        self.year_level = year_level

    def __str__(self):
        return (
            f"Student ID   : {self.student_id}\n"
            f"Student Name : {self.student_name}\n"
            f"Course       : {self.course}\n"
            f"Year Level   : {self.year_level}"
        )

    def to_row(self):
        return f"{self.student_id:<12} {self.student_name:<25} {self.course:<10} {self.year_level:<5}"

class DynamicArray:
    INITIAL_CAPACITY = 5
    GROWTH_FACTOR = 2

    def __init__(self):
        self._capacity = DynamicArray.INITIAL_CAPACITY
        self._data = [None] * self._capacity
        self._count = 0

    def size(self):
        return self._count

    def get_capacity(self):
        return self._capacity

    def is_empty(self):
        return self._count == 0

    def _resize(self):
        old_capacity = self._capacity
        new_capacity = old_capacity * DynamicArray.GROWTH_FACTOR
        new_data = [None] * new_capacity

        for i in range(self._count):
            new_data[i] = self._data[i]

        self._data = new_data
        self._capacity = new_capacity
        print(f"[System] Array capacity increased from {old_capacity} to {new_capacity}.")

    def add(self, student):
        if self._count == self._capacity:
            self._resize()
        self._data[self._count] = student
        self._count += 1

    def get(self, index):
        #3
        if index < 0 or index >= self._count:
            raise IndexError(f"Index out of bounds: {index}")
        return self._data[index]

    def set(self, index, student): 
        #4 
        if index < 0 or index >= self._count:
            raise IndexError(f"Index out of bounds: {index}")
        self._data[index] = student

    def search(self, student_id):
        for i in range(self._count):
            if self._data[i].student_id.lower() == student_id.lower():
                return i
        return -1

    def remove(self, index):
        if index < 0 or index >= self._count:
            return False

        for i in range(index, self._count - 1):
            self._data[i] = self._data[i + 1]

        self._data[self._count - 1] = None 
        self._count -= 1
        return True

    def display(self):
        if self.is_empty():
            print("No student records found.")
            return

        line = "-" * 73
        print(line)
        print(f"{'Student ID':<12} {'Student Name':<25} {'Course':<10} {'Year':<5}")
        print(line)
        for i in range(self._count):
            print(self._data[i].to_row())
        print(line)

students = DynamicArray()

def print_menu():
    print("================================")
    print("     STUDENT RECORD MANAGER")
    print("================================")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Display Array Information")
    print("7. Exit")


def read_int(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid whole number.")


def read_non_empty_line(prompt):
    while True:
        line = input(prompt).strip()
        if line:
            return line
        print("Input cannot be empty. Please try again.")


def add_student():
    print("--- Add Student ---")

    student_id = read_non_empty_line("Student ID: ")
    if students.search(student_id) != -1:
        print("A student with that ID already exists. Add cancelled.")
        return

    name = read_non_empty_line("Student Name: ")
    course = read_non_empty_line("Course: ")
    year = read_int("Year Level: ")

    students.add(Student(student_id, name, course, year))
    print("Student added successfully.")


def display_students():
    print("--- Student List ---")
    students.display()


def search_student():
    print("--- Search Student ---")
    student_id = read_non_empty_line("Enter Student ID to search: ")
    index = students.search(student_id)

    if index == -1:
        print(f'Student with ID "{student_id}" was not found.')
    else:
        print("Student found:")
        print(students.get(index))


def update_student():
    print("--- Update Student ---")
    student_id = read_non_empty_line("Enter Student ID to update: ")
    index = students.search(student_id)

    if index == -1:
        print(f'Student with ID "{student_id}" was not found.')
        return

    existing = students.get(index)
    print("Current record:")
    print(existing)
    print("Enter new values (leave blank to keep current value).")

    name = input(f"New Name [{existing.student_name}]: ").strip()
    if name:
        existing.student_name = name

    course = input(f"New Course [{existing.course}]: ").strip()
    if course:
        existing.course = course

    year_input = input(f"New Year Level [{existing.year_level}] (or press Enter to keep): ").strip()
    if year_input:
        try:
            existing.year_level = int(year_input)
        except ValueError:
            print("Invalid number entered. Year Level unchanged.")

    students.set(index, existing)
    print("Student record updated successfully.")


def remove_student():
    print("--- Remove Student ---")
    student_id = read_non_empty_line("Enter Student ID to remove: ")
    index = students.search(student_id)

    if index == -1:
        print(f'Student with ID "{student_id}" was not found.')
        return

    removed = students.get(index)
    students.remove(index)
    print(f"Removed student: {removed.student_name} ({removed.student_id})")


def display_array_info():
    print("--- Array Information ---")
    print(f"Number of students (size) : {students.size()}")
    print(f"Current array capacity     : {students.get_capacity()}")


def main():
    choice = None
    while choice != 7:
        print_menu()
        choice = read_int("Enter your choice: ")

        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            remove_student()
        elif choice == 6:
            display_array_info()
        elif choice == 7:
            print("Exiting program. Goodbye!")
        else:
            print("Invalid choice. Please try again.")

        print()


if __name__ == "__main__":
    main()
