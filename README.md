# HTML Viewer with Navigation

This project is a desktop application built with PyQt5 that allows you to browse and view HTML files from a specified folder. The left panel displays a file tree, and the right panel shows the selected HTML file in a browser view.

## Features
- Browse HTML files in a folder
- View HTML content in an embedded browser
- Simple, modern UI

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

## Usage

1. Place your HTML files in the `uploads` folder (create it if it doesn't exist).
2. Run the application:
   ```sh
   python html_viewer.py
   ```
3. Select an HTML file from the left panel to view it.

## Notes
- The `.venv` folder and `uploads` are excluded from version control via `.gitignore`.
- Only `.html` and `.htm` files are shown in the file browser.

## License
MIT
