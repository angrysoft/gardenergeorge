#!/usr/bin/python3

import os
import json
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import Response
from utils import getPlaceDetails
from utils import verifyCaptcha
from utils import SendEmail
from utils import dictToString

app = Flask(__name__)


@app.route('/')
@app.route('/about')
def index():
    return render_template('index.html')


@app.route('/lawncare')
def lawncare():
    return render_template('lawncare.html')


@app.route('/maintenance')
def maintenance():
    return render_template('maintenance.html')


@app.route('/gutter')
def gutter():
    return render_template('gutter.html')


@app.route('/partners')
def partners():
    return render_template('partners.html', partners=partners.get('partners'))


@app.route('/freequote')
def freequote():
    return render_template('freequote.html')


@app.route('/mail', methods=['GET', 'POST'])
def mail():
    if request.method == 'GET':
        return request.args.get('status', 'ooops something is wrong')
    elif request.method == 'POST':
        form = request.form.copy()
        form['msg'] = request.form.get('msg').replace('\n', '<br>')
        # TODO: Testing mail form
        return render_template('mail.html', mail=form)

        if not verifyCaptcha(config.get('captcha'), request.form.get('g-recaptcha-response')):
            return redirect('/mail?status={}'.format('spam'))

        s = SendEmail(config.get('server'),
                      config.get('user'),
                      config.get('password'),
                      config.get('port', '25'),
                      config.get('encryption'))
        s.addAddrTo(config.get('sendto'))
        s.addAddrFrom(config.get('from'))
        s.addTextContent(dictToString(request.form))
        s.addHtmlContent(render_template('mail.html', mail=request.form))
        s.addSubject('Message From GardnerGeorge.ie')
        try:
            err = s.send()
        except:
            err = True
        status = 'ok'
        return redirect('/mail?status={}'.format(status))


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html', reviews=getPlaceDetails(config.get('placeid'),
                                                                   config.get('apiKey')))


@app.route('/photos/<dir>')
def photos(directory):
    allowed = ['lawncare', 'gardenmaintenance', 'offer']
    ret = list()
    if directory in allowed:
        for x in os.listdir(os.path.join('media', directory)):
            if x.startswith('.'):
                continue
            ret.append(os.path.join('/media', directory, x))
    return json.dumps(ret)


@app.route('/sitemap.txt')
def sitemap():
    links = list()
    for link in app.url_map.iter_rules():
        if 'GET' in link.methods and not link.arguments and link.endpoint is not 'index':
            links.append(f'{request.host_url}{link.endpoint}')

    resp = Response(response='\n'.join(links), status=200, mimetype="text/plain")
    resp.headers["Content-Type"] = "text/plain; charset=utf-8"
    return resp


with open('config/config.json') as cfile:
    config = json.load(cfile)

with open('config/partners.json') as pfile:
    partners = json.load(pfile)

if __name__ == '__main__':
    app.run()
