import CourseList
import API_calls

def run():

    retrieved_courses = API_calls.get_all_GE_courses()
    course_list = CourseList.CourseList(retrieved_courses)

    for course in course_list.courses:
        print(course.title)

    # retrieved_courses = requests.get(f"https://api.peterportal.org/rest/v0/grades/calculated?code={course_code}").json()
    # average_gpa = retrieved_courses['gradeDistribution']['average_gpa']

    # file = open("courses.json", 'w')
    # json.dump(retrieved_courses, file, indent = 4) # type: ignore

    # relevant_coursed = []
    # for course in retrieved_courses["courseList"]:
    #     print(course["year"])

    # print(round(average_gpa, 2))

if __name__ == "__main__":
    run()
