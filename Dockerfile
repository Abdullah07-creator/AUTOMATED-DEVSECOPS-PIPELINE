FROM python:3.11-slim

WORKDIR /app

# Optimize layer caching by installing dependencies first
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app/ .

# Expose container application port
EXPOSE 5000

# Non-root user setup for container security
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

CMD ["python", "app.py"]
