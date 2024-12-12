from soft import API_calls, CourseList


def run():

    retrieved_courses = API_calls.auto_get_all_GE_courses()
    print(retrieved_courses)
    course_list = CourseList.CourseList(retrieved_courses)

    all_lectures = course_list.get_lectures()

    print(">>> one moment please... RETRIEVING GPAS <<<\n")

    open_lectures = [lecture for lecture in all_lectures if ((not lecture.full()) and lecture.get_gpa())]
    open_lectures.sort(key=lambda item: item.get_gpa(), reverse = True)

    if not open_lectures:
        print("-> ALL LECTURES ARE FULL FOR THIS GE :( <-")

    for lecture in open_lectures:
        lecture_info = f"{lecture.course.title} - AVERAGE GPA of {str(round(lecture.get_gpa(), 2))} - (COURSE CODE: {lecture.code}, COURSE #: {lecture.course.number})"
        print(lecture_info)

if __name__ == "__main__":
    run()
