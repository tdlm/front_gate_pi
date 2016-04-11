#!/usr/bin/python
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

import urllib2
from time import sleep
from SkyBell import SkyBell
from Sonos import Sonos
from Sonos import Logger as SonosLogger
from FrontGateState import FrontGateState

class FrontGateManager:
	sonos = Sonos()

	def init(self, output = 'sonos'):
		
		if output == 'mute':
			sonos = SonosLogger()

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
	frontGateManager.init(sys.argv[1])

