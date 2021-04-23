FROM node:14.1-alpine as react-app
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY front/package.json /usr/src/app
RUN npm install
COPY ./front/ /usr/src/app
RUN npm run build
FROM python:3.9-slim-buster as Darqube-back
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# https://serverfault.com/questions/949991/how-to-install-tzdata-on-a-ubuntu-docker-image
ENV DEBIAN_FRONTEND noninteractive
# OS dependencies
RUN apt update && apt install --no-install-recommends --no-install-suggests -y \

    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    gcc \
    htop
RUN pip3 install poetry


WORKDIR /app
# Copy only React Build into /nginx/html
COPY --from=react-app /usr/src/app/build /usr/share/nginx/html
# Copy only requirements to cache them in the Docker layer
COPY ./poetry.lock ./
COPY ./pyproject.toml ./
# App dependencies. We don't need virtual environment in Docker
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-dev
# Copy app files
COPY client-portal-python ./
COPY ./site.conf ./
COPY ./start.sh ./
# Nginx
RUN rm /etc/nginx/sites-enabled/* -f && ln -s /app/site.conf /etc/nginx/sites-enabled/
EXPOSE 80

RUN chmod +x ./main.py
RUN chmod +x ./start.sh
# Run
CMD ./start.sh
