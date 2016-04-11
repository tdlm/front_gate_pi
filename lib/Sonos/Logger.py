from Sonos import Sonos

class Logger(Sonos):
	def say(self, room, str, lang = 'en-us'):
		print "Say :: Room: %s, Str: %s, Lang: %s" % (room, str, lang)

	def sayAll(self, str, lang = 'en-us'):
		print "SayAll :: Str: %s, Lang: %s" % (str, lang)

