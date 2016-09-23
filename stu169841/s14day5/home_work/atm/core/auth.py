#!_*_coding:utf-8_*_

import os
from s14day5.home_work.atm.core import db_handler
from s14day5.home_work.atm.conf import settings
from s14day5.home_work.atm.core import logger
import json
import time

def acc_auth(account,password):
    '''
    account auth func
    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication , retun the account object, otherwise ,return None
    :return accont : {"status": 0, "password": "abc", "expire_date": "2021-01-01", "balance": 16223.55, "pay_day": 22, "id": 1234, "enroll_date": "2016-01-02", "credit": 15000}
    '''
    account_data = db_handler.db_handler(settings.DATABASE,account)
    print(account_data)
    if account_data['password'] == password:
        exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'], "%Y-%m-%d"))
        if time.time() >exp_time_stamp:
            print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
        else: #passed the authentication
            return  account_data   #auth success return account_data
    else:
        print("\033[31;1mAccount ID or password is incorrect!\033[0m")


def acc_login(user_data,log_obj):
    '''
    account login func
    :user_data: user info data , only saves in memory
    :return: {"status": 0, "password": "abc", "expire_date": "2021-01-01", "balance": 16223.55, "pay_day": 22, "id": 1234, "enroll_date": "2016-01-02", "credit": 15000}
    '''
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3 :   #user_data['is_authenticated']条件为Flase的时候条件成立
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth = acc_auth(account, password)
        if auth: #not None means passed the authentication
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            #print("welcome")
            return auth
        else:
            log_obj.error("account [%s] auth login flase" % account)
        retry_count +=1

    log_obj.error("account [%s] too many login attempts" % account)
    exit()
