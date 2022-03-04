import sqlalchemy as db
engine = db.create_engine('mysql+pymysql://root:poto0702@127.0.0.1:3306/als')

#mysql+pymysql://<USERNAME>:<PASSWORD>@<HOST>/<DATABASENAME>

##  -> to find username, use SELECT CURRENT_USER();
##  -> password is the one that u set up during the installation
##  -> host will be the ip address
##  -> database name is the name that u set as well
##
##to find out username and host,
##  - go to mysql connections on the workbench
##  - right click the name of the connection you are using and select Copy Connection String to Clipboard
##
##it will give USERNAME@IP_ADDRESS
##  -> username will be the same result as SELECT CURRENT_USER();
##  -> ip address will be put under host

q = "SELECT * FROM als.member LIMIT 0,5"
rs = engine.execute(q)
for i in rs:
    print(i)

