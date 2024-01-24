import database
import http.server
import socketserver
import json

PORT = 8001
connection = database.newConnection()
cursor = database.newCursor(connection)
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET_subst(self, path):
        print(path)
        if len(path) == 0:
            self.send_header("Content-type", "application/json")
            self.end_headers()
            dbresponse = database.getAll(cursor)
            self.wfile.write(bytes(json.dumps(dbresponse), "utf-8"))
            self.send_response(200)
        
        elif path[0] == "class":
            try:
                if len(path) < 2:
                    self.send_error(400)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                dbresponse = database.getByClass(cursor, path[1])
                self.wfile.write(bytes(json.dumps(dbresponse), "utf-8"))
                self.send_response(200)
                
            except Exception as err:
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(err.__class__.__name__, "utf-8"))
                self.send_error(400)
        elif path[0] == "teacher":
            try:
                if len(path) < 2:
                    self.send_error(400)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                dbresponse = database.getByTeacher(cursor, path[1])
                self.wfile.write(bytes(json.dumps(dbresponse), "utf-8"))
                self.send_response(200)

            except Exception as err:
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(err.__class__.__name__, "utf-8"))
                self.send_error(400)
            
        
    def do_GET(self):
        path = self.path.strip("/").split("/")
        print(path)
        if path[0] == "subst":
            try:
                self.do_GET_subst(path[1:])
            except IndexError:
                self.send_error(400)
        else:
            self.send_error(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            #self.wfile.write(b"")

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()