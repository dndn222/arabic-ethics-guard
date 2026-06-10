class Edge:
    def __init__(self, id, source, target, relation, weight=1.0):
        self.id = id
        self.source = source
        self.target = target
        self.relation = relation
        self.weight = weight

    def to_dict(self):
        return {
            "id": self.id,
            "source": self.source,
            "target": self.target,
            "relation": self.relation,
            "weight": self.weight
        }