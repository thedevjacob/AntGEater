import requests, json
import user_info

year, quarter, department, course_number = user_info.get_all_course_info()
print(f"https://api.peterportal.org/rest/v0/schedule/soc?term={year}%20{quarter}&department={department}&courseNumber={course_number}")
all_courses = requests.get(f"https://api.peterportal.org/rest/v0/schedule/soc?term={year}%20{quarter}&department={department}&courseNumber={course_number}").json()

# # course_code = int(input("Course code <<< "))
# course_code = all_courses
# all_courses = requests.get(f"https://api.peterportal.org/rest/v0/grades/calculated?code={course_code}").json()
# average_gpa = all_courses['gradeDistribution']['average_gpa']

file = open("stuff.json", 'w')
json.dump(all_courses, file, indent = 4) # type: ignore

relevant_coursed = []
for course in all_courses["courseList"]:
    print(course["year"])


# print(round(average_gpa, 2))
