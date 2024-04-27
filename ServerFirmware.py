# Server firmware built by Miguel
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import html

hostName = "localhost"
serverPort = 8080
print("")
ipaddr = input("Address to run from: > ")
print("Running server firmware version 1.7.2")
print("Files are stored in: " + os.getcwd())

filelist = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            filename = "index.html"
        elif self.path == "/favicon.ico":
            # Handle favicon request (provide a default favicon or an empty response)
            self.send_response(200)
            self.send_header("Content-type", "image/x-icon")
            self.end_headers()
            return
        else:
            filename = self.path[1:]

        # Logging the requested file
        print("Requested file:", filename)

        try:
            with open(filename, 'rb') as file:
                self.send_response(200)
                self.send_header("Content-type", self.content_type(filename))
                self.end_headers()

                # Read and send the file content
                content = file.read()
                self.wfile.write(content)

        except FileNotFoundError:
            # Handle file not found error
            self.send_error(404, 'File Not Found: {}'.format(self.path))
        except Exception as e:
            # Log other exceptions
            print("Error serving file:", str(e))
            self.send_error(500, 'Internal Server Error: {}'.format(str(e)))

    def content_type(self, file):
        _, extension = os.path.splitext(file)
        ContentTypes = {
            '.html': 'text/html',
            '.css': 'text/css',
            '.js': 'application/javascript',
        }
        return ContentTypes.get(extension.lower(), 'application/octet-stream')

if __name__ == "__main__":
    server_address = (ipaddr, 8000) # Runs at 192.168.2.16:8000
    httpd = HTTPServer(server_address, MyServer)
    print('Running at: ' + ipaddr +':8000')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("Server stopped manually.")