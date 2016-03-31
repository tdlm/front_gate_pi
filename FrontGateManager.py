#!/usr/bin/python

import urllib2
import RPi.GPIO as GPIO
from time import sleep

class Sonos:
        apiPort = 5005
        apiHost = '127.0.0.1'

        def say(self, room, str, lang = 'en-us'):
                path = 'http://{host}:{port}/{room}/say/{str}/{lang}'.format(
									host = self.apiHost,
									port = self.apiPort,
									room = urllib2.quote(room),
									str = urllib2.quote(str),
									lang = lang
								)
		print path
                self.__sonosRequest(path)

        def sayAll(self, str, lang = 'en-us'):
                path = 'http://{host}:{port}/sayall/{str}/{lang}'.format(
									host = self.apiHost,
									port = self.apiPort,
									str = urllib2.quote(str),
									lang = lang
								)
		print path
                self.__sonosRequest(path)

        def __sonosRequest(self, url):
                req = urllib2.Request(url)
                try:
                        urllib2.urlopen(req)
                except urllib2.URLError as e:
                        print e.reason


class FrontGateState:
	open = False
	lastState = False

	def __init__(self, pin):
		self.pin = pin
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	def run(self):
		if GPIO.input(self.pin):
			self.open = False 
		else:
			self.open = True 

		if self.open != self.lastState:
			if self.open:
				FrontGateManager.sonos.sayAll('The gate is now open')
			else:
				FrontGateManager.sonos.sayAll('The gate is now closed')
			self.lastState = self.open

class SkyBell:
	pressed = False
	lastState = False

	def __init__(self, pin):
		self.pin = pin
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	def run(self):
		if GPIO.input(self.pin):
			self.pressed = False 
		else:
			self.pressed = True 
		
		if self.pressed != self.lastState:
			if self.pressed:
				FrontGateManager.sonos.sayAll('There is someone at the door')
		self.lastState = self.pressed

class FrontGateManager:
	sonos = Sonos()

	def init(self):
		self.frontGateState = FrontGateState(22)
		self.skyBell = SkyBell(17)

		try:
			while True:
				self.frontGateState.run()
				self.skyBell.run()
				sleep(0.5)
		finally:
			GPIO.cleanup()


if __name__ == "__main__":
	frontGateManager = FrontGateManager()
	frontGateManager.init()	
