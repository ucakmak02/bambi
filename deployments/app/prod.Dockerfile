FROM python:3.6-slim-stretch

# set defatul workdir as /app
WORKDIR /app

# copy source code to docker '/app'
COPY . .

# update docker container os
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y
#RUN apt-get install -y default-libmysqlclient-dev
# install requirements
#RUN pip install --upgrade pip
#RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN pip install email_validator

# production
RUN pip install gunicorn
CMD gunicorn -b 0.0.0.0:8880 -w 4 main:app
#CMD python main.py
