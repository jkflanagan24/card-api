from utils.database import *
from baseball.sources.baseball_reference.players import *
from tasks import add

if __name__ == '__main__':
    # make_test_table()
    # get_all_players()
    r = add.delay(4,4)
    print(r)