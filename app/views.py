from flask import Flask, jsonify, abort, request, render_template

from app import app

super_peers = []

@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def index():
	return render_template('index.html', response = super_peers)


@app.route('/speers', methods=['GET'])
def get_SPeers():
    return jsonify({'Super Peers': super_peers})

@app.route('/speers/<int:id>', methods=['GET'])
def get_SPeer(id):
    peer = [peer for peer in super_peers if peer['id'] == id]
    if len(peer) == 0:
        abort(404)
    return jsonify({'task': peer[0]})


@app.route('/speers', methods=['POST'])
def put_SPeers():
	if not request.form["ip"] or not request.form["port"]:
		abort(400)
	if len(super_peers)==0:
		id = 1
	else:
		id = super_peers[-1]['id'] + 1
	
	peer = {
	    'id': id,
	    'ip': request.form['ip'],
	    'port': int(request.form['port']),
    }
	super_peers.append(peer)
	return render_template('index.html', response = super_peers), 201



#@app.route('/speers', methods=['POST'])
#def put_SPeers():
    #if not request.json or not 'ip' or not 'port' in request.json:
    #    abort(400)
    #peer = {
    #    'id': super_peers[-1]['id'] + 1,
    #    'ip': request.json['ip'],
    #    'port': request.json.get('port'),
    #}
    #super_peers.append(peer)
    #return jsonify({'Super Peer': peer}), 201

@app.route('/speers', methods=['DELETE'])
def delete_peers():
    del super_peers[:]
    return jsonify({'result': True})