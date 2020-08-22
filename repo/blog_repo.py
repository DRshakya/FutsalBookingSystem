from django.db import connection
import traceback

from models.blog import Blog
from models.user import User
from utils import print_timestamp


class BlogRepo(object):

    def fetch_blogs(self):
        query = "SELECT b.blog_id, b.title, b.tag, b.body, b.created_at, u.user_id, u.full_name, b.blog_image_url FROM blog as b INNER JOIN user as u ON b.user_id = u.user_id ORDER BY b.created_at DESC"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows is None:
                    return None
                else:
                    blogs = list()
                    for row in rows:
                        blog = Blog()
                        blog.blog_id = row[0]
                        blog.title = row[1]
                        blog.tag = row[2]
                        blog.body = row[3]
                        blog.created_at = row[4]
                        blog.created_date = print_timestamp(row[4])
                        user = User()
                        user.user_id = row[5]
                        user.full_name = row[6]
                        blog.user = user
                        blog.blog_image = row[7]

                        blogs.append(blog)
                    return blogs
        except Exception as e:
            traceback.print_exc()
            return None

    def delete(self, blog_id):
        query = "DELETE FROM blog WHERE blog_id = %s"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [blog_id])
                return True
        except Exception as e:
            traceback.print_exc()
            return False

    def save(self, blog):
        query = "INSERT INTO blog(blog_id, title, tag, body, user_id, created_at, blog_image_url) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [blog.blog_id, blog.title, blog.tag, blog.body, blog.user.user_id, blog.created_at, blog.blog_image])
                return True
        except Exception as e:
            traceback.print_exc()
            return False