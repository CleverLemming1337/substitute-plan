import database
import http.server
import socketserver
import json

PORT = 8000
connection = database.newConnection()
cursor = database.newCursor(connection)
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET_subst(self, path):
        print("class", path)
        if path[0] == "class":
            try:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                dbresponse = database.getByClass(cursor, path[1])
                self.wfile.write(bytes(json.dumps(dbresponse), "ascii"))
                print(bytes(json.dumps(dbresponse), "ascii"))
                
            except Exception as err:
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(err.__class__.__name__, "ascii"))
                self.send_response(400)
    def do_GET(self):
        path = self.path.strip("/").split("/")
        print(path)
        if path[0] == "subst":
            try:
                self.do_GET_subst(path[1:])
            except IndexError:
                self.send_response(400)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            #self.wfile.write(b"")

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()