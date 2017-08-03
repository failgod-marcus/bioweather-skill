from flask import Flask, Response
from bs4 import BeautifulSoup
import urllib
import json

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
            "uid": "urn:uuid:1335c695-cfb8-4ebb-abbd-80da344efa6b",
            "updateDate": "2016-05-23T00:00:00.0Z",
            "titleText":"Biowetter",
            "mainText": "Biowetter wäre hier"
        }

    js = json.dumps(responseJSON)
    resp = Response(js, status=200, mimetype='application/json', charset="utf-8")

    return resp

if __name__ == '__main__':
    app.run()
