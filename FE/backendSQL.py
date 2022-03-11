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

#############################################################################################################################################################################

### Main Functions

## Loan Books

def loanBook(membershipId, accessionNum, currDate):
    loanQuota = checkMemQuota(membershipId, "Book");
    resQuota = checkMemQuota(membershipId, "Reservation");
    fineAmt = checkFineValue(membershipId);
    derivedDueDate = datetime.strptime(currDate, "%Y/%m/%d") + timedelta(days=14)

    if loanQuota >= 2:
        raise Exception("Loan Quota Exceeded");
    elif fineAmt != 0:
        raise Exception("Outstanding Fines")
    elif checkIfBookOnLoan(accessionNum):
        currDueDate = checkDueDate(accessionNum); # Checks from Book what is the current dueDate
        raise Exception("Book currently on Loan until {0}".format(currDueDate));
    else:    
        loanBk = 'UPDATE Book SET dueDate="{0}", membershipId="{1}" WHERE accessionNum="{2}"'.format(derivedDueDate,
                                                                                                  membershipId,
                                                                                                  accessionNum)
        engine.execute(loanBk)
        return "Loan Success!"
    
def confirmLoan(membershipId, accessionNum, currDate):
    ## Loan Confirmation Page
    bookLoanQuery = 'SELECT accessionNum, title FROM Book WHERE accessionNum="{0}"'.format(accessionNum);
    bookInfo = engine.execute(bookLoanQuery).fetchone()

    derivedDueDate = datetime.strptime(currDate, "%Y/%m/%d") + timedelta(days=14)
    
    memberLoanQuery = "SELECT membershipId, memberName FROM Member WHERE membershipId='{0}'".format(membershipId);
    memInfo = engine.execute(memberLoanQuery).fetchone()
    if not bool(memInfo) or not bool(bookInfo):
        raise Exception("No empty fields allowed");
    return (bookInfo, currDate, memInfo, derivedDueDate.strftime("%Y/%m/%d"))

## Returning Books

def returnBook(accessionNum, returnDate):
    # Compute how much fine does the member own
    dueDate = checkDueDate(accessionNum);
    fineAmt = dateDiff(returnDate, dueDate) # Fine is $1/day
    bookLoanQuery = 'SELECT accessionNum, title, membershipId FROM Book WHERE accessionNum="{0}"'.format(accessionNum);
    bookInfo = engine.execute(bookLoanQuery).fetchone()

    ## Make sure return date is after due date
    if fineAmt < 0:
        raise Exception("Return date cannot be before due date")
    membershipId = bookInfo[-1]
    addFineQ = 'UPDATE Member SET currFine=currFine+{0} where membershipId="{1}"'.format(fineAmt,
                                                                                         membershipId)
    engine.execute(addFineQ)
    # Mark the book as returned in the Book Relation
    qReturn = 'UPDATE Book SET dueDate=NULL, membershipId=NULL WHERE accessionNum="{0}"'.format(accessionNum)
    engine.execute(qReturn)        
    
    nextId = checkNextReservation(accessionNum)
    if bool(nextId):
        # Delete his reservation
        cancelReservation(nextId, accessionNum);
        # Loan him the book
        loanBook(nextId, accessionNum, returnDate);

    if checkFineValue(membershipId) > 0:
        return "Warning! Member has outstanding fines to pay"
    return "Return sucessful. Member has no outstanding fines"

def confirmReturn(accessionNum, returnDate):
    ## Return Confirmation Page
    dueDate = checkDueDate(accessionNum);
    fineAmt = dateDiff(returnDate, dueDate)
    
    bookLoanQuery = 'SELECT accessionNum, title, membershipId FROM Book WHERE accessionNum="{0}"'.format(accessionNum);
    bookInfo = engine.execute(bookLoanQuery).fetchone()

    membershipId = bookInfo[-1]
    memberLoanQuery = "SELECT memberName FROM Member WHERE membershipId='{0}'".format(membershipId);
    memInfo = engine.execute(memberLoanQuery).fetchone()[0]
    
    return (bookInfo[0], bookInfo[1], bookInfo[2], memInfo, returnDate, fineAmt);

## Fine payments

def payFine(membershipId, paidDate, paidAmt):
    correctFineVal = checkFineValue(membershipId)

    if correctFineVal == 0:
        raise Exception("Member has no fine")
    elif correctFineVal != paidAmt:
        raise Exception("Incorrect fine payment amount.")
    else:
        paymentQuery = 'INSERT INTO Payment VALUES("{0}", "{1}", "{2}");'.format(membershipId,
                                                                                paidDate,
                                                                                paidAmt);
        updateMemQ = 'UPDATE Member SET currFine=0 WHERE membershipId="{0}"'.format(membershipId);
        engine.execute(paymentQuery);
        engine.execute(updateMemQ);

