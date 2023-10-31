import mysql .connector

remote = mysql .connector .connect (
   host = "192.168.56.101",
   port = "4567",
   user = "goym",
   password = "dudals017",
   database = "madang"
)

cur = remote .cursor ()

while True :
   command = input ("Enter Query (Ctrl+C to exit): ")
   
   try :
     cur .execute (command )
     result = cur .fetchall ()
     
     for row in result :
       print (row )

   except KeyboardInterrupt :
     print ("Exiting...")
     break

remote .close ()
