# all input functions

def get_all_course_info() -> tuple[int, str, str, str]:
    # get all info
    year = get_year()
    quarter = get_quarter()
    department = get_department()
    course_number = get_course_number()

    return year, quarter, department, course_number

def get_all_GE_info() -> tuple[int, str, str]:
    # get all info
    year = get_year()
    quarter = get_quarter()
    GE_category = get_course_GE()

    return year, quarter, GE_category

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

def get_course_GE() -> str:
    GE_categories = ['ANY', 'GE-1A', 'GE-1B', 'GE-2', 'GE-3', 'GE-4',
                     'GE-5A', 'GE-5B', 'GE-6', 'GE-7', 'GE-8']

    print("Which GE category would you like to select?")
    for category in GE_categories:
        print(f" • {category}")
    category_picked = input(" GE <<< ").upper().strip()

    if category_picked in GE_categories: return category_picked
    if ("GE-" + category_picked) in GE_categories: return "GE-" + category_picked

    print(f"Please correct only a listed category. You picked: '{category_picked}'")
    return get_course_GE()

