FROM python:latest
RUN pip install github-clone
WORKDIR /app/
ARG REPO
ARG FOLDER
RUN ghclone ${REPO}
WORKDIR /app/${FOLDER}
CMD python -m http.server 7000