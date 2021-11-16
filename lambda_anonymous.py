'''fact=lambda x:1 if x==0 else x*fact(x-1)
print(fact(5))

def fun(n):
    if n==0:
        return 1
    else:
        return n* fun(n-1)
print(fun(5))'''

''''def fun(n):
    return n+n
print(list(map(fun,[1,2,3])))'''

'''z=(list(filter(lambda x:x in['a','i','e','o','u'],['v','i','n','o'])))
print(z)'''

'''z=(list(filter(lambda x:x ,[1,2,3])))
print(z)'''

''''a=list(map(lambda x:x.upper(),['vin','sha']))
print(a)'''

'''import functools
s=functools.reduce(lambda x,y:x if x>y else y,[1,2,3])
print(s)'''

'''import sqlite3
con = sqlite3.connect('example.db')
print('connect')
con.execute('''#create table employee
#(id int primary key not null,
# name text not null,
 #age int,
 #alary real);
''')
con.close()
print('table created')'''

''''import sqlite3
con=sqlite3.connect('example.db')
con.execute("insert into employee values(1,'vinoth',24,20000)")
con.execute("insert into employee values(2,'harish',23,30000)")
con.execute("insert into employee values(3,'vinoth',21,220000)")
con.execute("insert into employee values(4,'vinoth',28,40000)")
con.execute("insert into employee values(5,'vinoth',27,50000)")
con.execute("insert into employee values(6,'vinoth',26,60000)")
con.commit()
con.close()
print('commit successfully')'''

#import cx_Oracle

#con = cx_Oracle.connect('hr/hr@localhost')

#print("Successfully connected to Oracle Database")

# importing module
import cx_Oracle
con = cx_Oracle.connect('hr/hr@localhost')
print(con.version)

# Now execute the sqlquery
cursor = con.cursor()

# Creating a table employee
cursor.execute("create table secondtable(empid integer primary key, name varchar2(30), salary number(7))")

print("Table Created successfully")

'''import cx_Oracle
con=cx_Oracle.connect('hr/hr@localhost')
cur=con.cursor()
cur.execute("insert into firstTbale values(1,'vinoth',20000)")
con.close()'''


import cx_Oracle as o
con=o.connect('hr/hr@localhost')
cur=con.cursor()
cur.execute("select count(*) from all_tables where owner='hr'")
rows = cur.fetchall()
count=0
for i in rows:
    count+=1
    print(i)
print(count)








