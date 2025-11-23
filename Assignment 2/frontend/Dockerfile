FROM python:3.11-slim

WORKDIR /app

RUN python -m pip install --no-cache-dir flask requests

COPY ["app.py", "templates", "./"]

EXPOSE 5000
    
CMD ["python", "app.py"]