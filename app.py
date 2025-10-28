from flask import Flask

#create the flask app instance 
app=Flask(__name__)

# create the first route which is a homepage
@app.route("/")
def home():
	return "Welcome to my Flask App"

# Run the development server 
if __name__=="__main__":
	app.run(debug=True)
