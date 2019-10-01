from flask import Flask   , render_template, request
from flask_mail import Mail, Message
from config import configuration


app = Flask(__name__)

app.config.update(configuration)
app.secret_key = 'mysecretkey'



mail = Mail(app)
 

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route('/sendMail', methods=['POST'])
def sendMail():
     subject = request.form['subject']
     user_emails = request.form['email']
     message = request.form["message"]
     msg = Message(subject=subject, 
                sender= "ppizzery@gmail.com", 
                recipients=[user_emails],
                body= message)
     mail.send(msg)
     # flash('Message sent successfully')
     return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)