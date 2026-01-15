# 🔐 Password Manager & Generator

A desktop password manager application built with **Python** and **Tkinter** that allows users to generate secure passwords, store credentials locally, and search for saved entries.

All data is persisted in a local `data.json` file, simulating a lightweight credential database.

---

## 🎯 Project Purpose

This project was developed to practice and demonstrate:

- Building desktop applications with **Tkinter**
- Generating secure random passwords
- Reading and writing structured data using **JSON**
- User input validation and confirmation dialogs
- Basic data persistence and error handling
- Event-driven programming in Python

---

## 🧠 Features

### 🔑 Password Generator
- Generates random passwords containing:
  - Uppercase and lowercase letters
  - Numbers
  - Symbols
- Automatically inserts the generated password into the input field

### 💾 Save Credentials
- Stores:
  - Website name
  - Email / Username
  - Password
- Confirms data before saving
- Automatically creates `data.json` if it does not exist

### 🔍 Search Tool
- Search credentials by website name
- Displays stored email and password
- Handles missing entries gracefully with user feedback

---

## 📁 Project Structure

password-manager/
│
├── main.py # Main application logic and UI
├── data.json # Local storage for saved credentials
├── logo.png # Application logo
└── README.md

yaml
Copiar código

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** – graphical user interface
- **JSON** – local data persistence
- **random** – password generation
- **tkinter.messagebox** – user feedback and confirmations

---

## ▶️ How to Run the Project

1. Make sure Python 3 is installed on your system.
2. Clone the repository:
   git clone https://github.com/dev-gabrielsn/password-manager.git
3. Navigate to the project folder:
   cd password-manager
4. Run the application:
   python main.py


## Concepts Applied

- Event-driven GUI programming
- Exception handling (try / except / else / finally)
- Data validation
- File I/O with JSON
- Separation of UI actions and application logic
- Basic UX principles (confirmation dialogs, feedback messages)
 
## Possible Future Improvements

- Encrypt stored passwords
- Add a master password for authentication
- Hide and reveal password functionality
- Copy password to clipboard
- Refactor into multiple modules
- Add automated tests
