import hashlib
import json
from textwrap import dedent
from time import sleep
from uuid import uuid4
from flask import Flask, jsonify, request
from urllib.parse import urlparse
from Blockchain.blockchain import Blockchain 
import node1, node2
import subprocess
from argparse import ArgumentParser
import requests
from User import user

def registerAllNodes(nodes):
	allNodes = {}
	urls = []
	for i in range(int(nodes)):
		urls.append(f"http://127.0.0.1:500{i}")

	payload = {"nodes" : urls}
	print(payload)

	for i in range(int(nodes)):
		r = requests.post(f"http://localhost:500{i}/nodes/register", json = payload)
		print(f"Response from server for {i} : {r.text}")

def assignNodes(nodes):
	userNode = {}
	for i in range(int(args.nodes)+1):
		if i==0: continue 
		name = input(f"Please enter the name for user at node {i} : ")
		aadhar = input(f"Please enter Aadhar card number for user at node {i} : ")
		tempUser = user.User(name, aadhar)
		userNode[tempUser] = i
	return userNode

parser = ArgumentParser()
parser.add_argument("--nodes")
args = parser.parse_args()

#Starting all the applications
for i in range(int(args.nodes)+1):
	if i==0: continue
	subprocess.Popen(f"python node{i}.py", shell=True)
	sleep(2)

#Registering all the nodes within each other
registerAllNodes(args.nodes)

#Dictionary to mantain which user is consuming which node->
userNode = assignNodes(args.nodes)


#Running the app to be consumed by UI
app = Flask(__name__)
@app.route('/nodes', methods=['GET'])
def getAllNodes():
	pass




if __name__ == "__main__":
	app.run(host='127.0.0.1', port=4990)