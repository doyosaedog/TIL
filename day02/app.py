from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# 127.0.0.1:5000/ssafy 입력했을때 
# hello ssafy 를 반환하는 함수 만들기
@app.route("/ssafy")
def ssafy():
    return "hello,ssafy! 오"
























if __name__ == '__main__':
    app.run(debug=True)