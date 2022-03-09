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




##deleteMem = 'DELETE FROM member WHERE membershipId="{0}" and currFine=0.00'.format(membershipId)
##engine.execute(deleteMem)

############################################################################################################################

### Main Functions

def loanBook(membershipId, accessionNum, currDate):
    loanQuota = checkMemQuota(membershipId, "Book");
    resQuota = checkMemQuota(membershipId, "Reservation");
    fineAmt = checkFineValue(membershipId);
    dueDate = checkDueDate(accessionNum);


    if loanQuota < 2:
        return("Loan Quota Exceeded");
    elif fineAmt == 0:
        return("Outstanding Fines")
    elif checkIfBookOnLoan(accessionNum):
        return("Book currently on Loan until {0}".format(dueDate));
    else:
        
        loanBk = 'UPDATE Book SET date="{0}", membershipId="{1}" WHERE accessionNum="{2}"'.format(currDate,
                                                                                                  membershipId,
                                                                                                  accessionNum)
        engine.execute(loanBk)
    return "Loan Success!"

def returnBook(accessionNum, membershipId, returnDate):
    # Compute how much fine does the member own
    dueDate = checkDueDate(accessionNum);
    fineAmt = dateDiff(returnDate, dueDate) # Fine is $1/day
    qAddFine = 'UPDATE Member SET currFine=currFine+{0} where membershipId="{1}"'.format(fineAmt,
                                                                                         membershipId)
    engine.execute(qAddFine)
    # Mark the book as returned in the Book Relation
    qReturn = 'UPDATE Book SET date=NULL, membershipId=NULL WHERE accessionNum="{0}"'.format(accessionNum)
    engine.execute(qReturn)


def payFine(membershipId, paidDate, paidAmt):
    correctFineVal = checkFineValue(membershipId)

    if correctFineVal == 0:
        return "Member has no fine"
    elif correctFineVal != paidAmt:
        return "Incorrect fine payment amount."
    else:
        paymentQuery = 'INSERT INTO Payment VALUES("{0}", "{1}", "{2}");'.format(membershipId,
                                                                                paidDate,
                                                                                paidAmt);
        updateMemQ = 'UPDATE Member SET currFine=0 WHERE membershipId="{0}"'.format(membershipId);
        engine.execute(paymentQuery);
        engine.execute(updateMemQ);
############################################################################################################################

def deleteMember(membershipId):
    currFine = checkFineValue(membershipId);
    if currFine > 0:
        return 'Member has loans, reservations or outstanding fines'
    try:
        deleteMember = 'DELETE FROM Member WHERE membershipId = "{0}"'.format(membershipId)
        engine.execute(deleteMember)
    except:
        print('Member has loans, reservations or outstanding fines')

def withdrawBook(accessionNum):
    
    if checkIfBookOnLoan(accessionNum):
        raise Exception("Books is on Loan");
    try:
        deleteMember = 'DELETE FROM Book WHERE accessionNum = "{0}"'.format(accessionNum)
        engine.execute(deleteMember)
    except:
        print("Book has reservations")


def deleteReservation(membershipId, accessionNum):     
    if checkReservation(accessionNum, membershipId) > 0:
        delRes = 'DELETE FROM Reservation WHERE membershipId = "{0}" and accessionNum ="{1}"'.format(membershipId,
                                                                                                     accessionNum)
        engine.execute(delRes)
    else:
        raise Exception("Reservation does not exist")

############################################################################################################################


def updateMember(membershipId, memName, memFac, memPhone, memEmail):
    
    updateMem = 'UPDATE Member SET memName="{1}", memFac="{2}", memPhone="{3}", memEmail="{4}" WHERE membershipId="{0}"'.format(membershipId, 
                                                                                                                                memName,
                                                                                                                                memFac,
                                                                                                                                memPhone,
                                                                                                                                memEmail)
    engine.execute(updateMem)


############################################################################################################################
### Insertion Functions
def createMember(membershipId, memName, memFace, memPhone, memEmail):
    try:
        createMem = 'INSERT INTO member VALUES ("{0}","{1}", "{2}", "{3}", "{4}", 0)'.format(membershipId,
                                                                                                memName,
                                                                                                memFace,
                                                                                                memPhone,
                                                                                                memEmail)
        engine.execute(createMem)
    except:
        raise Exception("Creation Error")

def createBook(accessionNum, title, ISBN, publisher, pubYear):
    try:
        createBk = 'INSERT INTO Book (accessionNum, title, ISBN, publisher, pubYear)'
        bookValues = 'VALUES ("{0}","{1}", "{2}", "{3}", "{4}")'.format(accessionNum,
                                                                              title,
                                                                              ISBN,
                                                                              publisher,
                                                                              pubYear)
        createQuery = createBk + bookValues
        engine.execute(createQuery)
    except:
        print("Creation Error")

def reserveBook(membershipId, accessionNum, date):

    fineAmt = checkFineValue(membershipId);
    resQuota = checkMemQuota(membershipId, "Reservation");

    if fineAmt > 0:
        raise Exception("O$P$")
    elif resQuota == 2:
        raise Exception("KNNCB")
    else:
        queryResBk = 'INSERT INTO Reservation VALUES("{0}", "{1}", "{2}")'.format(accessionNum,
                                                                                  membershipId,
                                                                                  date)
        engine.execute(queryResBk)

def createBkAuthor(accessionNum, author):
    createAuthor = 'INSERT INTO BookAuthor VALUES("{0}", "{1}")'.format(accessionNum,
                                                                        author)

    engine.execute(createAuthor)

############################################################################################################################

### Checking Functions

