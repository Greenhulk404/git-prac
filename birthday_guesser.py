name = input("please enter your name ")
print("welcome to the guessing game ")
noof_days = int(input("no of days in your birthday month , if you born in feb please feel free to tell 28 , leap years are sleep years   "))
print("")
print("ok thanks for info , uff all people should born in feb then i will work peacefully")
print ("")
print("no of days not at all useful i wasted my time")
print("")
sum = int(input(" can you please tell the sum of days in your bday month and your bday date  eg: if your bday is july 14th,  31+ 14 = 45   "))

print("   ")

bday_date = sum - noof_days

halfdata = int(input("can you please tell sum of your bday month and no of days in month eg: if your bday is july 14th ,   7 + 31 = 38  "))

print("   ")

char_month = int(input("one final question how many characters in your bday month spelling,  eg if your bday is july 14th , july = 4    "))

print("  ")


if halfdata <= 36 :
	if noof_days == 28 :
		print ("bday date  :  ", bday_date , ", month : feb")
	elif noof_days == 30 :
		if char_month == 5:
			print("bday date : ", bday_date , ", month : april")
		elif char_month == 4:
			print ("bday date : ", bday_date , ", month : june")
		else :
			print("check your bday month spelling and restart")
	elif noof_days == 31 :
		if char_month == 7 :
			print ("bday date : " , bday_date , ", month : january")
		elif char_month == 5 :
			print ("bday date :  " , bday_date, ", month :  march" )
		elif char_month == 3 :
			print ("bday date : " , bday_date , ", month : may")
		else :
			print ("check your bday month spelling and restart")
	else :
		print ("please choose only 31 or 30 or 28 days and restart game")
elif halfdata >= 37 :
		if noof_days == 30:
			if char_month == 8 :
				print("bday date :  ", bday_date , ", month : november")
			elif char_month == 9 :
				print ("bday date :  " ,bday_date , ", month : september")
			else :
				print ("check your bday month spelling and restart")
		elif noof_days == 31:
				if char_month == 4:
					print("bday date  :" , bday_date , ", month =  july")
				elif char_month == 6 :
					print("bday date  :", bday_date , ", month =  august" )
				elif char_month == 7 :
					print("bday date : " , bday_date , " , month = ocotober ")
				elif char_month == 8 :
					print ("bday date : " , bday_date , ", month = december" )
				else :
					print("check your bday month spelling and restart")
		else :
				print( "please choose 30 or 31 days correctly and restart game")
else :
				print("please add bday month with no of days in month correctly")
				
				
				
				
					
				
		