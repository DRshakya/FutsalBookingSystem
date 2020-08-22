from repo.blog_repo import BlogRepo
from repo.user_repo import UserRepo
from services.service import Service
from utils import generate_uuid, timestamp, password_hash, password_verify
import traceback


class BlogService(Service):
    def get_all_blogs(self):
        try:
            blog_repo = BlogRepo()
            return blog_repo.fetch_blogs()
        except Exception as e:
            traceback.print_exc()
            return None

    def delete(self, blog_id):
        try:
            blog_repo = BlogRepo()
            return blog_repo.delete(blog_id)
        except Exception as e:
            traceback.print_exc()
            return False


    def save(self, blog):
        blog.blog_id = generate_uuid()
        blog.created_at = timestamp()
        try:
            blog_repo = BlogRepo()
            if blog_repo.save(blog):
                return blog
        except Exception as e:
            traceback.print_exc()
            return None
