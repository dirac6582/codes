import json
from flask import Flask, jsonify, request, redirect
from flask_talisman import Talisman
import requests


global user
app = Flask(__name__)
Talisman(app)

# 
file = open('./data.json')
data = json.load(file)
print(data)

@app.route('/api/v1/data',methods=['GET'])
# return json data
def hello():
    return data


@app.route('/install/slack/slurm',methods=['GET'])
# 
def install_slack():
    global user
    # get user from inquery
    # http://127.0.0.1:5000/install/slack/slurm?user=amano
    user = request.args['user']
    # redirect to slack-app install page
    return redirect('https://slack.com/oauth/v2/authorize?client_id=165336660452.2879968029619&scope=incoming-webhook&user_scope=')
# https://127.0.0.1:5000/api/v1/slack
@app.route('/api/v1/slack', methods=['GET'])
# slack
# curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d 'code=165336660452.2874524940581.7f063609393790b4521a6f8c3e98b953f9425b2cb56df13b280fce4f69919c86&client_id=165336660452.2873960700565&client_secret=23dce85601894a8709213f8598d441f4' https://slack.com/api/oauth.v2.access
# install url
# https://slack.com/oauth/v2/authorize?client_id=165336660452.2873960700565&scope=incoming-webhook&user_scope=
def slack_oauth():
    if (request.method == 'GET'):
        global user
        # get code
        code = request.args['code']
        print("code is::", code)
        # define oauth_data dictionary
        oauth_data = dict()
        oauth_data['code'] = code
        # client_id/client_secret are fixed
        oauth_data['client_id'] = '165336660452.2879968029619'
        oauth_data['client_secret'] = '347675ac5739d1047ee2aae591d6e41e'
        # send oauth_data to slack api
        #Exchanging a temporary authorization code for an access token
        r = requests.post("https://slack.com/api/oauth.v2.access",data=oauth_data)
        print(r)
        r2 = r.json()
        #
        # add new item in data.json
        data['slack_slurm'][user]=r2
        json.dump(data,file)
        
        return 200, "Install successful for user " + user

    
@app.route('/api/v1/slurm', methods=['GET'])
def slurm():
    if (request.method == 'GET'):
        local_user = request.form.get("user")
        return jsonify(data['slack_slurm'][local_user])

if __name__ == '__main__':
    app.run(debug=True)
