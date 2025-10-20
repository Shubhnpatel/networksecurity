# --------------------------
# 1️⃣ Base image
# --------------------------
FROM python:3.10-slim

# --------------------------
# 2️⃣ Set working directory
# --------------------------
WORKDIR /app

# --------------------------
# 3️⃣ Copy only essential files
# --------------------------
COPY requirements.txt .
COPY . .

# --------------------------
# 4️⃣ Install dependencies
# --------------------------
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# (Optional) Install system-level deps (for MLflow or Mongo)
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# --------------------------
# 5️⃣ Expose port (if running an API)
# --------------------------
EXPOSE 5000

# --------------------------
# 6️⃣ Run your main script
# --------------------------
CMD ["python", "main.py"]
