from flask import Flask ,render_template
from flask import Flask, render_template
from controllers import aws_controller


app = Flask(__name__)
   

@app.route('/', methods=['GET'])
def index():
    data=aws_controller.get_items()
    return render_template('index.html',films=data)


        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)