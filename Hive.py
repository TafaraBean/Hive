import os
from flask import Flask, request, send_from_directory, redirect, url_for, render_template_string

UPLOAD_ROOT = 'uploads'
os.makedirs(UPLOAD_ROOT, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_ROOT

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Multi-File Uploader</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        textarea, select, input[type="file"] { width: 100%%; margin-bottom: 10px; }
        iframe { width: 100%%; height: 400px; border: 1px solid #ccc; }
    </style>
</head>
<body>
    <h2>Upload Files</h2>
    <form method="POST" action="/" enctype="multipart/form-data">
        <label>Select Target Folder:</label>
        <select name="folder">
            {% for folder in folders %}
                <option value="{{ folder }}" {% if folder == current_folder %}selected{% endif %}>{{ folder }}</option>
            {% endfor %}
        </select>
        <br>
        <label>Or Create New Folder:</label>
        <input type="text" name="new_folder" placeholder="e.g. STTN623/Chapter 0"><br>
        <label>Select Files (you can select up to 20):</label>
        <input type="file" name="files[]" multiple><br>
        <input type="submit" value="Upload">
    </form>

    <h3>Files in {{ current_folder or 'uploads' }}:</h3>
    <ul>
        {% for file in files %}
            <li><a href="{{ url_for('download_file', folder=current_folder, filename=file) }}">{{ file }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
'''

def list_all_folders(base):
    folders = []
    for root, dirs, _ in os.walk(base):
        for d in dirs:
            full = os.path.join(root, d)
            rel = os.path.relpath(full, base)
            folders.append(rel.replace("\\", "/"))  # Windows compatibility
    return folders

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    folders = list_all_folders(UPLOAD_ROOT)
    current_folder = ''
    target_path = UPLOAD_ROOT

    if request.method == 'POST':
        new_folder = request.form.get('new_folder', '').strip()
        selected_folder = request.form.get('folder', '').strip()

        if new_folder:
            current_folder = new_folder
        else:
            current_folder = selected_folder

        target_path = os.path.join(UPLOAD_ROOT, current_folder)
        os.makedirs(target_path, exist_ok=True)

        uploaded_files = request.files.getlist('files[]')
        for f in uploaded_files:
            if f and f.filename:
                try:
                    f.save(os.path.join(target_path, f.filename))
                except Exception as e:
                    print(f"❌ Failed to upload {f.filename}: {e}")

        return redirect(url_for('upload_file') + f"?folder={current_folder}")

    # GET method
    current_folder = request.args.get('folder', '')
    target_path = os.path.join(UPLOAD_ROOT, current_folder) if current_folder else UPLOAD_ROOT
    files = os.listdir(target_path) if os.path.exists(target_path) else []

    return render_template_string(HTML, files=files, folders=folders, current_folder=current_folder)

@app.route('/uploads/<path:folder>/<filename>')
def download_file(folder, filename):
    folder_path = os.path.join(UPLOAD_ROOT, folder)
    return send_from_directory(folder_path, filename, as_attachment=True)

if __name__ == '__main__':
    print("✅ Starting Flask server on http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000)
