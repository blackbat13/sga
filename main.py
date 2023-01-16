from sga import RabbitGenetics, WarriorGenetics


# rabbit_genetics = RabbitGenetics()
# fitness, generation = rabbit_genetics.run()
# print(f"Fitness: {fitness}, generation: {generation}")
# print(rabbit_genetics)

warrior_genetics = WarriorGenetics()
fitness, generation = warrior_genetics.run()
print(f"Fitness: {fitness}, generation: {generation}")
print(warrior_genetics)