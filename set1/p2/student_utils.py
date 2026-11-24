def calculate_average(grades):
    return sum(grades) / len(grades)


def determine_pass_fail(average):
    return "Passed" if average >= 75 else "Failed"


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)
