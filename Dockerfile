FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    binutils && \
    apt-get clean

WORKDIR /app

ARG EXCLUDE_FOLDERS=$EXCLUDE_FOLDERS

COPY . /app/

RUN chmod +x /app/list.sh && \
    sed -i 's/\r$//' /app/list.sh && \
    bash /app/list.sh

RUN python3 -m venv .venv
RUN . /app/.venv/bin/activate && pip install --no-cache-dir -r requirements.txt

SHELL ["/bin/bash", "-c"]

RUN . /app/.venv/bin/activate && python3 mkdocs.py
RUN ls -R /app/docs >> /app/file_list.txt

CMD ["/app/.venv/bin/mkdocs", "build"]