def confirmFinePayment(membershipId, paidDate, paidAmt):
    ## Return fine confirmation page
    return ("$"+str(paidAmt), membershipId, "Exact Fee Only", paidDate)

## Reserve Books

def reserveBook(membershipId, accessionNum, date):

    fineAmt = checkFineValue(membershipId);
    resQuota = checkMemQuota(membershipId, "Reservation");

    if fineAmt > 0:
        raise Exception("Member has outstanding Fine")
    elif resQuota >= 2:
        raise Exception("Member has exceed reservation quota")
    else:
        queryResBk = 'INSERT INTO Reservation VALUES("{0}", "{1}", "{2}")'.format(accessionNum,
                                                                                  membershipId,
                                                                                  date)
        engine.execute(queryResBk)
def confirmReservation(membershipId, accessionNum, reserveDate):
    ## Reservation Confirmation Page
    bookLoanQuery = 'SELECT accessionNum, title FROM Book WHERE accessionNum="{0}"'.format(accessionNum);
    bookInfo = engine.execute(bookLoanQuery).fetchone()
    
    memberLoanQuery = "SELECT membershipId, memberName FROM Member WHERE membershipId='{0}'".format(membershipId);
    memInfo = engine.execute(memberLoanQuery).fetchone()

    if not bool(bookInfo) or not bool(memInfo):
        raise Exception("MemberId/Accesion Number fields are wrong!")
    else:
        return (bookInfo[0], bookInfo[1], memInfo[0], memInfo[1], reserveDate)


#############################################################################################################################################################################

### Deletion and Withdrawal Functions

## Delete Member

def deleteMember(membershipId):
    currFine = checkFineValue(membershipId);
    if currFine > 0:
        raise Exception('Member has loans and/or outstanding fines')
    try:
        deleteMember = 'DELETE FROM Member WHERE membershipId = "{0}"'.format(membershipId)
        engine.execute(deleteMember)
    except:
        raise Exception('Member has loans and/or outstanding fines')
    
def confirmDeletion(membershipId):
    ## Return Deletion Confirmation Page
    queryMember = 'SELECT * FROM Member WHERE membershipId = "{0}"'.format(membershipId)
    result = engine.execute(queryMember).fetchone()
    if bool(result):
        return result[0:5]
    else:
        raise Exception("Member does not exist");

## Withdraw Book

def withdrawBook(accessionNum):
    
    if checkIfBookOnLoan(accessionNum):
        raise Exception("Books is on Loan");
    try:
        withdrawBook = 'DELETE FROM Book WHERE accessionNum = "{0}"'.format(accessionNum)
        engine.execute(withdrawBook)
    except:
        raise Exception("Book has reservations")

def confirmWithdrawal(accessionNum):
    ## Return Withdrawal Confirmation Page
    withdrawalQ = 'SELECT accessionNum, title, ISBN, publisher, pubYear FROM Book WHERE accessionNum="{0}"'.format(accessionNum);
 
    bookInfoList = engine.execute(withdrawalQ).fetchone()
    
    queryAuthors = "SELECT GROUP_CONCAT(authorName, ' ') FROM BookAuthor WHERE accessionNum='{0}'".format(accessionNum);
    authors = engine.execute(queryAuthors).fetchone()[0]
    
    bookInfoList = bookInfoList[0:2] + (authors,) + bookInfoList[2:]
        
    return bookInfoList;

## Cancel Reservation

def cancelReservation(membershipId, accessionNum):     
    if checkReservationToBeDeleted(membershipId, accessionNum) > 0:
        delRes = 'DELETE FROM Reservation WHERE membershipId = "{0}" and accessionNum ="{1}"'.format(membershipId,
                                                                                                     accessionNum)
        engine.execute(delRes)
    else:
        raise Exception("Reservation does not exist")

def confirmCancel(membershipId, accessionNum, cancelDate):
    ## Cancel Confirmation Page
    bookLoanQuery = 'SELECT accessionNum, title FROM Book WHERE accessionNum="{0}"'.format(accessionNum);
    bookInfo = engine.execute(bookLoanQuery).fetchone()
    
    memberLoanQuery = "SELECT membershipId, memberName FROM Member WHERE membershipId='{0}'".format(membershipId);
    memInfo = engine.execute(memberLoanQuery).fetchone()

    if not bool(bookInfo) or not bool(memInfo):
        raise Exception("Reservation does not exist")
    else:
        return (bookInfo[0], bookInfo[1], memInfo[0], memInfo[1], cancelDate)

