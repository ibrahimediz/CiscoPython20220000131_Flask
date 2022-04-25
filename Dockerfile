FROM python:slim
RUN useradd bloguser

WORKDIR /home/bloguser

COPY requirements.txt requirements.txt
RUN python -m venv env
RUN env/bin/pip install -r requirements.txt
RUN env/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY runbabyrun.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP runbabyrun.py

RUN chown -R bloguser:bloguser ./
USER bloguser

EXPOSE 5000
ENTRYPOINT [ "./boot.sh" ]