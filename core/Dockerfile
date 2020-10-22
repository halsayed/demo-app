FROM ubuntu:focal

## install gevent
#RUN apk add --no-cache --virtual .build-deps \
RUN apt-get update -y
RUN apt-get install -y \
    python3-dev \
    python3-pip \
    gcc  \
    unixodbc-dev \
    curl

# install mssql drivers
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN PATH="$PATH:/opt/mssql-tools/bin"
RUN export PATH
COPY odbc_dsn.ini ./
RUN odbcinst -i -s -f $PWD/odbc_dsn.ini -l
# application folder
RUN mkdir /app
WORKDIR /app

# python requirements
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

# application scripts
COPY *.py /app/
COPY templates /app/templates
COPY static /app/static

EXPOSE 5000
ENTRYPOINT ["python3", "-u"]
CMD ["/app/wsgi.py"]
