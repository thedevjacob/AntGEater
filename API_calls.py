import requests
import user_info
import json

def get_all_GE_courses() -> json:
    year, quarter, GE_category = user_info.get_all_GE_info()
    return requests.get(f"https://api.peterportal.org/rest/v0/schedule/soc?term={year}%20{quarter}&ge={GE_category}").json()
