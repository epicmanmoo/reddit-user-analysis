from src.getbestsubreddit import *

# just testing functionality
bs = BestSub()
r = bs.red_inst()
is_inserted = bs.get_best()
while not is_inserted:
    bs.get_best()
bs.get_conn().close()
bs.get_cursor().close()
