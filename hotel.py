class Room:
   def __init__(self,number,status):
      self.number = number
      self.status = status

class Hotel:
   def __init__(self):
      self.rooms = []

   def add_room(self,room):
      self.rooms.append(room)

   def find_room(self,number):
      for room in self.rooms:
         if room.number == number:
            return room
      return None

   def check_in(self,number):
      room = self.find_room(number)
      if room is not None:
         room.status = "occupied"
         print(f"{room.number}th room is occupied! ")

      else:
         print("check_in is error")

   def check_out(self,number):
      room = self.find_room(number)     
      if room is not None:
          room.status = "vacant"
          print(f"{room.number}th room is vacant!")

      else:
         print("error")  


   def display_room(self):
      print("All our Rooms: ")   
      for room in self.rooms:
         print(f"{room.number}:{room.status}")

hotel = Hotel()
hotel.add_room(Room("101","vacant"))
hotel.add_room(Room("102","occupied"))
hotel.add_room(Room("103","vacant"))
hotel.add_room(Room("104","vacant"))
hotel.add_room(Room("105","occupied"))
hotel.add_room(Room("106","occupied"))
hotel.add_room(Room("107","vacant"))
hotel.add_room(Room("108","vacant"))
hotel.add_room(Room("109","occupied"))
hotel.add_room(Room("110","vacant"))
hotel.display_room()

while True:

   choice = input("We are pleasure to serve you.You should choice (1)check_in, (2)check_out, (3)common rooms ,(4)you exit the site.")
   if choice == '4':
      print("Good bye dear client")
      break
   
   if choice not in ['1','2','3']:
      print("You have writted incorrect info")
      continue
   number = input("Select a room")

   if choice == '1':
      hotel.check_in(number)
   elif choice == '2' :
      hotel.check_out(number)
   elif choice == '3':
      hotel.display_room()




            
