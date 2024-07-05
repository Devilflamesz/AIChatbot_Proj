from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import spacy
import os
import re

app = Flask(__name__)
CORS(app)
nlp = spacy.load("en_core_web_sm")

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        classification = classify_file(filepath)
        return jsonify({'classification': classification}), 200
    return jsonify({'error': 'File type not allowed'}), 400

def classify_file(filepath):
    with open(filepath, 'r') as file:
        content = file.read().lower()  # Convert content to lowercase for case-insensitive matching

    # Define classification keywords with regex patterns
    top_secret_patterns = [
        r'exceptionally grave damage',
        r'highly sensitive',
        r'top secret',
        r'critical to national security',
        r'for eyes only',
        r'national security threat',
        r'extremely sensitive',
        r'highly classified',
        r'confidential source',
        r'eyes only',
        r'need to know basis',
        r'highly restricted',
        r'extremely confidential'
    ]

    secret_patterns = [
        r'serious damage',
        r'sensitive information',
        r'secret',
        r'not for public release',
        r'highly confidential',
        r'privileged information',
        r'proprietary information',
        r'confidential communication',
        r'internal circulation',
        r'limited access',
        r'need to know',
        r'highly sensitive information'
    ]

    confidential_patterns = [
        r'some damage',
        r'confidential',
        r'internal use only',
        r'privileged information',
        r'proprietary information',
        r'limited distribution',
        r'need to know',
        r'internal circulation',
        r'staff only',
        r'official use only',
        r'sensitive data',
        r'confidential material'
    ]

    restricted_patterns = [
        r'some disruption',
        r'restricted',
        r'limited distribution',
        r'need to know',
        r'internal circulation',
        r'access restricted',
        r'controlled access',
        r'sensitive information',
        r'confidential data',
        r'limited access',
        r'official business'
    ]

    official_closed_patterns = [
        r'negligible impact',
        r'official \(closed\)',
        r'internal use only',
        r'not for public distribution',
        r'staff only',
        r'official business',
        r'confidential communication',
        r'internal circulation',
        r'limited access',
        r'need to know',
        r'official use only'
    ]

    official_open_patterns = [
        r'public information',
        r'official \(open\)',
        r'for public release',
        r'open data',
        r'public domain',
        r'unclassified',
        r'publicly available',
        r'general knowledge',
        r'public record',
        r'open source'
    ]

    # Check for classification using regex
    if any(re.search(pattern, content) for pattern in top_secret_patterns):
        return "Top Secret"
    elif any(re.search(pattern, content) for pattern in secret_patterns):
        return "Secret"
    elif any(re.search(pattern, content) for pattern in confidential_patterns):
        return "Confidential"
    elif any(re.search(pattern, content) for pattern in restricted_patterns):
        return "Restricted"
    elif any(re.search(pattern, content) for pattern in official_closed_patterns):
        return "Official (Closed)"
    elif any(re.search(pattern, content) for pattern in official_open_patterns):
        return "Official (Open)"
    else:
        return "Unclassified"

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
