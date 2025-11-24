FROM python:3.11-slim

WORKDIR /app

RUN python -m pip install --no-cache-dir flask requests

COPY app.py .

EXPOSE 5001

CMD ["python", "app.py"]
