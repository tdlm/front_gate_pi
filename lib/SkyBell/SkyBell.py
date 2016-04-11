import RPi.GPIO as GPIO

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

	def push(self, message):
		os.system('prowl "Front Gate Pi" "2" "Gate Door Bell" "{message}"')
