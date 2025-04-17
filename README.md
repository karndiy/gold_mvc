# 🪙 Gold Price Scraper API (Flask + Docker)

This is a simple Flask web app that scrapes gold prices from the Gold Traders website and stores them in a SQLite database using an MVC pattern. It includes a REST API to fetch the data and Docker support for easy deployment.

---

## 📦 Features

- Scrape real-time gold prices from [goldtraders.or.th](https://www.goldtraders.or.th/)
- Save data to a local SQLite database
- Prevent duplicate entries based on `asdate`
- REST API endpoint for accessing stored gold data
- Docker & Docker Compose support

---

## 🚀 Live Endpoints

| Method | Route              | Description                    |
|--------|--------------------|--------------------------------|
| GET    | `/`                | View data in HTML              |
| GET    | `/api/gold`        | All gold prices in JSON        |
| GET    | `/api/gold_date`   | Latest data by `asdate`        |
| GET    | `/scrape`          | Trigger gold price scraping    |

---

## 🔧 Setup (without Docker)

```bash
# Create virtual env and activate
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install requirements
pip install -r requirements.txt

# Run the Flask app
flask run
---------------------------

🐳 Run with Docker
Build & Run the app
---------------------------
docker-compose up --build
###########################
Stop the app
--------------------------
docker-compose down
##########################


📁 Project Structure
gold_mvc/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   └── gold_model.py
│   ├── controllers/
│   │   └── gold_controller.py
│   ├── services/
│   │   └── gold_scraper.py
│   └── templates/
│       └── index.html
├── gold.db
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
-------------------------
📝 License
MIT License — Free to use, share, and modify.

✨ Author
Developed by Karn Lalokkeaw (กานต์ ละลอกแก้ว)
📧 karndiy@gmail.com | 📱 065-5659178 | 📍 Bangkok, Thailand
