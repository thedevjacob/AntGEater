# all input functions
import datetime


GE_CATEGORIES = ['GE-1A', 'GE-1B', 'GE-2', 'GE-3', 'GE-4',
                 'GE-5A', 'GE-5B', 'GE-6', 'GE-7', 'GE-8']

QUARTERS = {
    'Fall': (9, 10, 11, 12),  # Sept - Nov
    'Winter': (1, 2, 3),  # Dec - Feb
    'Spring': (4, 5),  # Mar - May
    'Summer1': (6, 7),  # June - July
    'Summer2': (8,),  # August
    'Summer10wk': (6, 7, 8),  # All summer months
}

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

def auto_all_GE_info() -> tuple[int, str, str]:
    # get all info
    year, quarter = auto_get_next_quarter()
    GE_category = get_course_GE()

    # Format the message and center it
    print(f"""
{'-' * 60} 
{('Selected ' + quarter + ' quarter of ' + str(year) + '.').center(60)}
{f">>> CATEGORY = '{GE_category}' <<<".center(60)}
{'-' * 60}
""")

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

def auto_get_next_quarter():
    current_date = datetime.date.today()

    current_month = current_date.month
    current_year = current_date.year

    # Find the next quarter
    if current_month in QUARTERS['Fall']:
        next_quarter = 'Winter'
        next_year = current_year + 1
    elif current_month in QUARTERS['Winter']:
        next_quarter = 'Spring'
        next_year = current_year
    elif current_month in QUARTERS['Spring']:
        next_quarter = 'Summer1'
        next_year = current_year
    elif current_month in QUARTERS['Summer1']:
        next_quarter = 'Summer2'
        next_year = current_year
    elif current_month in QUARTERS['Summer2']:
        next_quarter = 'Fall'
        next_year = current_year
    else:
        next_quarter = 'Winter'
        next_year = current_year + 1

    return next_year, next_quarter

def get_department() -> str:
    return input("Course Department <<< ")

def get_course_number() -> str:
    return input("Course Number <<< ")

def get_course_GE() -> str:
    # removed 'ANY' category
    print("Which GE category would you like to select?")
    for category in GE_CATEGORIES:
        print(f" • {category}")
    category_picked = input(" GE <<< ").upper().strip()

    if category_picked in GE_CATEGORIES: return category_picked
    if ("GE-" + category_picked) in GE_CATEGORIES: return "GE-" + category_picked

    print(f"Please correct only a listed category. You picked: '{category_picked}'")
    return get_course_GE()

