# student.py or in search.py if centralized
class Student:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"Student({self.id})"


# search.py
def linear_search(students, target_id):
    for student in students:
        if student.id == target_id:
            return student
    return None


# search.py
def binary_search(students, target_id):
    left = 0
    right = len(students) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_student = students[mid]

        if mid_student.id == target_id:
            return mid_student
        elif mid_student.id < target_id:
            left = mid + 1
        else:
            right = mid - 1

    return None
