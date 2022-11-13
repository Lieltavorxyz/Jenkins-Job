FROM python
WORKDIR /app
COPY . .
RUN "pip3 install -r requirments.txt"
CMD [ "python3", "http_e.py" ]