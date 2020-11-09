import sqlite3
conn = sqlite3.connect('AA_db.sqlite')
cur = conn.cursor()



cur.execute('CREATE TABLE wordcount (word VARCHAR NOT NULL PRIMARY KEY,count INT NOT NULL)')

conn.commit()
print("hai1")

cur.execute('CREATE TABLE twc (two_words VARCHAR NOT NULL PRIMARY KEY,count INT NOT NULL)')

conn.commit()
print("hai1")
cur.execute('CREATE TABLE npw (word VARCHAR NOT NULL PRIMARY KEY,next VARCHAR NOT NULL)')
conn.commit()
print("hai1")

cur.execute('CREATE TABLE probability (two_words VARCHAR NOT NULL PRIMARY KEY ,prob DOUBLE NOT NULL)')

conn.commit()
# print("hai1")
# cur.execute("create table run(first varchar primary key,val INT not null)")



cur.execute('CREATE TABLE run (two_words VARCHAR NOT NULL PRIMARY KEY ,prob DOUBLE NOT NULL)')

conn.commit()
val=("done",1)
cur.execute("insert into run values(?,?)",val)
conn.commit()
print("hao")




#
#
# cur.execute(sql, val)
# conn.commit()
# print("hey")
#
# cur.execute('SELECT * FROM wordcount')
# f = cur.fetchall()
# print(f)
#
# sql = "select count from wordcount WHERE word='"+l+"'"
# cur.execute(sql)
# k=cur.fetchall()
#
# tag=0;
# for u in k:
#     t=list(u)
#     for y in t:
#         co=y
#         tag=1;
#
# if(tag==0):
#     sql="insert into wordcount values(?,?)"
#     val=("rk",30)
#     cur.execute(sql,val)
#
# else:
#     co=co+1
#     co=str(co)
#     sql="UPDATE wordcount SET count ="+co+" WHERE word='"+l+"'"
#     cur.execute(sql)
#
# conn.commit()


# cur.execute('SELECT * FROM wordcount')
# f = cur.fetchall()
# print(f)
# print("\n"*5)

# cur.execute('SELECT * FROM npw')
# f = cur.fetchall()
# print(f)
# print("\n"*5)
#
# cur.execute('SELECT * FROM twc')
# f = cur.fetchall()
# print(f)
# print("\n"*5)

# cur.execute('SELECT * FROM probability')
# f = cur.fetchall()
# print(f)
# print("\n"*5)



# cur.execute("drop table wordcount")
# cur.execute("drop table npw")
# cur.execute("drop table twc")
# cur.execute("drop table probability")
# conn.commit()
# print("hai")






# #
# data="తిరుమలగిరి&పెదతుమ్మిడి&టేకుమట్ల&ఉండవల్లి&తిమ్మాపురం";
# dt=data.split("&")
# print(dt)

# cur.execute("drop table run")
# conn.commit()
# print("hai")