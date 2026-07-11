class PositionManager:

    def __init__(self):

        self.positions = []

    def add(self, signal):

        self.positions.append(signal)

    def remove(self, signal):

        if signal in self.positions:
            self.positions.remove(signal)

    def open_positions(self):

        return self.positions

    def count(self):

        return len(self.positions)