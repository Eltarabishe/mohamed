class parent():
    def __init__ (self,last_name,eye_color):
        print("parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print ("Last Name - " +self.last_name)
        print ("Eye Color - "+self.eye_color)

class Child(parent):
    def __init__ (self,last_name,eye_color,number_of_toys):
        print ("Child Constructor Called")
        parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys
    def show_info(self):
        print ("Last Name - " +self.last_name)
        print ("Eye Color - "+self.eye_color)
        print ("number of toys - "+ str(self.number_of_toys))

billt_cyrus = parent("Cyrus","blue")
#print (billt_cyrus.last_name)
#billt_cyrus.show_info()
miley_cyrus = Child("Cyrus","Blue",5)
miley_cyrus.show_info()

#print(miley_cyrus.last_name)

#print(miley_cyrus.number_of_toys)