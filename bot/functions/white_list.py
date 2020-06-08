from tinydb import TinyDB, Query

from config import base
base = base.base()
db_path = base['db_path']
db = TinyDB(db_path)
white_list = db.table('white_list', cache_size=0)
in_white = Query()


def add_to_white(id, amis_peer_id, name):
    try:
        if (white_list.search(in_white.id == str(id)) != []):  # 有在裡面就算了
            return True
        white_list.insert(
            {
                'id': str(id),
                'amis_peer_id': str(amis_peer_id),
                'name': str(name)
            }
        )
        return True
    except Exception as e:
        raise e


def rm_from_white(id):
    try:
        if (white_list.search(in_white.id == str(id)) == []):  # 不在裡面就算了
            return True
        white_list.remove(in_white.id == str(id))
        return True
    except Exception as e:
        raise e


def list_all():
    return white_list.all()
