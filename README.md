Secure Password Manager

A desktop-based password manager built with Python, CustomTkinter, SQLite, and Cryptography.

The application allows users to securely store, manage, and retrieve website credentials using a master password and encrypted password storage.

 Features

-  Master password authentication
-  Encrypted password storage using Fernet
- Random salt generation
- PBKDF2-HMAC-SHA256 key derivation
-  Local SQLite database
- Search and manage saved credentials
-  Copy passwords to clipboard
- Delete saved credentials
- Secure password generation
-  Modern desktop GUI using CustomTkinter
-  Dark-mode interface
-  Input validation and error handling


 Technologies Used

Technology| Purpose
Python| Application development
CustomTkinter| Graphical user interface
SQLite| Local database storage
Cryptography| Password encryption/decryption
Hashlib| Password hashing and key derivation
Secrets| Secure password generation
Git & GitHub| Version control and project management.

Security Concepts

This project demonstrates several important security concepts:

Master Password Authentication

The master password is not stored directly in the database.

A salted hash is generated for authentication.

Password Hashing

SHA-256 is used to create a hash of the master password combined with a randomly generated salt.

Key Derivation

PBKDF2-HMAC-SHA256 is used to derive an encryption key from the master password and salt.

Password Encryption

Stored website passwords are encrypted using Fernet symmetric encryption before being inserted into the database.

The encrypted password is decrypted only whe the authenticated user accesses the password vault.



Project Structure

SecurePasswordManager/
│
├── main.py
├── gui.py
├── auth.py
├── crypto_utils.py
├── database.py
├── password.py
├── requirements.txt
├── README.md
└── vault.db

File Description

"main.py"
Application entry point.

"gui.py"
Contains the graphical user interface, login screen, password vault, and user interactions.

"auth.py"
Handles master password registration and authentication.

"crypto_utils.py"
Handles encryption, decryption, and cryptographic key derivation.

"database.py"
Handles SQLite database initialization and credential storage/retrieval.

"password.py"
Generates secure passwords and checks password strength.

"requirements.txt"
Contains the Python packages required to run the application.

"vault.db"
Local SQLite database used by the application.


 Installation

1. Clone the Repository

git clone https://github.com/mp1924/SecurePasswordManager.git

2. Open the Project Folder

cd SecurePasswordManager

3. Install Dependencies

pip install -r requirements.txt

4. Run the Application

python main.py


First-Time Setup

When the application is launched for the first time:

1. Enter a master password.
2. Select First Time Setup.
3. The master password authentication data is stored securely.
4. Restart the application.
5. Enter the master password to access the password vault.


Using the Password Vault

After successful authentication, users can:

1. Enter a website name.
2. Enter the username.
3. Enter the password.
4. Save the credential.
5. View saved credentials in the password table.
6. Copy a password to the clipboard.
7. Delete unwanted credentials.
8. Refresh the vault.


Requirements

The project requires:

customtkinter
cryptography

Install them using:

pip install -r requirements.txt


 What I Learned

Through this project, I gained practical experience with:

- Python application development
- GUI development with CustomTkinter
- SQLite database management
- CRUD operations
- Password hashing
- Salt generation
- PBKDF2 key derivation
- Symmetric encryption
- Authentication systems
- Secure password generation
- Exception handling
- Git and GitHub workflow
- Structuring a multi-file Python project

 Future Improvements

Possible future improvements include:

- Password visibility toggle
- Password strength indicator
- Search/filter functionality
- Automatic password generation from the GUI
- Clipboard auto-clear
- Improved database security
- Export/import functionality
- Better UI themes
- Unit testing
- Automated testing with GitHub Actions

This project was created for educational and portfolio purposes to demonstrate concepts related to Python development, databases, authentication, and basic application security.
