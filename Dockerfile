# 1. Python 3.12 ka base image use karein (Kyunki Django 6.0 ko yehi chahiye)
FROM python:3.12-slim

# 2. Container ke andar app ka folder banayein
WORKDIR /app

# 3. requirements.txt copy karein
COPY requirements.txt .

# 4. Saari libraries install karein
RUN pip install --no-cache-dir -r requirements.txt

# 5. Apne project ka saara code container mein copy karein
COPY . .

# 6. Django ka port expose karein
EXPOSE 8000

# 7. Django server run karne ki command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]