import random
fish=int(open("save.txt").read())
def process(command):
  global fish
  if command=="save":
    open("save.txt","w").write(str(fish))
    print("saved")
  if command=="fish":
    x=random.randint(1,5)
    fish+=x
    print("You got "+str(x)+" fish")
while True:
  process(input("input: "))
