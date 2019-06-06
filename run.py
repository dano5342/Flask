import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # @ is a pyNotation
def index():
    return render_template("index.html")
    
#Flask injects the @app.route functions, these are called within the application and then
#as long as these are within the folder of "Templates" then the files will load with the HTML 
# Being directed to the browser.

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/careers')
def careers():
    return render_template("careers.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
         debug=True)
    ## Never have the above argument = true with deployed projects or anything LIVE
    # as this opens up the possiblity for bad defensive development.
    
