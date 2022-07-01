from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

post_obj = []
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()
for i in all_posts:
    obj = Post(i["id"], i["title"], i["subtitle"], i["body"])
    post_obj.append(obj)

@app.route('/')
def get_blog():
    return render_template("index.html", posts=post_obj)

@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for i in post_obj:
        if i.id == index:
            requested_post = i
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
