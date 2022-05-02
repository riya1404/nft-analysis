from flask import Flask, jsonify, render_template, request



app = Flask(__name__)

@app.route("/")
def func1():
     
	return render_template("front.html")
     
   
@app.route("/info")
def information():
      return render_template("info.html")

  
app.run(debug=True)
