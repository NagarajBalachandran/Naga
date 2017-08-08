import random
Account_Balance=0
Customer_Given_Amount=0
Customer_Balance_Amount=0
Twenty_Five=0
Fifty=0
Seventy_Five=0 
Waiting_List=[]

num_Passangers = int(input("Please enter number of Passangers:"))
print ("you entered %s Passangers" %num_Passangers)
Passangers_info = {}
Passangers_data = ['Enter amount : ']
for i in range(0,num_Passangers):
  Passangers_name = input("Passanger Name :")
  Passangers_info[Passangers_name] = {}
  for entry in Passangers_data:
    Passangers_info[Passangers_name][entry] = int(input(entry)) #storing the marks entered as integers to perform arithmetic operations later on.
        #print Passanger_info
        #print(Passangers_info[Passangers_name][entry]) # amount entered value
    
for x in Passangers_info:
    #print (x)
      for y in Passangers_info[x]:
      #print(Passangers_info[x][y])
      #print (y,':',Passangers_info[x][y])   
        Customer_Given_Amount = Passangers_info[x][y] #int(input('Enter the amount:'))
      
      if Customer_Given_Amount%25 != 0 :
        print("Please enter the correct denomination")
      else:
        print("")
      if Customer_Given_Amount < 25 :
        print("Amount not enough to get the tickets")
      elif Customer_Given_Amount == 25 :
        Account_Balance=Account_Balance+25
        Twenty_Five=Twenty_Five+1
        print("Ticket Booked Successfully for %s.No Balance Amount "%x)
        Waiting_List.append(x)
      elif Customer_Given_Amount == 50 :
        if Twenty_Five>=1:
          Account_Balance=Account_Balance+25
          Twenty_Five=Twenty_Five-1
          Fifty=Fifty+1
          print("Ticket Booked Successfully for %s.25 Balance Amount"%x)
          Waiting_List.append(x)
        else:
          print("Ticket can't book for %s. because no twenty five denomination available now"%x)
          
          
      elif Customer_Given_Amount == 75 :
       if Fifty>=1:
        Account_Balance=Account_Balance+25
        Fifty=Fifty-1
        Seventy_Five=Seventy_Five+1
        print("Ticket Booked Successfully for %s.50 Balance Amount"%x)
        Waiting_List.append(x)
       else:
        print("Ticket can't book for %s. because no Fifty denomination available now"%x)
        



for y in Waiting_List:
  del Passangers_info[y]
  

del Waiting_List[:]  
for x in Passangers_info:
    #print (x)
      for y in Passangers_info[x]:
      #print(Passangers_info[x][y])
      #print (y,':',Passangers_info[x][y])   
        Customer_Given_Amount = Passangers_info[x][y] #int(input('Enter the amount:'))
      
      if Customer_Given_Amount%25 != 0 :
        print("Please enter the correct denomination")
      else:
        print("")
      if Customer_Given_Amount < 25 :
        print("Amount not enough to get the tickets")
      elif Customer_Given_Amount == 25 :
        Account_Balance=Account_Balance+25
        Twenty_Five=Twenty_Five+1
        print("Ticket Booked Successfully for %s.No Balance Amount "%x)
       
      elif Customer_Given_Amount == 50 :
        if Twenty_Five>=1:
          Account_Balance=Account_Balance+25
          Twenty_Five=Twenty_Five-1
          Fifty=Fifty+1
          print("Ticket Booked Successfully for %s.25 Balance Amount"%x)
         
        else:
          #print("Ticket can't book for %s. because no twenty five denomination available now"%x)
          Waiting_List.append(x)
          
      elif Customer_Given_Amount == 75 :
       if Fifty>=1:
        Account_Balance=Account_Balance+25
        Fifty=Fifty-1
        Seventy_Five=Seventy_Five+1
        print("Ticket Booked Successfully for %s.50 Balance Amount"%x)
      
       else:
        #print("Ticket can't book for %s. because no Fifty denomination available now"%x)
        Waiting_List.append(x)
        

i=1
for z in Waiting_List:
  print("%s is waiting list %s" %(z,i ))
  i=i+1

print ("Total Account Balance %s " %Account_Balance)  
print ("Total Twenty Five notes count %s " %Twenty_Five)
print ("Total Fifty notes count %s " %Fifty)
print ("Total Seventy_Five notes count %s " %Seventy_Five)