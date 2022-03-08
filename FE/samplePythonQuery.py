import sqlalchemy as db
engine = db.create_engine('mysql+pymysql://root:password@127.0.0.1:3306/alsdatabase')

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

## Creation

membershipId = "A101A"
memName = "Hermione Granger"
memFace = "Science"
memPhone = "33336663"
memEmail = "flying@als.edu"

##try:
##    createMem = 'INSERT INTO member VALUES ("{0}","{1}", "{2}", "{3}", "{4}", 5.00)'.format(membershipId,
##                                                                                            memName,
##                                                                                            memFace,
##                                                                                            memPhone,
##                                                                                            memEmail)
##    engine.execute(createMem)
##except:
##    print("Creation Error")


## Deletion
fine = -1
retrieveFine = 'SELECT currFine FROM member WHERE membershipId = "{0}"'.format(membershipId)
fineResult = engine.execute(retrieveFine)
for n in fineResult:
    fine = n[0]

if fine == 0:
    deleteMem = 'DELETE FROM member WHERE membershipId="{0}" and currFine=0.00'.format(membershipId)
    engine.execute(deleteMem)
else:
    print("Deletion Error")


## Updating Records

q = "SELECT * FROM member LIMIT 0,5"
rs = engine.execute(q)

for r in rs:
    print(r)
