FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /prevencao_ml
ADD . /prevencao_ml 
EXPOSE 8000:8000
RUN pip install -r requirements.txt
RUN python3 prevencao_ml/manage.py migrate
RUN [ "python3", "prevencao_ml/manage.py", "runserver", "0.0.0.0:8000"]

