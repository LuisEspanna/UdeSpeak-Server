from flask import Flask, flash, request, redirect, jsonify, send_file, after_this_request
import os
from werkzeug.utils import secure_filename
import whisper
import torch
from flask_cors import CORS
from gtts import gTTS


UPLOAD_FOLDER = 'files'
ALLOWED_EXTENSIONS = {'mp3', 'wav'}

# Cargando whisper
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model_whisper = whisper.load_model("small").to(device)

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# create the folders when setting up your app
os.makedirs(os.path.join(app.instance_path, 'files'), exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.instance_path, 'files', secure_filename(file.filename)))
            # STT
            result = model_whisper.transcribe("instance/files/" + secure_filename(file.filename))

            data = { 
                "text" : result["text"], 
            }

            # Deleting audio file
            if os.path.exists("instance/files/" + secure_filename(file.filename)):
                os.remove("instance/files/" + secure_filename(file.filename))
            else:
                print("The file does not exist")
            return jsonify(data)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/test', methods=['GET'])
def jsonTest():
    data = { 
        "status" : True, 
        "description" : "Server online", 
    }
    return jsonify(data)



@app.route('/tts', methods=['POST'])
def tts():
    body = request.get_json();
    language = body['language']
    text = body['text']
    filename = body['filename']

    if (language, text, filename ) is not None:
        speech = gTTS(text = text, lang = language, slow = False)
        speech.save("instance/files/" + filename)
        if os.path.exists("instance/files/" + filename):
            result = send_file("instance/files/" + filename, as_attachment=True)
            return result
        else:
            print("The file does not exist")
    return jsonify({"status" : False})



@app.route('/tts/<id>', methods=['DELETE'])
def file_deleting(id):
    if os.path.exists("instance/files/" + id):
        os.remove("instance/files/" + id)
    else:
        print("The file does not exist")
    return jsonify({"status" : True})