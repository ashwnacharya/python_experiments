class application:
	def __init__(self, environ, start_response):
		self.environ = environ
		self.start = start_response


	urls = [
			("/","Index"), 
			("/hello", "Hello")
		]


	def __iter__(self):
		path_info = self.environ['PATH_INFO']
		method = self.environ['REQUEST_METHOD']
		
		for path, name in self.urls:
			if path.upper() == path_info.upper():
				funcName = method.upper() + "_" + name
				func = getattr(self, funcName)
				return func()

		return self.notFound()
		


	def GET_Index(self):
		status = '200 OK'
		response_headers = [('Content-Type','text/plain')]
		self.start(status, response_headers)
		
		yield "Welcome!\n"

	def GET_Hello(self):
		status = '200 OK'
		response_headers = [('Content-Type','text/plain')]
		self.start(status, response_headers)
		
		yield "Hello  World!\n"


	def notFound(self):
		status = '404 Not Found'
		response_headers = [('Content-Type','text/plain')]
		self.start(status, response_headers)
		
		yield "Page not found!\n"


