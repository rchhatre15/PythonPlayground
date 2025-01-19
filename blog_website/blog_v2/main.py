from flask import Flask, render_template
import requests
import post

app = Flask(__name__)

post_lst = []
response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
for data in response.json():
    temp = post.Post(data['id'], data['title'], data['subtitle'], data['body'],)
    post_lst.append(temp)

@app.route('/')
def home():
    return render_template("index.html", lst=post_lst)

@app.route('/<id>')
def create_post(id):
    post = None
    for val in post_lst:
        if int(val.id) == int(id):
            post = val
            break
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
