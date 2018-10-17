FROM python:3
ADD tryme.py /
RUN pip install pystrich
CMD [ "python", "./tryme.py" ]