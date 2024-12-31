FROM python:3.11-slim

WORKDIR /app

# Only copy the requirement file.  Notes: /app/: workdir
COPY requirements.txt /app/

#  Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining files
COPY . /app

EXPOSE 5000

CMD ["gunicorn", "app.main:app", "-b", "0.0.0.0:5000"]