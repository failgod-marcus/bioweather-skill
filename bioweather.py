from flask import Flask, jsonify
from bs4 import BeautifulSoup
import urllib

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
            "uid" : "testblafasel",
            "titleText":"Biowetter",
            "mainText": speech_text
        }

    return jsonify(responseJSON)

if __name__ == '__main__':
    app.run()
