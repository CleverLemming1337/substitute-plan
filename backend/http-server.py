import database
import http.server
import socketserver
import json

PORT = 8000
connection = database.newConnection()
cursor = database.newCursor(connection)
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET_subst(self, path):
        if len(path) == 0:
            self.send_header("Content-type", "application/json")
            self.end_headers()
            dbresponse = database.getAll(cursor)
            self.wfile.write(bytes(json.dumps(dbresponse), "utf-8"))
            print(dbresponse)
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
    def do_POST(self):
        path = self.path.strip("/").split("/")
        if len(path) == 0 or path[0] != "subst":
            self.send_error(400)
        else:
            self.do_POST_subst()
    def do_POST_subst(self):
        try:
            content_length = int(self.headers['Content-Length'])
            content = json.loads(self.rfile.read(content_length))
        except:
            self.send_error(400)
            raise
        if self.headers['Content-Type'] != "application/json":
            self.send_header("Accept", "application/json")
            self.send_error(406)
            return
        try:
            database.createEntry(cursor, content['date'], content['class'], content['hour'], content['teacher'], content['room'], content['notes'])
            connection.commit()
            self.send_response(200)
        except KeyError:
            self.send_error(400)




with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()