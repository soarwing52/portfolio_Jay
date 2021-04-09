FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /jay_profolio
COPY requirements.txt /jay_profolio/
RUN pip install -r requirements.txt
COPY . /jay_profolio/

#RUN python3 manage.py migrate
#RUN python manage.py loaddata datadump.json