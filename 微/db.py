import random
import pymysql

try:
	db = pymysql.connect(host='localhost', user='root', port=3306, password='123456789', db='op', charset='utf8')
	cur = db.cursor()
# print('成功！')
except Exception as e:
	print('数据库连接失败！', str(e))


def sql_query():
	# SELECT * from tou WHERE id ='1';
	sql = """SELECT * from tou WHERE id ='1';"""
	cur.execute(sql)
	db.commit()
	
	return cur.fetchall()[0][1]


def sql_query_wz():
	sql = f'''SELECT * FROM `sc`  LIMIT 0, 1000;'''
	cur.execute(sql)
	db.commit()
	return cur.fetchall()


def sql_query_wzz(iud=1):
	sql = f'''SELECT * FROM `sc` WHERE id ='{iud}';'''
	cur.execute(sql)
	db.commit()
	return cur.fetchall()


def sql_insert():
	sql = """INSERT INTO `tou` (`name`) VALUES ('小王');"""
	cur.execute(sql)
	db.commit()
	return cur.fetchall()


def sql_insert_register(name, password):
	sql = f"""INSERT INTO `login` (`mail`, `password`) VALUES ('{name}', '{password}');"""
	cur.execute(sql)
	db.commit()
	return cur.fetchall()


def sql_insert_wzz(wzb, wzw):
	sql = f"""INSERT INTO `wz` (`title`, `ni`) VALUES ('{wzb}', '{wzw}')"""
	cur.execute(sql)
	db.commit()
	return cur.fetchall()


def sql_del():
	sql = '''DELETE FROM tou WHERE name='小王';'''
	cur.execute(sql)
	db.commit()


def sql_modify(to='小王'):
	tou = sql_query()
	sql = f'''UPDATE `tou` SET `name`='{to}' WHERE (`name`='{tou}');'''
	cur.execute(sql)
	db.commit()


def sql_modify_wz(to='小王'):
	tou = sql_query()
	sql = f'''UPDATE `wz` SET `title`='啊实打实打算大苏打' WHERE (`id`='6');'''
	# sql = f'''UPDATE `wz` SET `title`=' 苏打', `ni`=' 哈哈' WHERE (`id`='6');'''
	cur.execute(sql)
	db.commit()


def sql_query_login():
	sql = """SELECT * from login WHERE mail='q@qq.com' AND `password`='123456789';;"""
	cur.execute(sql)
	db.commit()
	return cur.fetchall()[0]


def sql_query_sc():
	sql = f'''SELECT * from gs ;'''
	cur.execute(sql)
	db.commit()
	return random.choice(cur.fetchall())[1]


def sql_query_sp():
	sql = """SELECT * from sp;"""
	cur.execute(sql)
	db.commit()
	return cur.fetchall()


if __name__ == '__main__':
	db = pymysql.connect(host='localhost', user='root', port=3306, password='123456789', db='op', charset='utf8')
	cur = db.cursor()
	sql = f'''SELECT * FROM `sp`;'''
	cur.execute(sql)
	db.commit()
	#print(cur.fetchall())
	print(cur.fetchall())