FROM python:3.11-slim

#It will use a folder named "app" in the container
WORKDIR /app

#Copy the contents of the current directory to "/app" in the container
# 「COPY . .」 have the same effect in this case
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "app.main:app", "-b", "0.0.0.0:5000"]