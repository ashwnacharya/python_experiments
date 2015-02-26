import re
import traceback

class wsgiapp:
	def __init__(self, environ, start_response):
		self.environ = environ
		self.start = start_response
		self.status = "200 OK"
		self._headers = []


	def header(self, name, value):
		self._headers.append((name, value))

	def __iter__(self):

		try:
			x = self.delegate()
			self.start(self.status, self._headers)

		except:
			headers = [("Content-Type","text/plain")]
			self.start("500 Internal Error", headers)
			x = "Internal error:\n\n" + traceback.format_exc()	
			
		if isinstance(x, str):
			return iter([x])
		else:
			return iter(x)


	def delegate(self):
		path= self.environ['PATH_INFO']
		method = self.environ['REQUEST_METHOD']
		
		for pattern, name in self.urls:
			m = re.match('^' + pattern + '$', path)
			if m:
				args = m.groups()
				funcName = method.upper() + "_" + name
				func = getattr(self, funcName)
				return func(*args)

		return self.notFound()
		

class application(wsgiapp):

	urls = [
			("/","Index"), 
			("/hello/(.*)", "Hello")
		]


	def GET_Index(self):
		
		self.header('Content-Type','text/plain')		
		return "Welcome!\n"

	def GET_Hello(self, name):
		self.header('Content-Type','text/plain')		
		yield "Hello  %s!\n" %name


	


