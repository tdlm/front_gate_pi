class Sonos:
        apiPort = 5005
        apiHost = '127.0.0.1'

        def say(self, room, str, lang = 'en-us'):
                path = 'http://{host}:{port}/{room}/say/{str}/{lang}/{volume}'.format(
									host = self.apiHost,
									port = self.apiPort,
									room = urllib2.quote(room),
									str = urllib2.quote(str),
									lang = lang,
									volume = 50
								)
                self.__sonosRequest(path)

        def sayAll(self, str, lang = 'en-us'):
                path = 'http://{host}:{port}/sayall/{str}/{lang}/{volume}'.format(
									host = self.apiHost,
									port = self.apiPort,
									str = urllib2.quote(str),
									lang = lang,
									volume = 50
								)
                self.__sonosRequest(path)

        def __sonosRequest(self, url):
                req = urllib2.Request(url)
                try:
                        urllib2.urlopen(req)
                except urllib2.URLError as e:
                        print e.reason
