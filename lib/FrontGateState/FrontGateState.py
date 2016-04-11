import RPi.GPIO as GPIO

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
				self.play_random_sound()
				self.push("The gate is now open")
			else:
				FrontGateManager.sonos.sayAll('The gate is now closed')
				self.push("The gate is now closed")
			self.lastState = self.open

	def play_random_sound(self):
		sounds = [
			'./sounds/mp3/whittier.mp3',
			'./sounds/mp3/arpeggio.mp3',
			'./sounds/mp3/st_michaels.mp3',
			'./sounds/mp3/beethovens_fifth.mp3'
		]
		
		import random
		import os

		sound = random.choice(sounds)
		os.system('mpg123 {sound}'.format(sound = sound))
		
        def push(self, message):
                os.system('prowl "Front Gate Pi" "2" "Gate Open/Close" "{message}"'.format(message = message))
