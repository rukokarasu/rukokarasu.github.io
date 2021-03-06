# Basic python server. Probably neither secure nor standard-conforming, and
# definitely not DRY.
# 
# Need fortune, cowsay, and bleach installed.
# You also need a directory with pokemon sprites.

from http.server import BaseHTTPRequestHandler, HTTPServer
from subprocess import run, PIPE
from random import randint
from urllib.parse import parse_qs
import bleach

hostName = ''
hostPort = 80

class MyServer(BaseHTTPRequestHandler):
    def _set_headers_html(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def _set_headers_png(self):
        self.send_response(200)
        self.send_header('Content-type', 'image/png')
        self.end_headers()

    def do_POST(self):
        if self.path == '/msg':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            unsafemessage = parse_qs(post_data.decode('utf-8'))['message'][0]
            safemessage = bleach.clean(unsafemessage)
            with open('content', 'a') as f:
                 f.write('<p>' + safemessage + '</p>' + '\n')
            self.do_GET()

    def do_GET(self):
        print(self.path)
        if self.path == '/favicon.ico':
            self._set_headers_png()
            with open ('favicon.ico', 'rb') as img:
                self.wfile.write(img.read())

        # /msg lets you post messages to the server and displays them
        # Input is hopefully sanitized by bleach
        if self.path == '/msg':
            self._set_headers_html()
            with open('content', 'r') as f:
                self.wfile.write(bytes(f.read(), 'utf-8'))
            self.wfile.write(bytes('<form action="/msg" method="post">', 'utf-8'))
            self.wfile.write(bytes('  <textarea rows="4" cols="50" name="message"></textarea>', 'utf-8'))
            self.wfile.write(bytes('  <button type="submit">post</button>', 'utf-8'))
            self.wfile.write(bytes('</form>', 'utf-8'))

        # /pokemon displays a random pokemon sprite
        elif self.path == '/pokemon':
            index = randint(1, 251)
            with open('pokemon/main-sprites/crystal/' + str(index) + '.png', 'rb') as i:
                self.send_response(200)
                self.send_header('Content-type', 'image/png')
                self.wfile.write(i.read())
                return
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.wfile.write(bytes('pokemon machine broke', 'utf-8'))

        # any other page is just fortune | cowsay
        else:
            self._set_headers_html()
            s = run('fortune | cowsay', shell = True, stdout=PIPE).stdout.decode('utf-8')
            self.send_response(200)
            self.wfile.write(bytes('<pre>' + s + '</pre>', 'utf-8'))

    def do_HEAD(self):
        self._set_headers()

myServer = HTTPServer((hostName, hostPort), MyServer)
print('start')

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print('done')
