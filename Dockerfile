# Use official Python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port (Flask default is 5000, but gunicorn uses 8000)
EXPOSE 8000

# Run using gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "run:app"]
