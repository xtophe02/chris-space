# frontend/Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY main.py /app
COPY templates /app/templates
COPY static /app/static

RUN pip install fastapi uvicorn Jinja2

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
