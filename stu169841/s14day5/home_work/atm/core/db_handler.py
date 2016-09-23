#!_*_coding:utf-8_*_
import os
import json

def file_db_handle(conn_params):
    '''
    parse the db file path
    :param conn_params: the db connection params set in settings
    :return:
    '''
    print('file db:',conn_params)
    db_path ='%s/%s' %(conn_params['path'],conn_params['name'])
    return db_path  #D:\oldboy_python14\stu169841\s14day5\home_work\atm\db\accounts
def db_handler(conn_parms,account):
    '''
    connect to db
    :param conn_parms: the db connection params set in settings
    :return:a
    '''
    """
    DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name':'accounts',
    'path': "%s/db" % BASE_DIR
}
    """

    if conn_parms['engine'] == 'file_storage':
        db_path = file_db_handle(conn_parms)
        account_file = "%s/%s.json" %(db_path,account)
        print(account_file)
        if os.path.isfile(account_file):
            with open(account_file,'r') as f:
                return json.load(f)
        else:
            print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)
            exit()