#!/usr/bin/env python 

import numpy as np
import matplotlib.pyplot as plt



#In Part I: given a starting allele frequency of 0.5 and population of 100, plot a histogram of fixation times for the A allele. 


#Need function that will update the A count from the Wright-Fisher model.
#Also need function that will use the Wright Fisher function and keep and update count to fixation.

def wright_fisher(population, a_count): 
	return np.random.binomial(n=2 * population, p=float(a_count)/ (2 * population)) #n=2N, p = probability of A (given as 0.5 in the problem)






def update_count(population, a_freq = 0.5): #Default a_freq = 0.5 (given in problem)
	a_count = int(2 * population * a_freq)
	b_count = int(2 * population - a_count) #Initialize these counts

	count = 0 #This is like a "generation" counter
	while a_count != 0 and b_count != 0: #As long as not fixation, do a count
		a_count = wright_fisher(population, a_count)
		b_count = int(2 * population - a_count)

		count += 1

    return count 

#it is running wright_fisher to repeatedly get new values for A and B. It does this until A or B is zero, then returns the number of times it did this



if __name__ == "__main__":
	fixation_generation = []
	for i in range (1000): #Run X trials 
		fixation_generation.append(update_count(100))




plt.figure()
plt.hist(fixation_generation, bins = 25, edgecolor='black', linewidth=1.2, color= 'purple')
plt.xlabel('Fixation Generation')
plt.ylabel('Trials')
plt.title('Time to Fixation: Allelle Freq 0.5, Population 100')
plt.savefig("part1.png")
plt.close()













