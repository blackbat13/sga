import random

from sga.simple_genetics import SimpleGenetics


class WarriorGenetics(SimpleGenetics):
    def __init__(self, min_stat=1, max_stat=30, mean_stat=10, population_size=100,
                 to_retain=50, mutation_prob=0.01, goal=100):
        super().__init__(population_size=population_size, children_count=2, to_retain=to_retain,
                         mutation_prob=mutation_prob, goal=goal, name="Warriors")
        self._min_stat = min_stat
        self._max_stat = max_stat
        self._mean_stat = mean_stat

    def _populate(self):
        self._population = [{
            "health": int(random.triangular(self._min_stat, self._max_stat, self._mean_stat)),
            "attack": int(random.triangular(self._min_stat, self._max_stat, self._mean_stat)),
            "defense": int(random.triangular(self._min_stat, self._max_stat, self._mean_stat)),
            "fitness": 0,
            } for i in range(self._population_size)]

    def _fitness(self, el):
        return el["fitness"]
    
    def _compute_fitness(self):
        for el in self._population:
            el["fitness"] = 0
            for war in self._population:
                if el["attack"] - war["defense"] <= 0:
                    continue
                elif war["attack"] - el["defense"] <= 0:
                    el["fitness"] += 1
                elif (war["health"] / (el["attack"] - war["defense"])) < (el["health"] / (war["attack"] - el["defense"])):
                    el["fitness"] += 1
                

    def _make_child(self, male, female):
        parents = [male, female]
        return {
            "health": random.choice(parents)["health"],
            "attack": random.choice(parents)["attack"],
            "defense": random.choice(parents)["defense"],
            "fitness": 0
            }

    def _mutation(self, child):
        return {
            "health": int(child["health"] * random.uniform(0.5, 1.2)),
            "attack": int(child["attack"] * random.uniform(0.5, 1.2)),
            "defense": int(child["defense"] * random.uniform(0.5, 1.2)),
            "fitness": 0
            }

    def _sort_population(self):
        self._population = sorted(self._population, key= lambda el: el["fitness"])


if __name__ == "__main__":
    warrior_genetics = WarriorGenetics()
    fitness, generation = warrior_genetics.run()
    print(f"Fitness: {fitness}, generation: {generation}")
    print(warrior_genetics)
