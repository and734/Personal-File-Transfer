from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit


def get_unique_filename(filename):
    filename = secure_filename(filename)
    if not filename:
        return None
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(UPLOAD_FOLDER, new_filename)):
        new_filename = f"{base} ({counter}){ext}"
        counter += 1

    return new_filename

@app.route('/')
def index():
    return render_template('index.html', title="File Transfer")


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file:
        unique_filename = get_unique_filename(file.filename)
        if unique_filename:
            try:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
                return f"File uploaded successfully as {unique_filename}!"
            except Exception as e:
                return f"An error occurred: {str(e)}"
        else:
            return "Invalid filename."

    return redirect(url_for('index'))


@app.route('/files')
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('files.html', files=files)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

