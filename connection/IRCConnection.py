import socket
import random
import time

class IRCConnection():
	def __init__(self,name):
		self.network='irc.freenode.org'
		self.port=6667
		self.name=name
		self.nickname='tVirus'+str(int(random.random()*1000))+'_'+str(int(time.time()))
	def connect(self):
		#connecting to irc server
		self.irc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.irc.connect((self.network,self.port))
		print self.nickname
		self.irc.send('NICK '+self.nickname+'\r\n') #nickname is set as tVirus
		self.irc.send('USER PyIRC PyIRC PyIRC :Python IRC\r\n')
		
		#waiting until irc server is ready
		while True:
			data=self.irc.recv(4096)
			if data.lower().find('end of /motd')!=-1: #then we understand that irc server is ready
				break

	def sendMessage(self,msg): #send message to the user
		self.irc.send('PRIVMSG '+self.name+' :'+msg+'\r\n') 
	def close(self):
		self.irc.send('QUIT\r\n')
		self.irc.close()

if __name__=="__main__":
	irc=IRCConnection('sourgelin')
	irc.connect()
	irc.sendMessage('hello man!<br>how are you!')
	irc.close()