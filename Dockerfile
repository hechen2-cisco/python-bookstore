FROM python:alpine
EXPOSE 5000
WORKDIR /project
COPY . /project
RUN pip install -r requirements.txt
CMD ["python","app.py"]