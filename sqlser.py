import pymysql

global cur,conn

def opensqlserver():
    global cur
    conn = 'bmi'
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db=conn, charset='utf8')
    print(db)
    cur = db.cursor()
    # cur.execute("select * from alldev")

    # sql_select = 'select * from  huarui1 a order by seq desc limit 1'
    sql_select = 'select * from  huarui1'
    print(sql_select)
    cur.execute(sql_select)
    done_set = cur.fetchall()
    print(done_set)

def insertsqlserver(id,addr,wd,sd,tttt):
    global cur

    cur.execute("insert into wsds values(%d,%d,%1f,%1f,%s)"%(id,addr,wd,sd,tttt))
    conn.commit()

def closesqlserver():
    conn.close()

def test_sqlserver():
    server='127.0.0.1,1433'
    user="sa"
    password="Aa123456"
    database="dbtest"
    #conn=pymssql.connect(server='.',user='sa',password='Aa123456',database='dbst')

    #cur.execute("insert into book values(55,66)")
    #sql = "select * from book"
    #cur.execute(sql)
    #cur.execute("select * from book where bno=3")
    #rows = cur.fetchall()
    #cur.execute("create table wsddev(idint int not null primary key,addint int not null,wdfloat float not null,sdfloat float not null,time char(64) not null)")
    #cur.execute("insert into wsddev values(1,1,20.1,61.1,'2018-09-27 14:16:1523')")
    #cur.execute("insert into wsddev values(2,2,21.1,62.1,'2018-09-27 14:17:1523')")
    #cur.execute("insert into alldev values(3,3,23.1,63.1,'2018-09-27 14:18:1523')")
    conn.commit()
    cur.execute("select * from alldev")
    datas = cur.fetchall()
    for row in datas:
    #if (row[0] in nodeSet):
        print(row)
    conn.close()

if __name__ == '__main__':
    opensqlserver()
