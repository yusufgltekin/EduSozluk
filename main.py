from flask import Flask, render_template

app = Flask('app')

basliklar = [{
    "id": 1,
    "baslik": "28 aralik python bayramı",
    "yazilar": ["yazi1", "yazi2", "yazi3"]
}, {
    "id": 2,
    "baslik": "ücret zamları",
    "yazilar": ["yazi4", "yazi5", "yazi6"]
}, {
    "id": 3,
    "baslik": "veri bilimi",
    "yazilar": ["yazi7", "yazi8", "yazi9"]
}, {
    "id": 4,
    "baslik": "yilbasi geliyor",
    "yazilar": ["yazi10", "yazi11", "yazi12"]
}, {
    "id": 5,
    "baslik": "2024 mesajları",
    "yazilar": ["yazi13", "yazi14", "yazi15"]
}]


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
