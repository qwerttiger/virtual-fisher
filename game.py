import random
fish=int(open("save.txt").read().split()[0])
leastfish=int(open("save.txt").read().split()[1])
upgrades1=int(open("save.txt").read().split()[2])
def process(command):
  global fish,leastfish,upgrades1
  if command=="save":
    open("save.txt","w").write(str(fish)+"\n"+str(leastfish)+"\n"+str(upgrades1))
    print("saved")
  if command=="fish":
    x=random.randint(round(leastfish),round(leastfish*3))
    fish+=x
    print("You got "+str(x)+" fish")
  if command=="inventory":
    print(f"You have {fish} fish")
  if command=="upgrades":
    print(f"More Fish: bought {upgrades1} times price: {100*round(upgrades1**1.5)}")
  if command=="buy more fish" and fish>=100*round(upgrades1**1.5):
    upgrades1+=1
    leastfish*=1.1
    fish-=100*round(upgrades1**1.5)
while True:
  process(input("input: "))
