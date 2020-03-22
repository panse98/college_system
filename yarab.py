class course():
 def __init__(self,name,mark,total,place):
     self.name=name
     self.mark=mark
#class filesystem():
 #   def __init__(self,f):
  #      f=open("textfile.txt",r)



class admin():
 def __init__(self, password):
    self.password=password
 @staticmethod
 def loginadmin(password):
     if password == "0000":
         return 1
     else:
         return 0

 def addcourse(self,course_name):
        #self.course_name=course_name
        courses=['CO','Control','Data comm','Software',course_name]
          #define list
        with open('coursefile.txt','w')as f:
            f.writelines("%s\n" %course for course in courses)



course1 = admin(0000)
course1.addcourse('panse')