import random
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import numpy


class SimpleGenetics(ABC):
    def __init__(self, population_size=100, children_count=6, to_retain=30, mutation_prob=0.01, goal=6000):
        self._population_size = population_size
        self._children_count = children_count
        self._to_retain = to_retain
        self._mutation_prob = mutation_prob
        self._goal = goal
        self._population = []

    def run(self, max_generations=1000) -> (int, int):
        self._populate()
        population_fitness = self._fitness()
        generation = 1
        generation_list = []
        fitness_list = []
        while population_fitness < 1 and generation < max_generations:
            males, females = self._select()
            children = self._breed(males, females)
            self._mutate(children)
            self._population = males + females + children
            population_fitness = self._fitness()

            generation_list.append(generation)
            fitness_list.append(population_fitness)

            generation += 1


        x_points = numpy.array(generation_list)
        y_points = numpy.array(fitness_list)
        plt.plot(x_points, y_points)
        plt.show()
        return population_fitness, generation

    def _select(self):
        to_retain_by_sex = self._to_retain // 2
        self._sort_population()
        members_per_sex = len(self._population) // 2
        females = self._population[:members_per_sex]
        males = self._population[members_per_sex:]
        females = females[-to_retain_by_sex:]
        males = males[-to_retain_by_sex:]
        return males, females

    def _breed(self, males: list, females: list) -> list:
        random.shuffle(males)
        random.shuffle(females)
        children = []

        for mal, fem in zip(males, females):
            for child in range(self._children_count):
                children.append(self._make_child(mal, fem))

        return children

    def _mutate(self, children: list):
        for index, child in enumerate(children):
            if random.random() < self._mutation_prob:
                children[index] = self._mutation(child)

    def __str__(self):
        return f"Population fitness: {self._fitness()}\nPopulation: {self._population}"

    @abstractmethod
    def _populate(self):
        pass

    @abstractmethod
    def _fitness(self):
        pass

    @abstractmethod
    def _make_child(self, male, female):
        pass

    @abstractmethod
    def _mutation(self, child):
        pass

    @abstractmethod
    def _sort_population(self):
        pass
