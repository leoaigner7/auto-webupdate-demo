FROM python:3.11-slim

# install curl (needed for healthcheck)
RUN apt-get update && apt-get install -y curl

WORKDIR /app
COPY ./app /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080

HEALTHCHECK --interval=15s --timeout=5s --retries=4 \
  CMD curl -f http://0.0.0.0:8080/health || exit 1



CMD ["python", "main.py"]

