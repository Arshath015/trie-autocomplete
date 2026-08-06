class WeightedRanker:
    def __init__(self, weights):
        self.weights = weights

    def rank(self, matches):
        ranked_matches = []
        for match in matches:
            ranked_matches.append((match, self.weights[match]))
        ranked_matches.sort(key=lambda x: x[1], reverse=True)
        return ranked_matches
