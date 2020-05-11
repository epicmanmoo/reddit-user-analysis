from src.getbestsubreddit import *

valid_post_ids_list = []
valid_comment_ids_list = []
bs = BestSub()
r = bs.red_inst()
conn = bs.get_conn()
cursor = bs.get_cursor()


def check_exists(submission_id):
    check_command = (
        """
            SELECT post_id FROM post;
        """
    )
    cursor.execute(check_command)
    post_id = cursor.fetchone()
    for sub_id in post_id:
        if sub_id == submission_id:
            return False
    return True


command = (
    """
        SELECT username FROM reddit_user WHERE is_chosen = true;
    """
)
cursor.execute(command)
username = cursor.fetchone()[0]
user = r.redditor(username)
for comment in user.comments.hot(limit=50):
    if comment.submission.id not in valid_post_ids_list and check_exists(
            comment.submission.id) and comment.num_comments > 100:
        valid_post_ids_list.append(comment.submission.id)
        valid_comment_ids_list.append(comment.id)

if len(valid_post_ids_list) == 0 or len(valid_post_ids_list) < 5:
    print("RE-PICK USER")
else:
    if len(valid_post_ids_list) > 5:
        del valid_post_ids_list[5:]
        del valid_comment_ids_list[5:]
    # command = (
    #     """
    #         INSERT INTO reddit_user VALUES(%s, %s, %s, %s, false);
    #     """
    # )
    # command = (
    #     """
    #         INSERT INTO post VALUES(%s, %s, %s, %s, %s);
    #     """
    # )
    # command = (
    #     """
    #         INSERT INTO subreddit VALUES(%s, %s, %s);
    #     """
    # )
    # command = (
    #     """
    #         INSERT INTO user_comment VALUES(%s, %s, %s, %s, %s);
    #     """
    # )
    # command = (
    #     """
    #         INSERT INTO user_top_comments VALUES(%s, %s, %s, %s);
    #     """
    # )
    which_post = 0
    for id_of_comm in valid_comment_ids_list:
        comm_id = r.comment(id_of_comm)
        post_id = r.submission(valid_post_ids_list[which_post])

        # to_insert = (id_of_comm, post_id.id, str(list(r.info(['t5_' + post_id.subreddit.id]))[0]), comm_id.body, comm_id.author.id)

        # to_insert = (id_of_comm, post_id.subreddit.id, comm_id.author.id, post_id.id)

        # cursor.execute(command, to_insert)
        # conn.commit()
        which_post += 1
    for id_of_post in valid_post_ids_list:
        post_id = r.submission(id_of_post)
        # to_insert = (post_id.author.id, str(post_id.author), post_id.author.comment_karma, post_id.author.link_karma)

        # to_insert = (id_of_post, post_id.title, post_id.is_self, post_id.subreddit.id, post_id.author.id)

        # try:
        #     to_insert = (post_id.subreddit.id, str(list(r.info(['t5_' + post_id.subreddit.id]))[0]), post_id.author.id)
        #     cursor.execute(command, to_insert)
        #     conn.commit()
        #     conn.rollback()
        # except Exception:
        #     continue

cursor.close()
conn.close()
