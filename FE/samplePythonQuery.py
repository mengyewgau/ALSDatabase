import sqlalchemy as db
engine = db.create_engine('mysql+pymysql://root:poto0702@127.0.0.1:3306/als')
#mysql+pymysql://<USERNAME>:<PASSWORD>@<HOST>/<DATABASENAME>

q = "SELECT * FROM als.member LIMIT 0,5"
rs = engine.execute(q)
for i in rs:
    print(i)

