class application:
	def __init__(self, environ, start_response):
		self.environ = environ
		self.start = start_response


	urls = [
			("/","Index"), 
			("/hello", "Hello")
		]


	def __iter__(self):
		path = self.environ['PATH_INFO']

		if path == "/":
			return self.Get_Index()
		
		elif path == "/hello":
			return self.Get_Hello()
		
		else:
			return self.notFound()


	def Get_Index(self):
		status = '200 OK'
		response_headers = [('Content-Type','text/plain')]
		self.start(status, response_headers)
		
		yield "Welcome!\n"

	def Get_Hello(self):
		status = '200 OK'
		response_headers = [('Content-Type','text/plain')]
		self.start(status, response_headers)
		
		yield "Hello  World!\n"


	def notFound(self):
		status = '404 Not Found'
		response_headers = [('Content-Type','text/plain')]
		self.start(status, response_headers)
		
		yield "Page not found!\n"


