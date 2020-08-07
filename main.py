import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request
from urllib.parse import urlparse
from Blockchain.blockchain import Blockchain 
import node1, node2
import subprocess
from argparse import ArgumentParser
import requests

def registerAllNodes(nodes):

	allNodes = {}
	urls = []
	for i in range(int(nodes)):
		urls.append(str(f"http://127.0.0.1:500{i}"))

	payload = {'nodes' : urls}
	print(payload)

	for i in range(int(nodes)):
		r = request.post(f"http://localhost:500{i}/nodes/register", data = payload)

def main():
	parser = ArgumentParser()
	parser.add_argument("--nodes")
	args = parser.parse_args()

	for i in range(int(args.nodes)+1):
		if i==0: continue
		subprocess.Popen(f"python node{i}.py", shell=True)
		time.sleep(10)
	registerAllNodes(args.nodes)



if __name__ == "__main__":
	main()