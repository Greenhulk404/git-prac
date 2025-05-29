import random
batting_score= 0
bowling_score = 0
def scoring(i):
	score = random.randint(0,6)
	return score
	
name = input("enter your name  ")
print(name , "welcome to the cricketing world")
print("are you ready for the toss")
toss = input("choose heads or tails  ")
if toss == "heads":
	print("you won the toss ")
	selected = input("choose bat or bowl  ")
	if selected == "bat":
		print("get ready to face our thunder bolts")
		for i in range (1,7):
			x = scoring(i)
			print("your scored",x, "runs in" , i,"ball")
			batting_score = batting_score + x
		print("your total score is",batting_score)
		print("now get ready for bowling")
		for i in range (1,7):
			y = scoring(i)
			print("you conceed", y , "runs in ", i , "ball")
			bowling_score = bowling_score + y
			if bowling_score > batting_score :
				break
		print("opponent total score is " , bowling_score)
		if batting_score > bowling_score:
			print ("you won the match by", batting_score - bowling_score , "runs")
		elif batting_score < bowling_score :
			print("opponet won the match")
		else :
			print ("match is tie")
	elif selected == "bowl" :
		print("get ready to face hard hitters")
		for i in range (1,7):
			x = scoring(i)
			print("you conceed", x  , "runs in", i , "ball")
			bowling_score = bowling_score + x
		print("opponent total score is", bowling_score)
		print("get ready to face our thunder boults")
		for i in range (1,7):
			y = scoring(i)
			print ("you scored", y , "runs in", i , "ball")
			batting_score = batting_score + y
			if batting_score > bowling_score :
				break
		print("your total score is" , batting_score)
		if batting_score > bowling_score :
			print("you won the match")
		elif batting_score < bowling_score :
			print("opponet won match by" , batting_score - bowling_score , "runs")
		else :
			print ("match got tied")
	else :
		print("please choose bat or bowl properly, restart the game")
elif toss == "tails":
	print("you lost toss , opponet elected to bowl")
	print("get ready to face our thunderbolts")
	for i in range (1,7):
		x = scoring(i)
		print("you scored" , x ," runs in " , i , "ball" )
		batting_score = batting_score + x
	print ("your total score is", batting_score , "runs")
	print("get ready to face hard hitters")
	for i in range (1,7):
		y = scoring(i)
		print ("you conceed" , y , "runs in", i , "ball")
		bowling_score = bowling_score + y
		if bowling_score > batting_score :
			break
	print ("opponent total score is", bowling_score)
	if batting_score > bowling_score :
		print("you won the match by", batting_score - bowling_score , "runs")
	elif batting_score < bowling_score :
		print ("opponent chased the target")
	else :
		print ("match got tied")
else :
	print("please heads or tails correctly, restart the game")