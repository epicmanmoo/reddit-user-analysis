from src.getbestsubreddit import *

bs = BestSub()
r = bs.red_inst()
conn = bs.get_conn()
cursor = bs.get_cursor()
command = (
    """
        SELECT post_id from post;
    """
)
cursor.execute(command)
post_id = cursor.fetchone()[0]
post = r.submission(id=post_id)
comment_id = ""
comment_author_id = ""
comment_body = ""
subreddit_name = ""

# insert into reddit_user and user_comment.

post.comments.replace_more(limit=None)
for comment in post.comments.list():
    if comment.controversiality == 1:
        break
