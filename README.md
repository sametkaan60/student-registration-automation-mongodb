# Öğrenci Kayıt Otomasyonu / Student Registry Automation (MongoDB & Flask)

[Turkish](#türkçe) | [English](#english)

---

## Türkçe

Bu proje, MongoDB atlas veya yerel MongoDB sunucusu kullanarak öğrencileri kaydetmek, aramak, listelemek ve silmek için modern bir web arayüzü sağlar.

### 🚀 Özellikler

- **Modern Arayüz**: Glassmorphism ve dark mode destekli premium tasarım.
- **Full CRUD**: Öğrenci ekleme, arama, listeleme ve silme (tekli veya toplu).
- **Mock Modu**: MongoDB sunucusu çalışmasa bile uygulamanın test edilebilmesi için otomatik fallback.
- **Responsive Tasarım**: Mobil ve masaüstü cihazlarla tam uyumlu.

### 🛠️ Kurulum

1. Python bağımlılıklarını yükleyin:
   ```bash
   pip install flask pymongo flask-cors
   ```

2. Uygulamayı başlatın:
   ```bash
   python app.py
   ```

3. Tarayıcınızda açın: `http://127.0.0.1:5000`

---

## English

This project provides a modern web interface for registering, searching, listing, and deleting students using MongoDB Atlas or a local MongoDB server.

### 🚀 Features

- **Modern Interface**: Premium design with glassmorphism and dark mode support.
- **Full CRUD**: Add, search, list, and delete students (individual or bulk).
- **Mock Mode**: Automatic fallback to test the application even without a running MongoDB server.
- **Responsive Design**: Fully compatible with mobile and desktop devices.

### 🛠️ Installation

1. Install Python dependencies:
   ```bash
   pip install flask pymongo flask-cors
   ```

2. Start the application:
   ```bash
   python app.py
   ```

3. Open in your browser: `http://127.0.0.1:5000`

---

## 📁 Proje Yapısı / Project Structure

- `app.py`: Flask backend & API endpoints.
- `templates/index.html`: Main web interface.
- `static/css/style.css`: Premium styling.
- `main.py`: Original CLI-based application.