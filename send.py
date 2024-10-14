import	http.server
import	socketserver
import	os

PORT = 4040
FILE_PATH = "/home/tolrandr/goinfre/Win10_22H2_French_x64v1.iso"

class	SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/':  # Rediriger vers le fichier
			self.path = '/' + os.path.basename(FILE_PATH)
		return super().do_GET()

os.chdir(os.path.dirname(FILE_PATH))  # Change le répertoire courant

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
	print(f"Le serveur est démarré sur {PORT}, accédez à http://votre_adresse_IP_locale:{PORT}/")
	httpd.serve_forever()
