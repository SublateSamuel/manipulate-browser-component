FROM python:3.11
USER 0
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY --chown=1000:1000 ./requirements.txt /app/requirements.txt
ENV PATH="/home/pybots/.local/bin:${PATH}"
RUN useradd -u 1000 -ms /bin/bash pybots
USER pybots
USER 1000
RUN python -m pip install --user --upgrade pip
RUN pip install --user -r requirements.txt
#ENTRYPOINT ["python", "main.py" ]
ENTRYPOINT ["tail", "-f", "/dev/null"]
