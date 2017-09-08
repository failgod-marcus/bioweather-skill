from flask import Flask, Response
from bs4 import BeautifulSoup
import urllib
import json
import uuid
import datetime
import re

app = Flask(__name__)

@app.route('/api/v1.0/biowetter')
def biowetter():
    ndrFile = urllib.request.urlopen("https://www.ndr.de/nachrichten/wetter/biowetter101.html")
    ndrHtml = ndrFile.read()
    ndrFile.close()

    soup = BeautifulSoup(ndrHtml, "html.parser")
    completeText = soup.find("div", {"class": "modulepadding copytext"})
    speech_text = completeText.text
    speech_text = speech_text.replace('Biowetter', '')
    speech_text = speech_text.replace('Das Wetter zu jeder vollen Stunde auf NDR 2', '')

    # Add whitespace between to sentences
    speech_text = re.sub(r'([A-z])(\.)([A-z])', r'\1\2 \3', speech_text)

    #remove newlines and add period
    speech_text = re.sub(r'\n+', '. ', speech_text).rstrip()

    responseJSON = {
            "uid" : str(uuid.uuid1()),
            "updateDate" : str(datetime.datetime.utcnow().replace(microsecond=0).isoformat())+'.0Z', #bad hack because i don't know better
            "titleText":"Biowetter",
            "mainText": speech_text
        }

    js = json.dumps(responseJSON)
    response = app.response_class(response=js, status=200, mimetype='application/json')
    return response

if __name__ == '__main__':
    app.run()
