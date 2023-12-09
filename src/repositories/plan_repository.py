from database_connection import connection

class PlanRepository:
    def return_plan(self, username):
        db = connection

        return db[username]

    def find_user(self, username):
        if username in connection.keys():
            return True

        return False

    def create_user(self, username):
        db = connection

        db[username] = {}

        db.commit()

        return username

    def save_full_plan(self, username, plan_dict):
        db = connection

        db[username] = plan_dict

        db.commit()

    def add_course(self, username, course):
        db = connection

        users_plan = db[username]

        list_courses = users_plan["courses"]

        list_courses.append(course.to_json())

        users_plan["courses"] = list_courses
        db[username] = users_plan

        db.commit()

    def delete_course(self, username, code):
        db = connection

        users_plan = db[username]

        old_courses = users_plan["courses"]
        new_courses = []

        for old_course in old_courses:
            if not old_course["code"] == code:
                new_courses.append(old_course)

        users_plan["courses"] = new_courses
        db[username] = users_plan

        db.commit()

    def add_meb_exam(self, username, exam_code, exam_period):
        db = connection

        users_plan = db[username]
        meb_plan = users_plan["meb_plan"]

        modified_period = meb_plan[exam_period]
        modified_period.append(exam_code)
        meb_plan[exam_period] = modified_period

        users_plan["meb_plan"] = meb_plan
        db[username] = users_plan

        db.commit()

    def delete_meb_exam(self, username, exam_code, exam_period):
        db = connection

        users_plan = db[username]
        meb_plan = users_plan["meb_plan"]

        modified_period = meb_plan[exam_period]
        modified_period.remove(exam_code)
        meb_plan[exam_period] = modified_period

        users_plan["meb_plan"] = meb_plan
        db[username] = users_plan

        db.commit()

    def change_special_task(self, username, new_status):
        db = connection

        users_plan = db[username]
        users_plan["special_task"] = new_status

        db[username] = users_plan

        db.commit()
