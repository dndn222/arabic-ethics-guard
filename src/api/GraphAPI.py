from flask import Flask, request, jsonify
from storage.GraphStore import GraphStore
from models.Node import Node
from models.Edge import Edge

app = Flask(__name__)
graph_store = GraphStore()

@app.route('/nodes', methods=['POST'])
def add_node():
    data = request.json
    node = Node(data['id'], data['label'], data.get('properties'))
    graph_store.add_node(node)
    return jsonify(node.to_dict()), 201

@app.route('/nodes/<node_id>', methods=['DELETE'])
def delete_node(node_id):
    graph_store.remove_node(node_id)
    return '', 204

@app.route('/edges', methods=['POST'])
def add_edge():
    data = request.json
    edge = Edge(data['id'], data['source'], data['target'], data['relation'], data.get('weight', 1.0))
    graph_store.add_edge(edge)
    return jsonify(edge.to_dict()), 201

@app.route('/edges/<edge_id>', methods=['DELETE'])
def delete_edge(edge_id):
    graph_store.remove_edge(edge_id)
    return '', 204

@app.route('/subgraph', methods=['POST'])
def get_subgraph():
    data = request.json
    nodes, edges = graph_store.get_subgraph(data['node_ids'])
    return jsonify({
        'nodes': {nid: node.to_dict() for nid, node in nodes.items()},
        'edges': {eid: edge.to_dict() for eid, edge in edges.items()}
    }), 200

@app.route('/version', methods=['GET'])
def version_graph():
    version = graph_store.version_graph()
    return jsonify(version), 200

if __name__ == '__main__':
    app.run(debug=True)