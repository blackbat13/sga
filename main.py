from sga import RabbitGenetics


rabbit_genetics = RabbitGenetics()
fitness, generation = rabbit_genetics.run()
print(f"Fitness: {fitness}, generation: {generation}")
print(rabbit_genetics)