#############################################################################################################################################################################

### Update Functions
def checkMemForUpdate(membershipId):
    ## Checks if a member exists before we update them
    
    checkMem = 'SELECT memberName FROM Member WHERE membershipId="{0}"'.format(membershipId)
    result = engine.execute(checkMem).fetchone()
    if not bool(result):
        raise Exception("Member does not exist");

def checkMemForUpdate(membershipId):
    ## Checks if a member exists before we update them
    
    checkMem = 'SELECT memberName FROM Member WHERE membershipId="{0}"'.format(membershipId)
    result = engine.execute(checkMem).fetchone()
    if not bool(result):
        raise Exception("Member does not exist");

def updateMember(membershipId, memName, memFac, memPhone, memEmail):
    updateMem = 'UPDATE Member SET memberName="{1}", memberFac="{2}", memberPhone="{3}", memberEmail="{4}" WHERE membershipId="{0}"'.format(membershipId,
                                                                                                                                            memName,
                                                                                                                                            memFac,
                                                                                                                                            memPhone,
                                                                                                                                            memEmail)
    engine.execute(updateMem)

def confirmUpdate(membershipId, memName, memFac, memPhone, memEmail):
    if memName == "" or memFac == "" or memPhone == "" or memEmail == "":
        raise Exception("Missing or incomplete fields");
    ## Return Update Confirmation Page
    return (membershipId, memName, memFac, memPhone, memEmail);
