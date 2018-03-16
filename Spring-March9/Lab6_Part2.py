#!/usr/bin/env python 

import numpy as np
import matplotlib.pyplot as plt

#Part II: Vary population size and monitor the fixation time vs N. Allele frequency still 0.5.


def wright_fisher(population, a_count):
	return np.random.binomial(n=2 * population, p=float(a_count)/(2 * population))


def update_count(population, a_freq = 0.5): #Default a_freq = 0.5 (given in problem)
	a_count = int(2 * population * a_freq)
	b_count = int(2 * population - a_count) 

	count = 0 #This is like a "generation" counter
	while a_count != 0 and b_count != 0: #As long as not fixation, do a count
		a_count = wright_fisher(population, a_count) #Update A and B counts
		b_count = int(2 * population - a_count)

		count += 1

	return count 


if __name__ == "__main__":
	fixation_generation = []

	population_range = np.logspace(2,6, num=25) #Making a spread of populations to sample from in log space since the range is so big. Too big for linear space.

	for pop in population_range: #Run through all the generated population values
		fixation_generation.append(update_count(pop))
		






	plt.figure()
	plt.plot(population_range, fixation_generation, color='purple')
	plt.xlabel('Population')
	plt.ylabel('Fixation Generation')
	plt.title('Time to Fixation: Allelle Freq 0.5, Variable Population')
	plt.savefig("part2.png")
	plt.close()













