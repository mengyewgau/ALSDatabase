## SQL for retrieval
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

### Format for Mem Creation ###

SELECT * FROM member;

## Creation (SETTLED)
## Duplicates in Creation (SETTLED)

## Deletion
DELETE FROM member WHERE membershipId="A101A";
# Cannot delete if members have loans, reservations, outstnadiong fines 

## Update

# Can only update details

## Acquire Books

# Book must not be duplicate, missing or incomplete

## Withdrawal

# Cannot withdraw on loan/reserved/does not exist

## Borrowing

# Cannot borrow books that are on loan until DD/MM/YYYY (calculate when we retrieve)
# Cannot borrow if quota exceeded (calculate when retrieve)
# Cannot borrow if outstanding fines 

## Returning

# If have fines, must flag member that he has fines (i.e. return popup)

## Reservation

# Cannot reserve if quota exceed (calc when retrieve)
# Cannot reserve if outstanding fines
# Cannot reserve if overlap with another member (overlap --> reserve
