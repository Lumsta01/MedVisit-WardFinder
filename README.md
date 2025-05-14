
# 📍 MedVisit - WardFinder

**MedVisit - WardFinder** is a hospital visitor registration and ward navigation system. It simplifies the process of registering visitors, linking them with patients, and helping them locate wards using QR code technology and real-time verification.

---

## 🧩 Key Features

- Secure visitor-patient registration with QR code generation
- Real-time patient ward lookup
- Manual and scanner-based registration options
- Web-based interface for easy access
- Local database storage for patient/visitor info

---

## 🚀 Technologies Used

- **Python 3.x** (Back-end logic)
- **SQLite** (Local database)
- **HTML/CSS/JavaScript** (Frontend interface)
- **Flask** or lightweight web server (via `server.py`)
- **qrcode** (QR code generation)

---

## 🛠 Installation Requirements

Before starting, make sure you have the following installed:

- Python 3.10+
- pip
- Optional: A virtual environment (`venv` or `virtualenv`)

### 📦 Dependencies (install via pip):

```bash
pip install qrcode[pil]
```

---

## 📥 Installation Instructions

1. Clone the repository or unzip the downloaded folder:
   ```bash
   git clone https://github.com/yourusername/MedVisit-WardFinder.git
   cd MedVisit-WardFinder
   ```

2. Install dependencies (see above)

3. Run the application:
   ```bash
   cd src
   python server.py
   ```

---

## 🧪 Basic Usage

1. Open your browser and go to `http://localhost:5000` (or the hosted address).
2. Register a visitor and patient.
3. Scan the QR code for verification.
4. Use the "Ward Finder" to locate a patient’s ward.

---

## 🗂 Project Structure Overview

```
MedVisit-WardFinder/
├── README.md
├── visitor_patient_database.db         # SQLite DB file
├── qr_1234.png                         # Example QR code
├── resources/
│   └── html/
│       ├── index.html
│       ├── main.html
│       ├── wardfinder.html
│       ├── registrations.html
│       ├── scripts/
│       │   ├── client.js
│       │   └── main.js
│       └── templates/
│           └── styles.css
├── src/
│   ├── server.py                       # Starts the application server
│   ├── client.py                       # Client handling logic
│   ├── visitor_data.py                 # Visitor info handling
│   ├── verification.py                 # QR verification logic
│   └── qr_generator.py                 # QR code creation logic
```

---

## ⚙ Configuration Options

- `visitor_patient_database.db` — SQLite DB, can be replaced for production with a hosted DB.
- `server.py` — Modify port or IP binding if deploying to a remote server.
- HTML templates can be customized in `resources/html`.

---

## 🧯 Troubleshooting

- **QR code not generating?** Make sure `qrcode[pil]` is installed.
- **Webpage not loading?** Check that `server.py` is running and accessible.
- **Database not updating?** Ensure Python has write access to `visitor_patient_database.db`.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/foo`)
3. Commit your changes (`git commit -am 'Add foo'`)
4. Push to the branch (`git push origin feature/foo`)
5. Create a new Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
