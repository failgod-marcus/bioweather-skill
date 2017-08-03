from flask import Flask, Response
from bs4 import BeautifulSoup
import urllib
import json
import uuid
import datetime

app = Flask(__name__)

@app.route('/biowetter/api/v1.0/biowetter')
def biowetter():
    ndrFile = urllib.request.urlopen("https://www.ndr.de/nachrichten/wetter/biowetter101.html")
    ndrHtml = ndrFile.read()
    ndrFile.close()

    soup = BeautifulSoup(ndrHtml, "html5lib")
    completeText = soup.find("div", {"class": "modulepadding copytext"})
    speech_text = completeText.text

    responseJSON = {
            "uid" : str(uuid.uuid1()),
            #"uid" : "blafasel",
            "updateDate" : "2017-08-3T00:00:00.0Z", #str(datetime.datetime.now().isoformat()),
            "titleText":"Biowetter",
            "mainText": speech_text
        }

    js = json.dumps(responseJSON)
    response = app.response_class(response=js, status=200, mimetype='application/json')
    return response

if __name__ == '__main__':
    app.run()
