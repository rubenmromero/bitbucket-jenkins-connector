#!/usr/bin/python

#
# Modules Import
#
import os, sys, socket, json, requests, cgi, cgitb, subprocess, yaml

#
# Jenkins Configuration Import
#
file = open('../conf/jenkins.yaml', 'r')
jenkins_conf = yaml.safe_load(file)
file.close()

jenkins_url = jenkins_conf['jenkins_url']
jenkins_user = jenkins_conf['jenkins_user']
jenkins_user_token = jenkins_conf['jenkins_user_token']

#
# Main
#

# For execution through HTTP request
print 'Content-Type: text/html\n'

# Get the params recieved through GET query string in the request
query_string = {}
if os.getenv('QUERY_STRING'):
    args = os.getenv('QUERY_STRING').split('&')

    for arg in args:
        t = arg.split('=')
        if len(t) > 1:
            key,value = arg.split('=')
            query_string[key] = value

project = query_string.get('project')
application = query_string.get('application')

# If project field has been recieved, get the project deployment configuration
if project:
    file = open('../conf/' + project + '.yaml', 'r')
    deploy_conf = yaml.safe_load(file)
    file.close()

    task_name = deploy_conf['task_name']
    task_token = deploy_conf['task_token']
    ci_envs = deploy_conf['ci_envs']
else:
    print "It has not been recieved any 'project' param through query string in the request"
    exit(1)

# Get the data recieved through POST request body from webhook
webhook_data = cgi.FieldStorage()
payload = webhook_data.value

# If webhook Payload has been recieved, decode the JSON and get the pushed branch
if (payload) and (os.getenv('REQUEST_METHOD') == 'POST'):
    payload = json.loads(payload)
    branch = payload['push']['changes'][0]['new']['name']
else:
    print "The Payload sent from Bitbucket webhook has not been recieved"
    exit(1)

# If the pushed branch is not included in ci_envs list, finish the script execution with exit code 1
if branch not in ci_envs:
    exit(1)

# Define the Jenkins task URL
task_url = jenkins_url + '/job/' + task_name + '/branch/' + branch + '/buildWithParameters'

# Execute the POST request to the corresponding Jenkins task
if application:
    task_request = requests.post(task_url, auth=(jenkins_user, jenkins_user_token), data={"token":task_token, "delay":"0sec", "application":application})
else:
    task_request = requests.post(task_url, auth=(jenkins_user, jenkins_user_token), data={"token":task_token, "delay":"0sec"})
