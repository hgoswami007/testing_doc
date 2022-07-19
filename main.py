from wsgiref import simple_server
from flask import Flask,request,render_template
from flask_cors import cross_origin

app = Flask(__name__)

@app.route("/",methods=['GET'])
@cross_origin()
def home():
    return "Good Morning"




port = 5000
if __name__ =="__main__":
    host = '0.0.0.0'
    httpd = simple_server.make_server(host,port,app)
    httpd.serve_forever()
