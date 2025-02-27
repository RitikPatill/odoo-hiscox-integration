🚀 Odoo Hiscox Integration
📌 Overview
This is an Odoo 16 module that integrates with Hiscox API to manage customer applications. It allows users to:

✅ Collect customer data (name, email, phone, application status).
✅ Generate a QR Code for submission.
✅ Submit customer data to Hiscox API via a POST request.
✅ Query and update application status from Hiscox API via a GET request.
✅ Implement error handling and logging for robustness.
✅ Run inside Docker with PostgreSQL.
🏗️ Project Structure
lua
Copy
Edit
|-- addons/
|   |-- odoo_hiscox_integration/
|       |-- models/
|       |   |-- hiscox_case.py
|       |   |-- __init__.py
|       |-- security/
|       |   |-- ir.model.access.csv
|       |-- services/
|       |   |-- hiscox_api.py
|       |   |-- logger.py
|       |   |-- qr_generator.py
|       |   |-- __init__.py
|       |-- views/
|       |   |-- hiscox_case_views.xml
|       |-- __init__.py
|       |-- __manifest__.py
|-- config/
|   |-- odoo.conf
|-- docker-compose.yml
|-- README.md
🐳 Setup & Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/odoo-hiscox-integration.git
cd odoo-hiscox-integration
2️⃣ Create & Configure odoo.conf
Ensure config/odoo.conf exists and has the correct configuration.

3️⃣ Run Odoo with Docker
bash
Copy
Edit
docker-compose up -d
This will start Odoo on localhost:8069 and PostgreSQL.

4️⃣ Access Odoo
Open your browser and go to:
arduino
Copy
Edit
http://localhost:8069
Use default Odoo credentials:
Username: admin
Password: admin
5️⃣ Install the Module
Navigate to Apps.
Enable Developer Mode.
Search for "Hiscox Integration" and install it.
🔗 API Integration
Submit Data (POST Request)
The module submits customer applications to the Hiscox API when the user clicks Submit.

API Endpoint:

bash
Copy
Edit
POST https://hiscoxapi.free.beeceptor.com/v1/applications
Example Payload:

json
Copy
Edit
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890"
}
Check Application Status (GET Request)
The module queries the Hiscox API to fetch the latest status.

API Endpoint:
bash
Copy
Edit
GET https://hiscoxapi.free.beeceptor.com/v1/applications/{case_id}/status
🛠️ Customization
You can modify the hiscox_api.py file to point to a real API or enhance error handling.

📜 License
This project is under the MIT License.

🤝 Contributing
Feel free to fork the project and submit a pull request if you want to improve this module!

