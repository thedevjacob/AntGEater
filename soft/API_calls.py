import requests
import soft.user_info
import json

def auto_get_all_GE_courses() -> json:
    year, quarter, GE_category = soft.user_info.auto_all_GE_info()
    request = requests.get(f"https://api.peterportal.org/rest/v0/schedule/soc?term={year}%20{quarter}&ge={GE_category}").json()
    return request

def get_all_GE_courses_web(GE_category) -> json:
    year, quarter = soft.user_info.auto_get_next_quarter()
    request = requests.get(f"https://api.peterportal.org/rest/v0/schedule/soc?term={year}%20{quarter}&ge={GE_category}").json()
    return request


def get_average_gpa(section_code: int) -> float:
    retrieved_courses = requests.get(f"https://api.peterportal.org/rest/v0/grades/calculated?code={section_code}").json()
    return retrieved_courses['gradeDistribution']['average_gpa']