FROM python:3.12.4-bookworm
COPY . .
RUN pip install -r requirements.txt
CMD ["python","src/main.py"]