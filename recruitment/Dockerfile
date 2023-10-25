FROM python:3.11-slim
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt --no-cache-dir
CMD ["gunicorn", "recruitment.wsgi:application", "--bind", "0:8000"]