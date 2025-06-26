# 🧪 SQL Injection Test Website

A simple, intentionally vulnerable web application created to demonstrate and test **SQL Injection** attacks. This project is meant **strictly for educational and security testing purposes**.

---

## 📚 About the Project

This project simulates common SQL injection vulnerabilities through login forms and input fields. It is designed to help developers understand how SQL injection works and how to prevent it.

---

## 🔧 Technologies Used

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask
- **Database:** SQlite

---

## 🚀 Installation

1.Clone the repository:
   ```bash
   git clone https://github.com/Rafaelorr/bank_website.git
   cd bank_website
```

2.Install depencies:
   ```bash
   pip install -r requirements.txt
```

3.Create a new database
   ```bash
   python3 database_creation.py
```

4.Run the app:
   ```bash
   python3 app.py
```

---

## 🎯 What You Can Test

* Login forms with unfiltered input
* Search fields that pass data directly into SQL queries
* Any user input field that interacts with the database

---

## 🛡️ What You'll Learn

* How SQL Injection attacks work
* Why input validation and sanitization matter
* How to fix vulnerabilities using:

  * Prepared statements / parameterized queries
  * Input filtering and escaping
  * Proper error handling and logging

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.
You are free to use, share, and modify this software under the terms of the license.
For more details, see the [LICENSE](./LICENSE) file or visit [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html).

---

## 🤝 Collaboration

I welcome and appreciate collaboration!  
But there're some guidelines to make things easier.

### 💡 Guidelines
   * Write clear, concise commit messages.

   * Follow the existing naming conventions.

   * Please be respectful in discussions.
