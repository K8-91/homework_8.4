from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/mypage/me', methods = ['GET'])
def me():
    return render_template("mypage_me.html")

@app.route('/mypage/contact', methods = ['GET'])
def contact():
    return render_template("mypage_contact.html")

@app.route('/mypage/contact', methods = ['POST'])
def post_contact():
    print(request.mypage_contact)
    return redirect('/mypage/me')