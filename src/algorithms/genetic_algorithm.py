import random

from src.models.box import Box
from src.models.container import Container
from src.algorithms.extreme_point_algorithm import ExtremePointAlgorithm


class GeneticAlgorithm:
    def __init__(
        self,
        container: Container,
        boxes: list[Box],
        population_size: int = 20,
        generations: int = 50,
        mutation_rate: float = 0.1
    ):
        self.container = container
        self.boxes = boxes
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def create_chromosome(self):
        chromosome = self.boxes.copy()
        random.shuffle(chromosome)
        return chromosome

    def create_population(self):
        population = [
            self.create_chromosome()
            for _ in range(self.population_size)
        ]

        return population

    def evaluate_fitness(self, chromosome):
        # Create a fresh empty container for this chromosome
        test_container = Container(
            length=self.container.length,
            width=self.container.width,
            height=self.container.height
        )

        # Use Extreme Point as the placement decoder
        decoder = ExtremePointAlgorithm(test_container)

        total_packed_volume = 0

        # Follow the chromosome order exactly
        for box in chromosome:
            if decoder.place_box(box):
                total_packed_volume += box.volume()

        return total_packed_volume

    def tournament_selection(self, population):
        # Randomly choose two chromosomes
        chromosome1, chromosome2 = random.sample(population, 2)

        # Calculate their fitness
        fitness1 = self.evaluate_fitness(chromosome1)
        fitness2 = self.evaluate_fitness(chromosome2)

        # Return the chromosome with the higher fitness
        if fitness1 >= fitness2:
            return chromosome1

        return chromosome2

    def order_crossover(self, parent1, parent2):
        size = len(parent1)

        # Randomly choose two crossover points
        start, end = sorted(random.sample(range(size), 2))

        # Create an empty child
        child = [None] * size

        # Copy a section from parent1 into the child
        child[start:end + 1] = parent1[start:end + 1]

        # Get boxes from parent2 that are not already in the child
        remaining_boxes = [
            box
            for box in parent2
            if box not in child
        ]

        # Fill the empty positions
        remaining_index = 0

        for i in range(size):
            if child[i] is None:
                child[i] = remaining_boxes[remaining_index]
                remaining_index += 1

        return child

    def mutate(self, chromosome):
        mutated = chromosome.copy()

        if random.random() < self.mutation_rate:
            i, j = random.sample(range(len(mutated)), 2)
            mutated[i], mutated[j] = mutated[j], mutated[i]

        return mutated

    def decode_chromosome(self, chromosome):
        # Create a fresh empty container
        test_container = Container(
            length=self.container.length,
            width=self.container.width,
            height=self.container.height
        )

        decoder = ExtremePointAlgorithm(test_container)

        packed_boxes = []
        unpacked_boxes = []

        # Follow chromosome order exactly
        for box in chromosome:
            if decoder.place_box(box):
                packed_boxes.append(box)
            else:
                unpacked_boxes.append(box)

        placements = test_container.placements

        return packed_boxes, unpacked_boxes, placements

    def run(self):
        population = self.create_population()

        for generation in range(self.generations):
            # Sort population from best fitness to worst
            population = sorted(
                population,
                key=self.evaluate_fitness,
                reverse=True
            )

            # Elitism: keep the best chromosome unchanged
            new_population = [population[0]]

            # Fill the rest of the new population
            while len(new_population) < self.population_size:
                parent1 = self.tournament_selection(population)
                parent2 = self.tournament_selection(population)

                child = self.order_crossover(parent1, parent2)
                child = self.mutate(child)

                new_population.append(child)

            population = new_population

        # Find the best chromosome after all generations
        best_chromosome = max(
            population,
            key=self.evaluate_fitness
        )

        best_fitness = self.evaluate_fitness(best_chromosome)

        packed_boxes, unpacked_boxes, placements = (
            self.decode_chromosome(best_chromosome)
        )

        return (
            best_chromosome,
            best_fitness,
            packed_boxes,
            unpacked_boxes,
            placements
        )