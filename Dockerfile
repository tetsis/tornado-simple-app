FROM python:3

WORKDIR /usr/src/tornado-simple-app

RUN wget https://pypi.python.org/packages/cf/d1/3be271ae5eba9fb59df63c9891fdc7d8044b999e8ac145994cdbfd2ae66a/tornado-5.0.2.tar.gz
RUN tar xvzf tornado-5.0.2.tar.gz
RUN cd tornado-5.0.2 && python setup.py build
RUN cd tornado-5.0.2 && python setup.py install

COPY . .

CMD [ "python", "./server.py" ]
