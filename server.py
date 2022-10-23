from flask import Flask, render_template
app = Flask(__name__)


# When a user visits http://localhost:5000/play, 
# have it render three beautiful looking blue boxes. 
# Please use a template to render this.
@app.route('/play')
def level_one():
    return render_template("index.html",num=3,color="blue")

# When a user visits localhost:5000/play/(x), 
# have it display the beautiful looking blue boxes x times.
@app.route('/play/<int:num>')
def level_two(num):
    return render_template("index.html", num=num, color="blue")

# When a user visits localhost:5000/play/(x)/(color), 
# have it display beautiful looking boxes x times, 
# but this time where the boxes appear in (color).
@app.route('/play/<int:num>/<color>')
def level_three(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)