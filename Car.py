class car:

   wheels = 4 #class varible

   def __init__(self,make,model,year,color):#contructor
       self.make = make  #instance variable
       self.model = model #instance variable
       self.year = year #instance variable
       self.color = color  #instance variable

   # self = the object that is using this method
   def drive(self):
       print("This "+self.model+" is driving")

   def stop(self):
       print("This "+self.model+" is stopped")

