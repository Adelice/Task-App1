from flask import Flask

#create the flask app instance 
app=Flask(__name__)

# create the first route which is a homepage
@app.route("/")
def index():
	return "<h1>Python Operations with Flask Routing and Views</h1>"
# create a second route (/print/Hello) with a string_print view

@app.route("/print/<x>")
def print_string(x):
	print(x) # for the console 
	return x # for the browser

# Third route (/count/4)
@app.route("/count/<int:num>")
def count(num):
	result=""
	for i in range(1,num+1):
		result+= str(i) + "<br>"
	return result 
@app.route("/math/<int:num1>/<operation>/<int:num2>")

# Run the development server 
if __name__=="__main__":
	app.run(debug=True)
