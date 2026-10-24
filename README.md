
# Hive

Hive is a small toolkit for sharing your notes and documents. It has two parts that work on the same `uploads` folder:

- **`Hive.py`** is a Flask web page for uploading files into folders and downloading them again. Pair it with ngrok to share it with colleagues and friends.
- **`html_viewer.py`** is a desktop application built with PyQt5 that allows you to browse and view HTML files from a specified folder. The left panel displays a file tree, and the right panel shows the selected HTML file in a browser view.

## Features
- Upload several files at once into an existing folder, or create a new (nested) folder such as `STTN623/Chapter 0` (`Hive.py`)
- See the files in a folder and download them from the browser (`Hive.py`)
- Browse HTML files in a folder (`html_viewer.py`)
- View HTML content in an embedded browser (`html_viewer.py`)
- Simple, modern UI
- Use ngrok to create temporary public sites for sharing your notes and documents

## Project Structure
```
hive/
├── Hive.py            # Flask upload/download server on http://127.0.0.1:5000
├── html_viewer.py     # PyQt5 desktop viewer for the HTML files in uploads/
├── requirements.txt   # PyQt5 and PyQtWebEngine (Flask is installed separately, see below)
└── uploads/           # Your files; created by Hive.py on first run and ignored by git
```

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/TafaraBean/hive.git
   cd hive
   ```
2. **Create a virtual environment:**
   ```sh
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   source .venv/bin/activate     # macOS/Linux
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   pip install flask
   ```
   (`Hive.py` needs Flask, which isn't listed in `requirements.txt` yet.)
4. **Install ngrok:**
   - Download ngrok from https://ngrok.com/download
   - Unzip and place the executable in your PATH

## Usage

Run both scripts from the project folder so they use the same `uploads` folder.

1. Start the upload server:
   ```sh
   python Hive.py
   ```
   Open http://127.0.0.1:5000, pick a target folder (or type a new folder name), select your files and click **Upload**. The `uploads` folder is created automatically. You can also copy HTML files straight into `uploads` (create it if it doesn't exist).
2. To read your HTML files on your own computer, run the application:
   ```sh
   python html_viewer.py
   ```
3. Select an HTML file from the left panel to view it.
4. To share your work, open a new terminal window and run:
   ```sh
   ngrok http 5000
   ```
   (Make sure `Hive.py` is running before you start ngrok.)
   Share the generated ngrok URL with your colleagues and friends so they can access your notes and documents. Visitors see the same upload page and can download files from it.

## Notes
- The `.venv` folder and `uploads` are excluded from version control via `.gitignore`.
- Only `.html` and `.htm` files are shown in the desktop viewer's file browser.
- Ngrok creates a temporary public URL for your local site, making sharing easy. `Hive.py` has no login and doesn't check folder names or download paths, so anyone with the link can upload files and may be able to reach files outside `uploads`. Only share the link with people you trust, and stop ngrok when you're done sharing.
- Download links only work for files inside a folder. Files uploaded without choosing or creating a folder land at the top level of `uploads`; they appear in the list, but their links return "Not Found".

## License
MIT
