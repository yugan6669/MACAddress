FROM python:3
WORKDIR /usr/src/app
COPY ./macaddress.py /usr/src/app/
RUN pip install requests
CMD ["python3","macaddress.py"]
