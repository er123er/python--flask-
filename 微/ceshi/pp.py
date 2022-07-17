import pymysql
from datetime import datetime


def main():
    '''获取mysql连接'''
    conn = pymysql.connect(host='localhost', user='root', port=3306, password='123456789', db='op', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM `wz`;')
    datas = cursor.fetchall()
    # 将 rows转换成 [{},{}]
    cursor.close()
    res = rows_to_dict(cursor.description, datas)
    print(res)
    # [{'id': '1', 'phone': '13399999999', 'username': '超级测试人员'}, {'id': '2', 'phone': '18899999999', 'username': '测试'}]
    conn.close()


def rows_to_dict(descriptions: tuple, datas: tuple):
    '''datas descriptions 为 ((),())'''
    if descriptions == None:
        return None
    if len(datas) == 0:
        return []
    keys = [a[0] for a in descriptions]

    results = []
    for data in datas:
        # data 为tuple ()
        tmp = {}
        for _index, key in enumerate(keys):
            # 日期类型处理
            if isinstance(data[_index], datetime):
                tmp[key] = data[_index].strftime('%Y-%m-%d %H:%M:%S')
            else:
                tmp[key] = data[_index]
        results.append(tmp)
    return results


if __name__ == '__main__':
    main()


