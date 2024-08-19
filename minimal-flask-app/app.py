
#* Creating a minimal flask application

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

# Routing and Handling requests
'''	
Routes in Flask are defined using the @app.route() decorator. This tells Flask which URLs should trigger which functions.
'''	
@app.route('/about')
def about():
    return 'This is the About Page'



# Rendering Templates

'''
Templates are files that contain HTML and variables. They are rendered using a template engine like Jinja2.
'''
@app.route('/index')
def index():
    return render_template('index.html')
    



# Running the application
if __name__ == '__main__':
    app.run(debug=True)