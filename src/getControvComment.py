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

post.comment_sort = 'controversial'
for comment in post.comments:
    if comment.controversiality == 1:
        if comment.body != "[removed]":
            print(comment.body, '\n', comment.score)
            break

conn.close()
cursor.close()
