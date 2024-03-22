import os
import flask
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
PORT = 5555

web_name = "Test Server"

print("")
print(f"IP      : {IP}")
print(f"PORT    : {PORT}")
print(f"web name: {web_name}")
print("")

app = flask.Flask(__name__)

@app.route('/GET/<path>')
def GET(path):
	path_string = path.replace('-', '/')
	
	try:
		r = open(f"{path_string}.svr", "r")
		value = r.read()
		r.close()
	
		return value
	except:
		return "NULL"

@app.route('/POST/<path>/<value>')
def POST(path, value):
	path_string = f"{path.replace('-', '/')}.svr"
	
	os.makedirs(os.path.dirname(path_string), exist_ok=True)
	
	r = open(path_string, "w")
	r.write(value)
	r.close()
	
	return "TRUE"
    

@app.route('/')
def home():
	return web_name

if __name__ == '__main__':
	app.run(host=IP, port=PORT)
