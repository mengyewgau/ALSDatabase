CREATE TABLE Member(  
     membershipId	VARCHAR(25)    NOT NULL,
     name			VARCHAR(25)   NOT NULL,
     memberFac        VARCHAR(25)   NOT NULL,
     memberEmail    VARCHAR(25)	NOT NULL,
     memberPhone VARCHAR(8) NOT NULL,
	 PRIMARY KEY (membershipId)); 
CREATE TABLE Book( 
     ISBN    VARCHAR(25)    NOT NULL,
     bookTitle    VARCHAR(4)    NOT NULL,
	 publisher     VARCHAR(5)    NOT NULL,
     pubYear  YEAR,
     PRIMARY KEY (ISBN));
CREATE TABLE BookCopy(
     accessionNum    VARCHAR(25)    NOT NULL,
     ISBN       VARCHAR(25)	NOT NULL,
     PRIMARY KEY (accessionNum),
     FOREIGN KEY (ISBN) REFERENCES Book(ISBN));
CREATE TABLE Fine( 
     membershipId     VARCHAR(5)    NOT NULL,
     paidDate       DATE NOT NULL,
     paidAmt       DECIMAL(2) NOT NULL,
     PRIMARY KEY (membershipId, paidDate, paidAmt),
     FOREIGN KEY (membershipId) REFERENCES Member(membershipId)); 
CREATE TABLE Author(
     authorName     VARCHAR(25)    NOT NULL,
     authorId       VARCHAR(25) NOT NULL,
#     ISBN       VARCHAR(25),
	 PRIMARY KEY (authorId));
#     FOREIGN KEY (ISBN)    REFERENCES Book(ISBN));

CREATE TABLE BookAuthors(
	ISBN VARCHAR(25) NOT NULL,
    authorId VARCHAR(25) NOT NULL,
    primary key (ISBN, authorId),
    foreign key (ISBN) REFERENCES Book(ISBN),
    FOREIGN KEY (authorId) references Author(authorId));