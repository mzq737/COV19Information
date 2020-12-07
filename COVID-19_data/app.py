from flask import Flask
from flask import render_template
from flask import jsonify
import utils
import nltk
# nltk.download('punkt')

app = Flask(__name__)

@app.route('/time')
def get_time():
    return utils.get_time()

@app.route('/c1')
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({"confirmed":data[0], "dead":data[1], "recovered":data[2], "fatality_rate":"%.2f%%" % (data[3] * 100)})

@app.route('/c2')
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        res.append({"name":tup[0], "value":int(tup[1])})
    return jsonify({"data":res})

@app.route("/l1")
def get_l1_data():
    data = utils.get_l1_data()
    day,confirmed,recovered,dead = [],[],[],[]
    for a,b,c,d in data[0:]:
        day.append(a.strftime("%m-%d")) #Convert datetime type
        confirmed.append(b)
        recovered.append(c)
        dead.append(d)
    return jsonify({"day":day, "confirmed": confirmed, "recovered": recovered, "dead": dead})

@app.route("/l2")
def get_l2_data():
    data = utils.get_l2_data()
    day, confirmed_add, dead_add = [], [], []
    for a, b, c in data[0:]:
        day.append(a.strftime("%m-%d"))
        confirmed_add.append(b)
        dead_add.append(c)
    return jsonify({"day": day, "confirmed_add": confirmed_add, "dead_add": dead_add})

@app.route("/r1")
def get_r1_data():
    data = utils.get_r1_data()
    state = []
    confirmed = []
    for k,v in data:
        state.append(k)
        confirmed.append(int(v))
    return jsonify({"state": state, "confirmed": confirmed})

@app.route("/r2")
def get_r2_data():
    data = utils.get_r2_data()
    sentences = nltk.sent_tokenize(str(data))
    nouns = []
    d = []
    for sentence in sentences:
        for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
            if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS' or pos == 'VBG' or pos == 'JJ'):
                nouns.append(word)
    nouns = list(set(nouns))
    # print(nouns)
    for w in nouns:
        d.append({"name": w, "value": 20000})
    # print(d)
    return jsonify({"kws": d})

@app.route('/')
def hello_world():
    return render_template("main.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
