from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_unique_filename(filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(UPLOAD_FOLDER, new_filename)):
        new_filename = f"{base} ({counter}){ext}"
        counter += 1

    return new_filename

@app.route('/')
def index():
    return render_template('files.html', title="File Transfer")

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        unique_filename = get_unique_filename(file.filename) # Generate unique name
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        return f"File uploaded successfully as {unique_filename}!"

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) # Change port here if necessary
