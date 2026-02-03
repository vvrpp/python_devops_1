from flask import Flask

app = Flask('myapp')
@app.route("/sendEmail")
def sendEmailtoclient():
    return "EMAIL send.. "

@app.route("/log/<mag>")
def log(msg):
    return 'info: your Log' + msg +"is recored" 
@app.route("/showBlog/<int:postID>")
def showblog(postID):
    return 'showing Blog with Post ID' + str(postID)
app.run(debug=True)