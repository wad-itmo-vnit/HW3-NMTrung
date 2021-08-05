from flask import Flask, render_template, send_from_directory, send_file

app = Flask(__name__)
@app.route('/')
def hw31():
    return render_template('index.html')

@app.route('/img/get/<number>')
def serve_img(number):
    if (len(number) < 2):
        file_name = './static/images/img0' + number + '.jpg'
    else:
        file_name = './static/images/img'+ number + '.jpg'
    return send_file(file_name)

@app.route('/img/<image_name>')
def hw32(image_name):
    file_name = './static/images/' + image_name + '.jpg'
    return send_file(file_name)

@app.route('/static/<filename>')
def hw33(filename):
    css = 'css'
    if css in filename:
        file_name = './static/css/' + filename
    else:
        file_name = './static/js/' + filename
    return send_file(file_name)

app.run(host='localhost', port=5000)