# 📦 Django DRF CSV Upload API

A Django REST Framework (DRF) based API that allows users to upload a CSV file, validate the data, and store valid records in the database. The API provides a detailed summary of successful and failed records.

---

## 🚀 Features

- 📤 Upload CSV file via API
- ✅ Data validation using DRF serializers
- 📧 Email validation & age constraints
- ⚠️ Duplicate email handling (skipped safely)
- 📊 Summary response (success + rejected records)
- 🧪 Unit testing using Django TestCase

---

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (default DB)
- CSV (Python Standard Library)

---

## 📂 Project Setup (From Scratch)

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd <your-project-folder>
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
source env/bin/activate  # Linux / Mac
env\Scripts\activate     # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

> If requirements.txt is not available:
```bash
pip install django djangorestframework
```

---

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Run Development Server

```bash
python manage.py runserver
```

Server will run at:
```
http://127.0.0.1:8000/
```

---

## 📡 API Endpoints

### 🔹 Upload CSV

- **URL:** `/users/upload-csv/`
- **Method:** `POST`
- **Content-Type:** `multipart/form-data`

#### 📥 Request

| Key  | Type | Description |
|------|------|------------|
| file | File | CSV file |

---

### 📄 Sample CSV Format

```csv
name,email,age
John Doe,john@example.com,25
Jane Doe,jane@example.com,30
```

---

### 📤 Response Example

```json
{
  "success_count": 2,
  "rejected_count": 1,
  "errors": [
    {
      "row": 3,
      "error": {
        "email": ["Enter a valid email address."]
      },
      "data": {
        "name": "Invalid",
        "email": "invalidemail",
        "age": "25"
      }
    }
  ]
}
```

---

## ⚠️ Validation Rules

- `name` → must not be empty
- `email` → must be valid format
- `age` → must be between 0 and 120
- duplicate emails → skipped

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 📚 References

- Django Documentation: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- Python CSV Module: https://docs.python.org/3/library/csv.html

---

## 👨‍💻 Author

**Vysakh E**  
Python Full Stack Developer

---

## ⭐ Notes

This project follows clean code practices with:
- Modular ViewSet design
- Serializer-based validation
- Proper error handling
- Scalable structure for future improvements
