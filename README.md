# 📄 MakeMyPDFs - Professional PDF Processing Tool 🚀

MakeMyPDFs is a fast, secure, and modern web application built to handle various PDF operations like Merging, Compressing, and Splitting effortlessly. The project is built completely on Django with a highly responsive, dark-themed UI powered by Tailwind CSS.

---

## ✨ Features
- **Merge PDF:** Combine multiple PDF files into a single document in your desired order.
- **Modern UI/UX:** Premium dark-themed interface built with Tailwind CSS and FontAwesome.
- **Interactive Frontend:** Drag-and-drop file upload, real-time progress bars, and smooth animations using Vanilla JS.
- **Secure Processing:** Files are processed securely in memory using Python.
- **Docker Ready:** Easy deployment and consistent environments across all machines.

*(More features like Compress PDF, Split PDF, etc., are in active development!)*

---

## 🛠️ Tech Stack

**Backend:**
* [Django](https://www.djangoproject.com/) (Python Web Framework)
* PyPDF2 (PDF manipulation)
* Python `io` module (In-memory file processing)

**Frontend:**
* HTML5 & Vanilla JavaScript
* [Tailwind CSS](https://tailwindcss.com/) (Via CDN for rapid UI development)
* FontAwesome (Icons)

---

## 📂 Project Structure
```text
makemypdfs/
│
├── docutools/              # Main Django Project Directory
│   ├── settings.py         # Project settings, configurations
│   └── urls.py             # Main URL routing
│
├── tools/                  # Django App for PDF Tools
│   ├── views.py            # Backend logic (Merge, Compress, etc.)
│   └── urls.py             # App-specific routing
│
├── templates/              # HTML Templates (Tailwind UI)
│   ├── base.html           # Main layout and navbar
│   └── tools/              # Individual tool pages (merge.html, etc.)
│
├── static/                 # Static assets (Custom CSS/JS if any)
├── requirements.txt        # Python dependencies
└── Dockerfile              # Docker image configuration
