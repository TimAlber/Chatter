import threading
import webbrowser
import BaseHTTPServer
import SimpleHTTPServer
import json

FILE = 'stimmen.html'
PORT = 2222


class TestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """The test example handler."""

    def do_POST(self):
	print str(self.path)
        """Handle a post request by returning the square of the number."""
        length = int(self.headers.getheader('content-length'))
        data_string = self.rfile.read(length)
	result = json.loads(data_string)
	print result
	#userlen = int(self.headers.getheader('content-length'))
        #user = self.rfile.read(userlen)
	#print 'User:'+user

	#user = 'TimtheAdmin'
	with open("stimmentext.txt", "a+") as sm:
    	   sm.write(str(result[0])+' :: '+str(result[1])+'\n')
	#sm.close

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, TestHandler)
    server.serve_forever()

try:
        #Create a web server and define the handler to manage the
        #incoming request
        print 'Sarting Server on port: ',PORT
	start_server()
        #print 'Started httpserver on port ' , PORT_NUMBER

        #Wait forever for incoming htto requests

except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
