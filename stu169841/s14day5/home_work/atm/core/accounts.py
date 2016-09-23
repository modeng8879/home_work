#!_*_coding:utf-8_*_

# import json
# import time
# from s14day4.home_work.atm.core import db_handler
# from s14day4.home_work.atm.conf import settings
#
#
# def load_current_balance(account_id):
#     '''
#     return account balance and other basic info
#     :param account_id:
#     :return:
#     '''
#     db_path = db_handler.db_handler(settings.DATABASE)
#     account_file = "%s/%s.json" %(db_path,account_id)
#     with open(account_file) as f:
#         acc_data = json.load(f)
#         return  acc_data
# def dump_account(account_data):
#     '''
#     after updated transaction or account data , dump it back to file db
#     :param account_data:
#     :return:
#     '''
#     db_path = db_handler.db_handler(settings.DATABASE)
#     account_file = "%s/%s.json" %(db_path,account_data['id'])
#     with open(account_file, 'w') as f:
#         acc_data = json.dump(account_data,f)
#
#     return True

#!_*_coding:utf-8_*_

import json
import time
from s14day5.home_work.atm.core import db_handler
from s14day5.home_work.atm.conf import settings


def load_current_balance(account_id):
    '''
    return account balance and other basic info
    :param account_id:
    :return:
    '''
    acc_data = db_handler.db_handler(settings.DATABASE,account_id)
    return  acc_data

def dump_account(account_data):
    '''
    after updated transaction or account data , dump it back to file db
    :param account_data:
    :return:
    '''
    db_path = db_handler.file_db_handle(settings.DATABASE)
    account_file = "%s/%s.json" %(db_path,account_data['id'])
    with open(account_file, 'w') as f:
        json.dump(account_data,f)

    return True