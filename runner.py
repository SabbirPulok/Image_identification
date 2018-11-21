from flask import Flask, render_template, request

from ml import get_predict

#from werkzeug import secure_filename
app=Flask(__name__)


@app.route('/uploader')
def upload_file():
    return render_template('upload.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        #f.save('Upload/'+f.filename)
        result = get_predict(f)
        if result == 'Car':
            return render_template('car.html')
        if result == 'Moon':
            return render_template('Moon.html')
        if result == 'Mountain':
            return render_template('Mountain.html')



if __name__ == '__main__':
    app.run(debug=True, port=7999)
