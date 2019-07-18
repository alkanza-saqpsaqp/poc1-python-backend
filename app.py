#!/usr/bin/python

from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080

landing_page = """
<!doctype html>
<html lang=en>
<head>
<meta charset=utf-8>
<title>Alkanza</title>
</head>
<body>
<h1>Título</h1>
<h3>branch002</h3>
</body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    """Handler for GET requests"""
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    content = landing_page.encode('utf-8')
    self.wfile.write(content)

try:
  server = HTTPServer(('', PORT_NUMBER), MyHandler)
  print('Started httpserver on port', PORT_NUMBER)
  server.serve_forever()

except KeyboardInterrupt:
  server.server_close()
  print('Stopping server')
