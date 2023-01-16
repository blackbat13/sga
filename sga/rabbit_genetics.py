import random

from sga.simple_genetics import SimpleGenetics


class RabbitGenetics(SimpleGenetics):
    def __init__(self, min_weight=1000, max_weight=3000, mean_weight=1800, population_size=100, children_count=6,
                 to_retain=30, mutation_prob=0.01, goal=6000):
        super().__init__(population_size=population_size, children_count=children_count, to_retain=to_retain,
                         mutation_prob=mutation_prob, goal=goal, name="Rabbits")
        self._min_weight = min_weight
        self._max_weight = max_weight
        self._mean_weight = mean_weight

    def _populate(self):
        self._population = [int(random.triangular(self._min_weight, self._max_weight, self._mean_weight)) for i in
                            range(self._population_size)]

    def _fitness(self, el):
        return el

    def _make_child(self, male, female):
        return random.randint(female, male)

    def _mutation(self, child):
        return int(child * random.uniform(0.5, 1.2))

    def _sort_population(self):
        self._population = sorted(self._population)


if __name__ == "__main__":
    rabbit_genetics = RabbitGenetics()
    fitness, generation = rabbit_genetics.run()
    print(f"Fitness: {fitness}, generation: {generation}")
    print(rabbit_genetics)
