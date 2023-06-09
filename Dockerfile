FROM python:3.7-alpine
COPY . .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "scraper.py"]