from src.getbestsubreddit import *

bs = BestSub()
r = bs.red_inst()
# is_inserted = bs.get_best()
# while not is_inserted:
#     bs.get_best()
command = (
    """
        SELECT sub_name FROM popular_subreddits ORDER BY curr_time DESC LIMIT 1;
    """
)
conn = bs.get_conn()
cursor = bs.get_cursor()
cursor.execute(command)
sub = cursor.fetchone()[0]
post = r.subreddit(str(sub)).top("day")
top_post = list(post)[0]
post_id = top_post.id
post_title = top_post.title
post_is_text = top_post.is_self
post_author_id = top_post.author.id
post_subreddit_id = top_post.subreddit.id
post_author_username = str(top_post.author)
post_author_c_karma = top_post.author.comment_karma
post_author_p_karma = top_post.author.link_karma
# command = (
#     """
#         INSERT INTO reddit_user VALUES(%s, %s, %s, %s);
#     """
# )
# to_insert = (post_author_id, post_author_username, post_author_c_karma, post_author_p_karma)

# side note for future reference: if comment_id ends up being null then ignore it. all it
# means is that the tuple contains info about the poster on the ORIGINAL subreddit that
# we are looking at, is is not that useful.

# cursor.execute(command, to_insert)

# command = (
#     """
#         INSERT INTO post VALUES(%s, %s, %s, %s, %s);
#     """
# )
# to_insert = (post_id, post_title, post_is_text, post_subreddit_id, post_author_id)
# cursor.execute(command, to_insert)
# conn.commit()

conn.close()
cursor.close()

