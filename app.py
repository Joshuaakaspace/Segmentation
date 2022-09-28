from flask import Flask, render_template
import config
import requests
import json

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)

headers = {'authorization': 'Bearer {}'.format(app.config['SECRET_KEY']),'content-type':'application/json'}    


@app.route('/')
def index():
    return render_template('index.html', **locals())
    

@app.route('/use')
def users():
    url = 'https://api.airtable.com/v0/appkrs0NZt62fVBPh/Segment?maxRecords=3&view=Grid%20view'
    r = requests.get(url, headers=headers)
    result = json.loads(r.text)
    
    
    
    
    return render_template('use.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)

