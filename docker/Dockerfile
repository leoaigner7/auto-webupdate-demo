FROM python:3.11-slim

WORKDIR /app
COPY ./app /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080

HEALTHCHECK --interval=15s --timeout=3s --retries=4 CMD curl -fsS http://127.0.0.1:8080/health || exit 1



CMD ["python", "main.py"]

