import pymysql
from common.get_case_info import GetCaseInfo
import logging
log = logging.getLogger(__name__)


class DbOperations:
    def __init__(self):
        self.conn = pymysql.connect(host='', user="", passwd="", db="")
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def select_data(self, sql):
        log.info("开始查询测试数据")
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # self.cursor.close()
        # self.conn.close()
        log.info("数据库连接关闭成功")
        return result

    def get_db_result(self):
        case_info_list = GetCaseInfo().get_case_info()
        # [{'case1': {'origin': 'select nickname from users;', 'current': 'select nickname from users_copy;'}}]
        compare_data_list = []
        for case_info in case_info_list:
            case_name = list(case_info.keys())[0]
            origin_sql = case_info[case_name]['origin']
            current_sql = case_info[case_name]['current']

            origin_result = self.select_data(origin_sql)
            current_result = self.select_data(current_sql)
            compare_data = (case_name, origin_result, current_result)
            compare_data_list.append(compare_data)
        return compare_data_list
        # [('case1', [{'nickname': 'admin'}, {'nickname': 'test1'}], [{'nickname': 'admin'}, {'nickname': 'test1'}]),
        # ('case2', [{'email': 'pei.chen@thoughtworks.com'}, {'email': None}], [{'email': 'pei.chen@thoughtworks.com'}, {'email': '123@qq.com'}])]


if __name__ == '__main__':
    # sql = "select * from users;"
    # print(DbOperations().select_data(sql))
    print(DbOperations().get_db_result())