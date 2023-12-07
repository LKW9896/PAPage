from flask import Flask,render_template,url_for,send_file
app = Flask(__name__)

@app.route('/')
def findex():
    return render_template('index.html')

@app.route('/<page_name>.html')
def page(page_name):
    return render_template(f'{page_name}.html')

@app.route('/search_index.json')
def search():
    return send_file('static\search_index.json','')

@app.route('/images/<file_name>')
def image(file_name):
    return send_file(f'static\images\{file_name}','')

if __name__=='__main__':
    app.run(debug=True,threaded=True)