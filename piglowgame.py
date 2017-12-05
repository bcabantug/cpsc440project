from piglow import PiGlow
from time import sleep
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import random
import urlparse

PORT_NUMBER = 80

piglow = PiGlow()

val = 0
count = 1

gameCont = True;

colorList = ['red', 'orange','yellow','green','blue','white']

numberOrder = []

levelCount = 0


class myHandler(BaseHTTPRequestHandler):
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
            if "inputString" in qs:
                inText = qs['inputString'][0]
            
                self.send_response(200)
                self.send_header('Content-type',"application/json")
                self.end_headers()
		self.wfile.write('"true"')
		
		print inText
	    return
	try:
		    #Check the file extension required and
			#set the right mime type

	    sendReply = False
	    if self.path.endswith(".html"):
		mimetype='text/html'
		sendReply = True
	    if self.path.endswith(".png"):
		mimetype='image/png'
		sendReply = True
	    if self.path.endswith(".woff"):
		mimetype='application/x-font-woff'
		sendReply = True
           	if self.path.endswith(".woff2"):
                    mimetype='application/font-woff2'
    		sendReply = True
    	    if self.path.endswith(".ttf"):
		mimetype='application/octet-stream'
	    	sendReply = True
	    if self.path.endswith(".js"):
		mimetype='application/javascript'
	    	sendReply = True
	    if self.path.endswith(".css"):
		mimetype='text/css'
		sendReply = True

            if sendReply == True:
		#Open the static file requested and send it
		f = open(curdir + sep + self.path) 
		self.send_response(200)
	    	self.send_header('Content-type',mimetype)
    		self.end_headers()
    		self.wfile.write(f.read())
    		f.close()
	    return

	except IOError:
	    self.send_error(404,'File Not Found: %s' % self.path)
try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started piglowweb server on port ' , PORT_NUMBER
    #Wait forever for incoming http requests
    #server.serve_forever()
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
        
        #test to see if it will process one request
        
        
        
        server.serve_forever()
        
        
        userAnswer = raw_input("Please enter the order of colors(with underscore separation):")
        
        print "you entered ",userAnswer
        
        
    
        #list(map(int,userAnswer))
    
        listAnswer = map(int, userAnswer.split('_'))
        #for i in userAnswer:
        #    print i
    
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
    
except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
    piglow.all(0)
    

    
