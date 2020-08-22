import traceback

from django.db import connection
from django.http import HttpResponse, request


class BookRepo(object):
    def check_book(self, uid, date, starttime, endtime, ground):
        query1 = "SELECT * FROM book WHERE b_date = %s AND b_start= %s AND b_end = %s AND b_ground = %s"
        #query1 = "INSERT INTO book( user_id, b_date, b_start, b_end, b_ground) VALUES(%s,%s,%s,%s,%s)"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query1, [date, starttime, endtime, ground])
                row = cursor.fetchone()
                if row is None:
                    query = "INSERT INTO book( user_id, b_date, b_start, b_end, b_ground) VALUES(%s,%s,%s,%s,%s)"
                    try:
                        with connection.cursor() as cursor:
                            cursor.execute(query, [uid, date, starttime, endtime, ground])
                            print("There is success in booking the asdbjhad")
                            return True
                    except Exception as e:
                        traceback.print_exc()
                    return True
                else:
                    return False

        except Exception as e:
            traceback.print_exc()
            return False


