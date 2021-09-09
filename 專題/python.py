# -*- coding: utf-8 -*-


from flask import Flask,render_template
app=Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("留言板.html")

app.run()
