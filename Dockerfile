FROM python:3.8 as builder
MAINTAINER we684123
# for telegram_mark_all_read

WORKDIR /telegram_mark_all_read
COPY . .
RUN python -m pip install --upgrade pip \
    && pip install -r requirements.txt

FROM builder
WORKDIR /telegram_mark_all_read
CMD ["python","/telegram_mark_all_read/main.py"]
