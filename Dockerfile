FROM python:3.10.6

COPY requirements.txt /temp/requirements.txt

RUN python3 -m venv venv

RUN #venv/Scripts/activate



RUN pip install --upgrade pip

RUN pip install -r /temp/requirements.txt

COPY . /.

WORKDIR /.

EXPOSE 8000

RUN adduser --disabled-password connect-user

USER connect-user