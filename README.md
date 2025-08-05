
# HTML Viewer with Navigation

This project is a desktop application built with PyQt5 that allows you to browse and view HTML files from a specified folder. The left panel displays a file tree, and the right panel shows the selected HTML file in a browser view.

## Features
- Browse HTML files in a folder
- View HTML content in an embedded browser
- Simple, modern UI
- Use ngrok to create temporary public sites for sharing your notes and documents

## Installation

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd Hive
   ```
2. **Create a virtual environment:**
   ```sh
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Install ngrok:**
   - Download ngrok from https://ngrok.com/download
   - Unzip and place the executable in your PATH

## Usage

1. Place your HTML files in the `uploads` folder (create it if it doesn't exist).
2. Run the application:
   ```sh
   python html_viewer.py
   ```
3. Select an HTML file from the left panel to view it.
4. To share your work, open a new terminal window and run:
   ```sh
   ngrok http 5000
   ```
   (Make sure Hive is running before you start ngrok.)
   Share the generated ngrok URL with your colleagues and friends so they can access your notes and documents.

## Notes
- The `.venv` folder and `uploads` are excluded from version control via `.gitignore`.
- Only `.html` and `.htm` files are shown in the file browser.
- Ngrok creates a temporary public URL for your local site, making sharing easy and secure.

## License
MIT
