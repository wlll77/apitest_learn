import pytest

from utils.mysql_util import db


@pytest.fixture()
def banner_num():
    sql = "SELECT count(1) as banner_num FROM goods_banner"
    result = db.select_db_one(sql)
    return result['banner_num']
