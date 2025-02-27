# 🚀 Odoo Hiscox Integration  

## 📌 Overview  
Odoo Hiscox Integration is an Odoo 16 module that connects with the **Hiscox API** to manage customer applications. It enables users to:  

✅ Collect customer data (name, email, phone, application status).  
✅ Generate a **QR Code** for submission.  
✅ Submit customer data to **Hiscox API** via a **POST** request.  
✅ Query and update application status from **Hiscox API** via a **GET** request.  
✅ Implement **error handling and logging** for robustness.  
✅ Run inside **Docker** with PostgreSQL.  

---

## 🐳 Setup & Installation  

### 1️⃣ Clone the Repository  
Run the following commands in your terminal:  

```bash
git clone https://github.com/your-username/odoo-hiscox-integration.git
cd odoo-hiscox-integration
```

### 2️⃣ Create & Configure `odoo.conf`  
Ensure `config/odoo.conf` exists and is correctly configured.

### 3️⃣ Run Odoo with Docker  
Start Odoo and PostgreSQL using:  

```bash
docker-compose up -d
```

This will start Odoo on `localhost:8069`.

### 4️⃣ Access Odoo  
Open your browser and go to:  

```
http://localhost:8069
```

Use the default Odoo credentials:  
- **Username:** `admin`  
- **Password:** `admin`  

### 5️⃣ Install the Module  
- Navigate to **Apps**.  
- Enable **Developer Mode**.  
- Search for **"Hiscox Integration"** and install it.  

---

## 🔗 API Integration  

### 🚀 Submit Data (POST Request)  
The module submits customer applications to the **Hiscox API** when the user clicks **Submit**.

**API Endpoint:**  
```bash
POST https://hiscoxapi.free.beeceptor.com/v1/applications
```

**Example Payload:**  
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890"
}
```

### 📌 Check Application Status (GET Request)  
The module queries the **Hiscox API** to fetch the latest status.

**API Endpoint:**  
```bash
GET https://hiscoxapi.free.beeceptor.com/v1/applications/{case_id}/status
```

---

## 🛠️ Customization  
Modify the `hiscox_api.py` file to:  
- Connect to a **real Hiscox API**.  
- Enhance **error handling and logging**.  

---

## 📜 License  
This project is licensed under the **MIT License**.

---

## 🤝 Contributing  
Feel free to **fork** this repository and submit a **pull request** to contribute improvements!  
