import json
from flask import Blueprint
from sql_study.sql_operator import operator_mysql
import functools

bp = Blueprint('api1', __name__,url_prefix='/api')
op = operator_mysql()


def json_resp(func):
    @functools.wraps(func)
    def __func(*args, **kwargs):
        resp = func(*args, **kwargs)
        if isinstance(resp, dict):
            if 'success' not in resp:
                resp = dict(success=True, data=resp)
        elif isinstance(resp, (int, float, str, list)):
            return dict(success=True, data=resp)
        else:
            raise TypeError('response should be instance of dict.')
        return json.dumps(resp)
    return __func


@bp.route('/sql')
@json_resp
def allUserInfo():
    res = op.select_sql("select * from user")
    return res


if __name__ == '__main__':
    print(allUserInfo())
