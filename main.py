import requests, json
import user_info

# all_courses = requests.get(f"https://api.peterportal.org/rest/v0/schedule/soc?term={year}%20{quarter}&department={department}&courseNumber={course_number}").json()

year, quarter, GE_category = user_info.get_all_GE_info()
all_courses = requests.get(f"https://api.peterportal.org/rest/v0/schedule/soc?term={year}%20{quarter}&ge={GE_category}").json()

# all_courses = requests.get(f"https://api.peterportal.org/rest/v0/grades/calculated?code={course_code}").json()
# average_gpa = all_courses['gradeDistribution']['average_gpa']

# file = open("courses.json", 'w')
# json.dump(all_courses, file, indent = 4) # type: ignore

# relevant_coursed = []
# for course in all_courses["courseList"]:
#     print(course["year"])

# print(round(average_gpa, 2))
