import sqlalchemy as db
from datetime import *
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


##
##def deleteMember(membershipId):
##    fine = -1
##    retrieveFine = 'SELECT currFine FROM member WHERE me'
##
##    if fine == 0:
##        deleteMem = 'DELETE FROM member WHERE membershipId="{0}" and currFine=0'.format(membershipId)
##        engine.execute(deleteMem)
##    else:
##        print("Deletion Error")


##deleteMem = 'DELETE FROM member WHERE membershipId="{0}" and currFine=0.00'.format(membershipId)
##engine.execute(deleteMem)


### Main Functions

def loanBook(accessionNum, membershipId, currDate):
    loanQuota = checkMemQuota(membershipId, "Loan");
    resQuota = checkMemQuota(membershipId, "Reservation");
    fineAmt = checkFineValue(membershipId);
    dateDiff = dateDiff(checkLoanDate(accessionNum), currDate)
    resDate = checkResDate(accessionNum)
    if loanQuota < 2:
        print("Loan Quota Exceeded");
    elif fineAmt == 0:
        print("Outstanding Fines")
    elif date < availDate:
        print("Book on loan");
    else:
        loanBk = 'UPDATE Book SET date="{0}", membershipId="{1}" WHERE accessionNum="{2}"'.format(currDate,
                                                                                                  membershipId,
                                                                                                  accessionNum)
        engine.execute(loanBk)
    return "Loan Success!"

def reserveBook():
    return

def returnBook(accessionNum, membershipId, returnDate):

    # Compute how much fine does the member own
    dueDate = checkRelationDate(accessionNum, "Book");
    numDays = dateDiff(returnDate, dueDate)
    print(numDays)

    # Mark the book as returned in the Book Relation
    qReturn = 'UPDATE Book SET date=NULL, membershipId=NULL WHERE accessionNum="{0}"'.format(accessionNum)
    



def deleteMember(membershipId):
    ## Incomplete function, DELETE CASCADE
    deleteMember = 'DELETE FROM Member WHERE membershipId = "{0}"'.format(membershipId)
    deleteReserve = 'DELETE FROM Reservation WHERE membershipId = "{0}"'.format(membershipId)
    engine.execute(deleteReserve)
    engine.execute(deleteMember)
    return 'Reservations and Member details by "{0}" Deleted'.format(membershipId)


def updateMember():
    return
### Insertion Functions
def createMember(membershipId, memName, memFace, memPhone, memEmail):
    try:
        createMem = 'INSERT INTO member VALUES ("{0}","{1}", "{2}", "{3}", "{4}", 5.00)'.format(membershipId,
                                                                                                memName,
                                                                                                memFace,
                                                                                                memPhone,
                                                                                                memEmail)
        engine.execute(createMem)
    except:
        print("Creation Error")

def createBook(accessionNum, title, ISBN, publisher, pubYear):
    try:
        createBk = 'INSERT INTO Book (accessionNum, title, ISBN, publisher, pubYear)'
        bookValues = 'VALUES ("{0}","{1}", "{2}", "{3}", "{4}", 5.00)'.format(accessionNum,
                                                                              title,
                                                                              ISBN,
                                                                              publisher,
                                                                              pubYear)
        engine.execute(createBk + bookValues)
    except:
        print("Creation Error")


### Checking Functions

def checkFineValue(membershipId):
    # Returns current fine value of membershipId
    retrieveFine = 'SELECT currFine FROM member WHERE membershipId = "{0}"'.format(membershipId)
    fineResult = engine.execute(retrieveFine).fetchone()[0]
    return fineResult

def checkMemQuota(memId, relation):
    # Returns books loaned/reserved, depending on relation given
    retrieveLoan = 'SELECT membershipId FROM {0} WHERE membershipId = "{1}"'.format(relation, memId)
    result = engine.execute(retrieveLoan).fetchall()
    return len(result)

def checkRelationDate(accessionNum, relation): # Book for due date, Reservation for Reservation Date
    # Returns Loan Date of item
    queryDate = 'SELECT date FROM {0} WHERE accessionNum = "{1}"'.format(relation,
                                                                         accessionNum)
    datetimeStr = engine.execute(queryDate).fetchone()
    print(type(datetimeStr))
    # Check Resevation
    return datetime.strptime(datetimeStr, "%y/%m/%d")

def isReserved(accessonNum):
    queryReservation = 'SELECT accessionNum FROM Reservation where accessionNum="{0}"'.format(accessionNum)
    return len(engine.execute(queryReservation).fetchall()) > 0

##def checkResDate(accessionNum, membershipId):
##    # Returns latest res date
##    queryResDate = 'SELECT date FROM Reservation WHERE accessionNum = "{0}" and membershipId = "{1}"'.format(accessionNum,
##                                                                                                             membershipId)
##    datetimeStr = engine.execute(queryResDate).fetchone()
##    # Returns a string format --> To convert into DATETIME 
##    return datetime.strptime(datetimeStr, "%y/%m/%d")



### Report Functions
def bookReport():
    return

def loanReport():
    ## Returns reservations report
    queryLoanReport = 'SELECT accessionNum, title, memberName FROM Book'

    return engine.execute(queryLoanReport).fetchall()


def reservationReport():
    ## Returns reservations report
    qResReport = 'SELECT b.accessionNum, title, m.membershipId, memberName FROM Reservation r, Book b, Member m WHERE r.accessionNum = b.accessionNum AND r.membershipId=m.membershipId;'

    return engine.execute(qResReport).fetchall()

def outsFineReport():
    # Returns members with outstanding fines report
    queryFineReport = 'SELECT "membershipId","memName","memFac","memPhone","memEmail" FROM Member WHERE currFine > 0'
    return engine.execute(queryFineReport).fetchall()

def bookLoanedToMemReport(membershipId):
    return



### Helper Functions
def dateDiff(date1, date2):
    return abs(date2-date1)



membershipId = "A101A"
memName = "Hermione Granger"
memFace = "Science"
memPhone = "33336663"
memEmail = "flying@als.edu"

returnBook("A01", "A101A", "2022/03/10")
