def get_all_course_info() -> tuple[int, str, str, str]:
    # get all info
    year = get_year()
    quarter = get_quarter()
    department = get_department()
    course_number = get_course_number()

    return year, quarter, department, course_number

def get_year() -> int:
    return int(input("Year <<< "))

def get_quarter() -> str:
    print("""Quarter?
        1 - Fall
        2 - Winter
        3 - Spring""")
    quarter = int(input("QUARTER <<< "))
    quarter = "Fall" if quarter == 1 else quarter
    quarter = "Winter" if quarter == 2 else "Spring"

    return quarter

def get_department() -> str:
    return input("Course Department <<< ")

def get_course_number() -> str:
    return input("Course Number <<< ")
