class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def add_score(self, points):
        self.score += points

    def __str__(self):
        return f"{self.name}: {self.score}"
    pass
print("test")