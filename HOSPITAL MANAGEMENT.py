
class hospital:
  def __init__(self,icu,ew,gw):
    self.icu=icu
    self.ew=ew
    self.gw=gw
  def check_bed_avail(self):
    print("These are the availabe beds")
    print("icu :",self.icu)
    print("emergency ward :",self.ew)
    print("general ward :",self.gw)
  
class patient:
  def __init__(self):
    print("Enter your name: ")
    self.name=input()
    print("Enter your age: ")
    self.age=input()
    print("Enter your sex: ")
    self.sex=input()
  def basic_details(self):
    print("Name : ",self.name,"\nAge : ",self.age,"\tSex : ",self.sex)
  def status(self):
    print("Enter the status of the patient as provided in options:")
    self.status=input()
  def stat_of_patient(self):
    print("Name : ",self.name,"\nAge : ",self.age,"\tSex : ",self.sex)
    print("Status of the patient : ",self.status)
    
class doctor:
  def wel_doctor(self):
    print("Hello Doctor")
bh=hospital(10,5,20)

while True:
  print("=====Welcome to Basha Hospitals=====")
  print("Please select from the option below")
  print("\n 1-Book an appointment ")
  option=int(input())
  if option==1:
    print("Please enter your Basic details")
    p=patient()
    print("Let us check the availability of doctor and get back to you")
    d=doctor()
    d.wel_doctor()
    print("Please consult the patient and provide us the necessary option")
    p.basic_details()
    bh.check_bed_avail()
    print("\n 1-icu \n 2-emergency ward \n 3-general ward")
    print("Enter the option")
    opt=int(input())
    if opt==1:
      bh.icu=bh.icu-1
      p.status()

      print("Patient admitted in icu")
    elif opt==2:
      bh.ew=bh.ew-1
      p.status()
      print("Patient admitted in emergency ward")
    elif opt==3:
      bh.gw=bh.gw-1
      p.status()
      print("Patient admitted in general ward")
    else:
      print("Please enter a valid option")
    print("Choose the option")
    print("\n 1-Show Status of the patient \n 2-Discharge the patient")
    op=int(input())
    if op==1:
      p.stat_of_patient()
    elif op==2:
      print("The patient has been discharged \nThank you")
      if p.status()=="icu":
        if bh.icu>10:
          bh.icu=bh.icu+1
        elif p.status()=="emergency ward":
          if bh.ew>5:
            bh.ew=bh.ew+1
        elif p.status()=="general ward":
          if bh.gw>20:
            bh.gw=bh.gw+1
      else:
       print("Enter Valid option")
    break
  else:
    print("Please enter a valid option")
  