def checkFineValue(membershipId): #FE Facing
    # Returns current fine value of membershipId
    retrieveFine = 'SELECT currFine FROM member WHERE membershipId = "{0}"'.format(membershipId)
    fineResult = engine.execute(retrieveFine).fetchone()[0]
    return fineResult

def checkMemQuota(memId, relation): #FE Facing
    # Returns books loaned/reserved, depending on relation given
    retrieveLoan = 'SELECT membershipId FROM {0} WHERE membershipId = "{1}"'.format(relation, memId)
    result = engine.execute(retrieveLoan).fetchall()
    return len(result)


def checkReservation(accessionNum, membershipId):
    queryReservation = 'SELECT EXISTS(SELECT * FROM Reservation where accessionNum="{0}" and membershipId="{1}");'.format(accessionNum,
                                                                                                                        membershipId)
    return engine.execute(queryReservation).fetchone()[0]

def checkDueDate(accessionNum): # Book for due date, Reservation for Reservation Date
    # Returns Loan Date of item
    queryDate = 'SELECT date FROM Book WHERE accessionNum = "{0}"'.format(accessionNum)
    loanDate = engine.execute(queryDate).fetchone()[0]
    # Check Resevation
    if loanDate == None:
        return 0
    return loanDate + timedelta(days=14)

def checkIfBookOnLoan(accessionNum):
    queryLoan = 'SELECT membershipId FROM Book where accessionNum="{0}"'.format(accessionNum)
    haveLoan = engine.execute(queryLoan).fetchone()[0]
    
    # If bool(haveLoan) is true, book is on already on loan
    return bool(haveLoan)
############################################################################################################################


### Report Functions
def bookSearchReport(word, category): 
    queryBookInfo = 'SELECT accessionNum, title, ISBN, publisher, pubYear FROM Book where {0} LIKE "%%{1}%%";'.format(category,
                                                                                                                      word)
    bookInfoList = engine.execute(queryBookInfo).fetchall()

    for index in range(len(bookInfoList)):
        acNum = bookInfoList[index][0];
        queryAuthors = "SELECT GROUP_CONCAT(authorName, ' ') FROM BookAuthor WHERE accessionNum='{0}'".format(acNum);
        authors = engine.execute(queryAuthors).fetchone()[0]
        
        bookInfoList[index] = bookInfoList[index][0:2] + (authors,) + bookInfoList[index][2:]

    return bookInfoList;

def loanReport():
    ## Returns loan report
    queryBookInfo = 'SELECT accessionNum, title, ISBN, publisher, pubYear FROM Book where membershipId != " ";'

    bookInfoList = engine.execute(queryBookInfo).fetchall()
    

    for index in range(len(bookInfoList)):
        acNum = bookInfoList[index][0];
        queryAuthors = "SELECT GROUP_CONCAT(authorName, ' ') FROM BookAuthor WHERE accessionNum='{0}'".format(acNum);
        authors = engine.execute(queryAuthors).fetchone()[0]
        
        bookInfoList[index] = bookInfoList[index][0:2] + (authors,) + bookInfoList[index][2:]
        
    return bookInfoList;

def reservationReport():
    ## Returns reservations report
    qResReport = 'SELECT b.accessionNum, title, m.membershipId, memberName FROM Reservation r, Book b, Member m WHERE r.accessionNum = b.accessionNum AND r.membershipId=m.membershipId;'

    return engine.execute(qResReport).fetchall()

def outsFineReport():
    # Returns members with outstanding fines report
    queryFineReport = 'SELECT "membershipId","memName","memFac","memPhone","memEmail" FROM Member WHERE currFine > 0'
    return engine.execute(queryFineReport).fetchall()

def bookLoanedToMemReport(membershipId):
    queryBookInfo = 'SELECT accessionNum, title, ISBN, publisher, pubYear FROM Book where membershipId = "{0}";'.format(membershipId)
    bookInfoList = engine.execute(queryBookInfo).fetchall()

    for index in range(len(bookInfoList)):
        acNum = bookInfoList[index][0];
        queryAuthors = "SELECT GROUP_CONCAT(authorName, ' ') FROM BookAuthor WHERE accessionNum='{0}'".format(acNum);
        authors = engine.execute(queryAuthors).fetchone()[0]
        
        bookInfoList[index] = bookInfoList[index][0:2] + (authors,) + bookInfoList[index][2:]

    return bookInfoList;



### Helper Functions
def dateDiff(endDate, startDate):
    queryDate = 'SELECT DATEDIFF("{0}", "{1}")'.format(endDate, startDate)
    daysDiff = engine.execute(queryDate).fetchone()[0]
    if daysDiff > 14:
        return daysDiff
    return 0;



id1 = "A101A"
n1 = "Hermione Granger"
f1 = "Science"
p1 = "33336663"
e1 = "flying@als.edu"

id2 = "A102A"
n2 = "Ronald Ranger"
f2 = "BZA"
p2 = "12336663"
e2 = "bobo@als.edu"

id3 = "A103A"
n3 = "Hairy Granger"
f3 = "Com"
p3 = "35234895"
e3 = "wand@als.edu"

an1 = "A01"
t1 = "Animal Farm"
au1a = "George Orwell"
au1b = "Sim Lim Square"
i1 = "9790000000001"
pub1 = "Intra S.r.l.s."
py1 = "2021"

##createMember(id1, n1, f1, p1, e1)
##createMember(id2, n2, f2, p2, e2)
##createMember(id3, n3, f3, p3, e3)

##deleteMember(id1)

##createBook(an1, t1, i1, pub1,py1)
##createBkAuthor(an1, au1a)
##createBkAuthor(an1, au1b)

loanBook(id2, an1, "2022/03/09")
