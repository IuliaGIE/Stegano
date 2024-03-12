# Utilizăm o imagine de bază alpine
FROM python:3.9-alpine

# Setăm directorul de lucru în container
WORKDIR /app

# Copiem fișierele necesare în container
COPY web/app.py .
COPY web/utils.py .
COPY web/templates/ ./templates
COPY web/static/ ./static

# Instalăm dependențele
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expunem portul 80 al containerului
EXPOSE 80

# Setăm comanda de rulare a serverului
CMD ["python", "app.py"]
