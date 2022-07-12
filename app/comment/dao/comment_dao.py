from comment import Comment
import json


COMMENT_PATH = '../../data/comments.json'

class CommentDAO:
    def __init__(self,path):
         self.path = COMMENT_PATH

    def load_data(self):
        with open(self.path, "r", encoding="utf-8") as f:
            comments_data = json.load(f)
            comments = []
            for comment in comments_data:
                comments.append(Comment(
                    comment["post_id"],
                    comment["commenter_name"],
                    comment["comment"],
                    comment["pk"],
                ))
        return comments

    def get_comments_by_post_id(self, post_id):
        posts = self.load_data()
        comments_post = []
        for post in posts:
            if post.post_id == post_id:
                comments_post.append(post)
        return comments_post


l = CommentDAO(COMMENT_PATH)
print(l.get_comments_by_post_id(4))