from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<luku>') #localhost:3000/alkuluku tai 127.0.0.1:3000/alkuluku
def alkuluku(luku):
    # args = request.args
    luku = int(luku)
    alkuluku = True

    for i in range(2, luku - 1):
        if luku % i == 0:
            alkuluku = False

    vastaus = {
        'Number': luku,
        'isPrime': alkuluku
    }

    return vastaus

if __name__ == "__main__":
    app.run(use_reloader=True, host='localhost', port=3000) #'localhost' = 127.0.0.1