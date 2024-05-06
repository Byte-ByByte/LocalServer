# Server firmware built by Miguel
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import html

hostName = "localhost"
serverPort = 8080
print("")
ipaddr = input("Address to run from: > ")
ipport = input("Port to run from: > ")
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
        ContentTypes = { # Define MIME types
        	'.htm': 'text/html',
            '.html': 'text/html',
            '.css': 'text/css',
            '.js': 'application/javascript',
            '.aac': 'audio/acc',
            '.abw': 'application/x-abiword',
            '.apng': 'image/apng',
            '.arc': 'application/x-freearc',
            '.avif': 'image/avif',
            '.avi': 'video/x-msvideo',
            '.azw': 'application/vnd.amazon.ebook',
            '.bin': 'application/octet-stream',
            '.bz2': 'application/x-bzip2',
            '.cda': 'application/x-cdf',
            '.csh': 'application/x-csh',
            '.csv': 'text/csv',
            '.doc': 'application/msword',
            '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            '.eot': 'application/vnd.ms-fontobject',
            '.epub': 'application/epub+zip',
            '.gz': 'application/octet-stream', # Use 'application/gzip' for non-download files
            '.gif': 'image/gif',
            '.ico': 'application/vnd.microsoft.icon',
            '.ics': 'text/calendar',
            '.jar': 'application/java-archive',
            '.jpeg': 'image/jpeg',
            '.jpg': 'image/jpeg',
            '.json': 'application/json',
            '.jsonld': 'application/ld+json',
            '.mid': 'audio/midi',
            '.midi': 'audio/midi',
            '.mjs': 'text/javascript',
            '.mp3': 'audio/mpeg',
            '.mp4': 'video/mp4',
            '.mpeg': 'video/mpeg',
            '.mpkg': 'application/vnd.apple.installer+xml',
            '.odp': 'application/vnd.oasis.opendocument.presentation',
            '.ods': 'application/vnd.oasis.opendocument.spreadsheet',
            '.odt':'application/vnd.oasis.opendocument.text',
            '.oga': 'audio/ogg',
            '.ogv': 'video/ogg',
            '.ogx':'application/ogg',
            '.opus': 'audio/opus',
            '.otf': 'font/otf',
            '.png': 'image/png',
            '.pdf': 'application/pdf',
            '.php': 'application/x-httpd-php',
            '.ppt': 'application/vnd.ms.powerpoint',
            '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
            '.rar': 'application/octet-stream', # Use 'application/vnd.rar' for non-download files
            '.rtf': 'application/rtf',
            '.sh': 'application/x.sh',
            '.svg': 'image/svg+xml',
            '.tar': 'application/x-tar',
            '.tif': 'image/tiff',
            '.tiff': 'image/tiff',
            '.ts':  'video/mp2t',
            '.ttf': 'font/ttf',
            '.txt': 'text/plain',
            '.vsd': 'application/vnd.visio',
            '.wav': 'audio/wav',
            '.weba': 'audio/webm',
            '.webm': 'video/webm',
            '.webp': 'image/webp',
            '.woff': 'font/woff',
            '.woff2': 'font/woff2',
            '.xhtml': 'application/xhtml+xml',
            '.xls': 'application/vnd.ms-excel',
            '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            '.xml': 'application/xml',
            '.xul': 'application/vnd.mozilla.xul+xml',
            '.zip': 'application/octet-stream', # Use 'application/zip' for non-download files
            '.3gp': 'audio/3gpp',
            '.3g2': 'audio/3gpp2',
            '.7z': 'application/octet-stream', # Use 'application/x-7z-compressed' for non-download files
        }
        return ContentTypes.get(extension.lower(), 'application/octet-stream')

if __name__ == "__main__":
    server_address = (ipaddr, int(ipport)) # Runs at 192.168.2.16:8000
    httpd = HTTPServer(server_address, MyServer)
    print('Running at: ' + ipaddr + ":" + ipport)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print(" Server stopped manually.")
