class Averager:
    def __init__(self) -> None:
        self.series: list = []

    def __call__(self, value) -> float:
        self.series.append(value)
        total = sum(self.series)
        return total / len(self.series)

    def __repr__(self) -> str:
        total = sum(self.series)
        total = total / len(self.series)
        return f'{total}'


if __name__ == '__main__':
    avg = Averager()
    for i in range(10):
        avg(i)
        print(avg)
    print(avg)
