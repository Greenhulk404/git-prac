class movie :
		
		def  __init__ (self, name, language, genre):
			self.name = name
			self.language = language
			self.genre = genre
			
		def display(self):
			print(self.name, self.language , self.genre)

			
		
movie1 =movie("tourist family",  "tamil" , "feel good")
movie2 =movie ("alpuzzha gymkhana", "malyalam", "sports, comedy")

movie3 = movie("kudumbasthan", "tamil", "comedy, emotion")


print("hello welcome to movie recommendations")

name = input("please enter you name  ")
name = name.lower()

if name == "sailaja":
	print("yo sweet sister , ping me in whatsapp")
elif name == "deekshith":
	print("bava garruuuuuuuuu")
	movie1.display() , movie2.display(), movie3.display()
	
else :
	movie1.display(), movie2.display(), movie3.display()
	
	

