from flask import Flask,request,redirect,Response
import requests
app = Flask(__name__)
SITE_NAME = "http://MAIN_SITE_NAME"

@app.route("/",methods=['GET','POST'])
def index():
    global SITE_NAME
    if request.method=="GET":
        resp = requests.get(f"{SITE_NAME}")
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method=="POST":
        resp = requests.post(f"{SITE_NAME}",data=request.form)
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response



@app.route("/<path:path>",methods=["GET","POST"])
def proxy(path):
    global SITE_NAME
    if request.method=="GET":
        resp = requests.get(f"{SITE_NAME}{path}")
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method=="POST":
        resp = requests.post(f"{SITE_NAME}{path}",data=request.form)
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response



if __name__ == "__main__":
    app.run(debug = True,port=1337)
