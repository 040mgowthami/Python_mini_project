score=0
answer=input("1.what is the capital if india:")
if answer.lower()=="dehli":
  score+=1
answer=input("2.how many days are in a week:")
if answer=="7":
  score+=1
answer=input("3.5+5")
if answer=="10":
  score+=1
print("your score:",score,"/3")
