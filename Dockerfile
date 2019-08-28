FROM python:3.7.0


ENV WORKSPACE /Dev/Projects/
WORKDIR $WORKSPACE

RUN cd $WORKSPACE && \
    git clone https://github.com/bmdepesa/rpgbot && \
    cd rpgbot && \
    pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "rpgbot/rpgbot2.py" ]