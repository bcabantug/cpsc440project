from piglow import PiGlow
from time import sleep
import random

piglow = PiGlow()

val = 0
count = 1

gameCont = True;

colorList = ['red', 'orange','yellow','green','blue','white']

numberOrder = []

levelCount = 0


while gameCont == True:
    levelCount += 1
    print "PiGlow Memory Game"
    
    print "Follow the order of colors that appear and relay them back!"
    print "1 - red"
    print "2 - orange"
    print "3 - yellow"
    print "4 - green"
    print "5 - blue"
    print "6 - white"
    
    print "Current Level: %i" % (levelCount)
    
    print "Ready in "
    
    l = 5
    while l > 0:
        print l
        sleep(1)
        l-=1
    
    num = random.randint(1, 6)
    
    numberOrder.append(num)
    
    for i in numberOrder:
        
        if(i == 1):
            piglow.red(10)
            sleep(1)
            piglow.red(0)
            sleep(1)
        elif(i==2):
            piglow.orange(10)
            sleep(1)
            piglow.orange(0)
            sleep(1)
        elif(i==3):
            piglow.yellow(10)
            sleep(1)
            piglow.yellow(0)
            sleep(1)
        elif(i==4):
            piglow.green(10)
            sleep(1)
            piglow.green(0)
            sleep(1)
        elif(i==5):
            piglow.blue(10)
            sleep(1)
            piglow.blue(0)
            sleep(1)
        elif(i==6):
            piglow.white(10)
            sleep(1)
            piglow.white(0)
            sleep(1)
            
    userAnswer = raw_input("Please enter the order of colors(with spaces):")
    print "you entered ",userAnswer
    
    #list(map(int,userAnswer))
    
    listAnswer = map(int, userAnswer.split())
    #for i in userAnswer:
     #   print i
    
    print listAnswer
    print numberOrder
    
    for i in userAnswer:
        
        if(i == 1):
            piglow.red(10)
            sleep(2)
            piglow.red(0)
            sleep(1)
        elif(i==2):
            piglow.orange(10)
            sleep(2)
            piglow.orange(0)
            sleep(1)
        elif(i==3):
            piglow.yellow(10)
            sleep(2)
            piglow.yellow(0)
            sleep(1)
        elif(i==4):
            piglow.green(10)
            sleep(2)
            piglow.green(0)
            sleep(1)
        elif(i==5):
            piglow.blue(10)
            sleep(2)
            piglow.blue(0)
            sleep(1)
        elif(i==6):
            piglow.white(10)
            sleep(2)
            piglow.white(0)
            sleep(1) 
   
    
    if numberOrder != listAnswer:
        print "Sorry! Incorrect Pattern: Pattern was "
        
        for i in numberOrder:
            print i
        
        j = 0
        
        while j < 5:
            piglow.red(10)
            sleep(1)
            piglow.red(0)
            sleep(1)
            j+=1
        
        gameCont = False
        
    else:
        print "Congratulations! moving to next level..."
        print "Pattern was "
        
        for i in numberOrder:
            print i
            
        k = 0
        while k < 4:
            piglow.all(10)
            sleep(1)
            piglow.all(0)
            sleep(1)
            k+=1
        
if gameCont == False:
    print "Thanks for playing!"
    piglow.all(0)
    

#while True:
 #   leds = range(1, 19, +1)
  #  for led in leds:
   #     if count == 1:
    #        val = val +1
     #       if val > 90:
      #          count = 0
       # else:
        #    val = val - 1
         ##      count = 1
        #piglow.led(led, val)
        
        #sleep(0.0075)
def do_GET(self):
		#get address 
		parts = urlparse.urlparse(self.path)
		if parts.path=="/":
			self.path="/index.html"

		#append to URL
		if parts.query != "":
			qs = urlparse.parse_qs( parts.query )

		###################################
		#CHECK URL AND GET THE COLOR THEN APPEND TO A LIST
		###################################
		if "text" in qs:
			inText = qs['text'][0]
        
        
        
        
