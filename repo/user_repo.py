from django.db import connection
import traceback

from models.user import User


class UserRepo(object):

    def signin(self, email):
        query = "SELECT user_id, full_name, email, password FROM user WHERE email = %s"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [email])
                row = cursor.fetchone()
                if row is None:
                    return None
                else:
                    user = User()
                    user.user_id = row[0]
                    user.full_name = row[1]
                    user.email = row[2]
                    return {"user":user, "password":row[3]}
        except Exception as e:
            traceback.print_exc()
            return None

    def save(self, user, password):
        query = "INSERT INTO user(user_id, full_name, email, password, phone, address, created_at) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [user.user_id, user.full_name, user.email, password,user.phone, user.address, user.created_at])
                return True
        except Exception as e:
            traceback.print_exc()
            return False