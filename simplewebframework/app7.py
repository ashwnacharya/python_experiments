import re

class wsgiapp:
	def __init__(self, environ, start_response):
		self.environ = environ
		self.start = start_response

	def __iter__(self):
		return self.delegate()

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
		status = '200 OK'
		response_headers = [('Content-Type','text/plain')]
		self.start(status, response_headers)
		
		yield "Welcome!\n"

	def GET_Hello(self, name):
		status = '200 OK'
		response_headers = [('Content-Type','text/plain')]
		self.start(status, response_headers)
		
		yield "Hello  %s!\n" %name


	def notFound(self):
		status = '404 Not Found'
		response_headers = [('Content-Type','text/plain')]
		self.start(status, response_headers)
		
		yield "Page not found!\n"