#############################################################################################################################################################################
### Creation Functions
def createMember(membershipId, memName, memFac, memPhone, memEmail):
    if memName == "" or memFac == "" or memPhone == "" or memEmail == "":
        raise Exception("Missing or incomplete fields");
    try:
        createMem = 'INSERT INTO member VALUES ("{0}","{1}", "{2}", "{3}", "{4}", 0)'.format(membershipId,
                                                                                            memName,
                                                                                            memFac,
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
        raise Exception("Creation Error")
def createBkAuthor(accessionNum, author):
    createAuthor = 'INSERT INTO BookAuthor VALUES("{0}", "{1}")'.format(accessionNum,
                                                                        author)

    engine.execute(createAuthor)

#############################################################################################################################################################################

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

def checkReservationToBeDeleted(membershipId, accessionNum):
    queryReservation = 'SELECT EXISTS(SELECT * FROM Reservation where accessionNum="{0}" and membershipId="{1}");'.format(accessionNum,
                                                                                                                          membershipId)
    # Check for existence reservation between accessionNum and membershipId exists
    return engine.execute(queryReservation).fetchone()[0]

def checkNextReservation(accessionNum):
    queryReservation = 'SELECT membershipId FROM Reservation where accessionNum="{0}"'.format(accessionNum);
    haveRes = engine.execute(queryReservation).fetchone();

    if bool(haveRes):
        return haveRes[0]
    else:
        return False

def checkDueDate(accessionNum): # Book for due date, Reservation for Reservation Date
    # Returns Loan Date of item
    queryDate = 'SELECT dueDate FROM Book WHERE accessionNum = "{0}"'.format(accessionNum)
    # Check Resevation
    return engine.execute(queryDate).fetchone()[0];

def checkIfBookOnLoan(accessionNum):
    queryLoan = 'SELECT membershipId FROM Book where accessionNum="{0}"'.format(accessionNum)
    haveLoan = engine.execute(queryLoan).fetchone()[0]
    
    # If bool(haveLoan) is true, book is on already on loan
    return bool(haveLoan)

#############################################################################################################################################################################

### Report Functions
def bookSearchReport(word, category):
    if category == 'Author':
        queryBookInfo = 'SELECT b.accessionNum, title, ISBN, publisher, pubYear FROM Book b INNER JOIN BookAuthor bA ON b.accessionNum = bA.accessionNum WHERE bA.authorName LIKE "%%{0}%%";'.format(word)

        bookInfoList = engine.execute(queryBookInfo).fetchall()

        for index in range(len(bookInfoList)):
            acNum = bookInfoList[index][0];
            queryAuthors = "SELECT GROUP_CONCAT(authorName, ' ') FROM BookAuthor WHERE accessionNum='{0}'".format(acNum);
            authors = engine.execute(queryAuthors).fetchone()[0]
            
            bookInfoList[index] = bookInfoList[index][0:2] + (authors,) + bookInfoList[index][2:]

        return bookInfoList;

    else:
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
    loanReportQ = 'SELECT accessionNum, title, ISBN, publisher, pubYear FROM Book where membershipId != " ";'
 
    bookInfoList = engine.execute(loanReportQ).fetchall()
    
    for index in range(len(bookInfoList)):
        acNum = bookInfoList[index][0];
        queryAuthors = "SELECT GROUP_CONCAT(authorName, ' ') FROM BookAuthor WHERE accessionNum='{0}'".format(acNum);
        authors = engine.execute(queryAuthors).fetchone()[0]
        
        bookInfoList[index] = bookInfoList[index][0:2] + (authors,) + bookInfoList[index][2:]
        
    return bookInfoList;

def reservationReport():
    ## Returns reservations report
    resReport = 'SELECT b.accessionNum, title, m.membershipId, memberName FROM Reservation r, Book b, Member m WHERE r.accessionNum = b.accessionNum AND r.membershipId=m.membershipId'
    return engine.execute(resReport).fetchall()

def outsFineReport():
    # Returns members with outstanding fines report
    queryFineReport = 'SELECT membershipId,memberName,memberFac,memberPhone,memberEmail FROM Member WHERE currFine > 0'
    return engine.execute(queryFineReport).fetchall()[0]

def booksLoanedToMemReport(membershipId):
    queryBookInfo = "SELECT accessionNum, title, ISBN, publisher, pubYear FROM Book WHERE membershipId = '{0}'".format(membershipId)
    bookInfoList = engine.execute(queryBookInfo).fetchall()
    for index in range(len(bookInfoList)):
        acNum = bookInfoList[index][0];
        queryAuthors = "SELECT GROUP_CONCAT(authorName, ' ') FROM BookAuthor WHERE accessionNum='{0}'".format(acNum);
        authors = engine.execute(queryAuthors).fetchone()[0]
        
        bookInfoList[index] = bookInfoList[index][0:2] + (authors,) + bookInfoList[index][2:]

    return bookInfoList;
#############################################################################################################################################################################

### Helper Functions
def dateDiff(endDate, startDate):
    queryDate = 'SELECT DATEDIFF("{0}", "{1}")'.format(endDate, startDate)
    daysDiff = engine.execute(queryDate).fetchone()[0]
    if daysDiff > 0 or daysDiff <= -14:
        return daysDiff
    return 0

#############################################################################################################################################################################

### TEST INPUT

# print(booksLoanedToMemReport("A103A"))
# print(confirmCancel("A103A", "A02", "2022/10/03"))

# id1 = "A101A"
# n1 = "Hermione Granger"
# f1 = "Science"
# p1 = "33336663"
# e1 = "flying@als.edu"

# id2 = "A102A"
# n2 = "Ronald Ranger"
# f2 = "BZA"
# p2 = "12336663"
# e2 = "bobo@als.edu"

# id3 = "A103A"
# n3 = "Hairy Granger"
# f3 = "Com"
# p3 = "35234895"
# e3 = "wand@als.edu"

# an1 = "A01"
# t1 = "Animal Farm"
# au1a = "George Orwell"
# au1b = "Sim Lim Square"
# i1 = "9790000000001"
# pub1 = "Intra S.r.l.s."
# py1 = "2021"

# an2 = "A02"
# t2 = "Human Farm"
# au2a = "George Bush"
# au2b = "Jim Simp Square"
# i2 = "9790000000002"
# pub2 = "EPH"
# py2 = "2015"

# an3 = "A03"
# t3 = "Human Zoo"
# au3a = "Big Bush"
# au3b = "Kim Pimp Square"
# i3 = "9790000000003"
# pub3 = "Pearson"
# py3 = "2008"
# createMember(id1, n1, f1, p1, e1)
# createMember(id2, n2, f2, p2, e2)
# createMember(id3, n3, f3, p3, e3)

# deleteMember(id3)


# createBook(an1, t1, i1, pub1,py1)
# createBkAuthor(an1, au1a)
# createBkAuthor(an1, au1b)
# createBook(an2, t2, i2, pub2, py2)
# createBkAuthor(an2, au2a)
# createBkAuthor(an2, au2b)
# createBook(an3, t3, i3, pub3, py3)
# createBkAuthor(an3, au3a)
# createBkAuthor(an3, au3b)


# updateMember(id1, n1, f1, p1, e3)


# reserveBook(id3, an3, "2022/03/03")
# reserveBook(id3, an2, "2022/03/03")

# print(loanBook(id2, an2, "2022/03/09"))
# ##

# withdrawBook(an1)

