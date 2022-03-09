CREATE TABLE Member(  
     membershipId	VARCHAR(25)   	NOT NULL,
     memberName		VARCHAR(25)   	NOT NULL,
     memberFac      VARCHAR(25)   	NOT NULL,
     memberPhone    VARCHAR(8)	  	NOT NULL,
     memberEmail 	VARCHAR(25)		NOT NULL,
     currFine		INT 			NOT NULL,
	 PRIMARY KEY 	(membershipId)); 
CREATE TABLE Book( 
	accessionNum	VARCHAR(25) 	NOT NULL,
    title    		VARCHAR(25)		NOT NULL, #Authors will have to be referenced directly to BookAuthor
	ISBN			VARCHAR(25)		NOT NULL,
	publisher		VARCHAR(25)		NOT NULL,
	pubYear  		YEAR			NOT NULL,
    date			DATE,
    membershipId	VARCHAR(25),
	PRIMARY KEY 	(accessionNum),
    FOREIGN KEY 	(membershipId) 
		REFERENCES Member(membershipId)
        ON DELETE RESTRICT); 
    
CREATE TABLE BookAuthor(
	accessionNum 	VARCHAR(25) 	NOT NULL,
    authorName		VARCHAR(50) 	NOT NULL,
    FOREIGN key 	(accessionNum) REFERENCES Book(accessionNum));
    
CREATE TABLE Payment( 
	membershipId	VARCHAR(25)		NOT NULL,
	paidDate 		DATE 			NOT NULL,
    paidAmt			INT 			NOT NULL,
    PRIMARY KEY 	(membershipId, paidDate, paidAmt),
    FOREIGN KEY 	(membershipId) REFERENCES Member(membershipId)); 
    
CREATE TABLE Reservation(
	accessionNum 	VARCHAR(25) 	NOT NULL,
    membershipId	VARCHAR(50) 	NOT NULL,
    date	 		DATE			NOT NULL,
    PRIMARY KEY 	(accessionNum, membershipId),
    FOREIGN key 	(accessionNum) 
		REFERENCES 	Book(accessionNum)
        ON DELETE RESTRICT,
    FOREIGN key 	(membershipId) 
		REFERENCES 	Member(membershipId)
        ON DELETE CASCADE);