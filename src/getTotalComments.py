from src.getbestsubreddit import *

bs = BestSub()
r = bs.red_inst()
conn = bs.get_conn()
cursor = bs.get_cursor()

command = (
    """
        SELECT post_id FROM POST;
    """
)
cursor.execute(command)
for i in range(0, cursor.rowcount):
    cursor.execute(command)
    post_id = (cursor.fetchall()[i][0])
    print(post_id)
    post = r.submission(post_id)
    post.comments.replace_more(limit=0)
    top_level_comm_count = 0
    for comm in post.comments.list():
        top_level_comm_count += 1
    total_com_command = (
        """
            UPDATE post SET total_toplevel_comments = %s WHERE post_id = %s;
        """
    )
    to_update = (top_level_comm_count, post_id)
    cursor.execute(total_com_command, to_update)
    conn.commit()

cursor.close()
conn.close()
