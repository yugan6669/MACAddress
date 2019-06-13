FROM python:3
RUN mkdir -p /usr/share/macapp
WORKDIR /usr/share/macapp                                                                                                                                                                       
COPY ./macaddress.py /usr/share/macapp
ENTRYPOINT ["python3", "macaddress.py"]

