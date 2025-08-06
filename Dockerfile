FROM python:3.10-slim
WORKDIR /app
COPY publisher.py .
RUN pip install requests
CMD ["python", "publisher.py"]
