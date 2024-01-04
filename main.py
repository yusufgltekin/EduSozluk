from flask import Flask, render_template
import pandas as pd

app = Flask('app')


def getBaslik(path, sheetName):
    data = pd.read_excel(path, sheet_name=sheetName)
    basliklar = []
    for index, row in data.iterrows():
        baslikSozluk = {
            "id": row["id"],
            "baslik": row["baslik"],
            "yazilar": row["yazilar"].split(",")
        }
        basliklar.append(baslikSozluk)

    return basliklar

basliklar = getBaslik("basliklar.xlsx","Sayfa1")

@app.route('/')
def home_page():
  return render_template("ana_sayfa.html", basliklar=basliklar)


@app.route('/baslik/<baslik_id>')
def baslik_goster(baslik_id):
  baslik = ""
  yazilar = []
  for b in basliklar:
    if b["id"] == int(baslik_id):
      baslik = b["baslik"]
      yazilar = b["yazilar"]

  return render_template("baslik_icerik.html", baslik=baslik, yazilar=yazilar)



app.run(debug=True, host='0.0.0.0', port=5000)

