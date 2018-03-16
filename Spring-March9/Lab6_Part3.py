#!/usr/bin/env python 

import numpy as np
import matplotlib.pyplot as plt

#Part III: Vary the allele frequency, keeping population = 100. Show allele frequency vs generation fixation. 


def wright_fisher(population, a_count):
    return np.random.binomial(n=2 * population, p=float(a_count)/(2 * population))


def update_count(population, a_freq = 0.5): 
    a_count = int(2 * population * a_freq)
    b_count = int(2 * population - a_count) 

    count = 0 
    while a_count != 0 and b_count != 0: 
        a_count = wright_fisher(population, a_count) 
        b_count = int(2 * population - a_count)

        count += 1

    return count 



if __name__ == "__main__":
    population = 100
    frequencies = np.linspace(0.05, 0.95, num=100) #Cannot be 0 or 1 or will be fixed. Creates a range of frequency weights. 

    avg_iterations = []
    freq_variance = []
    freq_std = []


    for freq in frequencies:
        iterations = []
        for i in range(100):
            iterations.append(update_count(population, a_freq=freq)) #Set different frequencies

        avg_iterations.append(np.mean(iterations))
        freq_variance.append(np.var(iterations))
        freq_std.append(np.std(iterations))


        # print avg_iterations
        # print freq_variance


### I could not figure out how to plot the variances, so I plotted the standard deviations instead. I tried plotting the variances, and it just turned the graph into a giant blob of color. 
plt.figure()
# plt.errorbar(frequencies, avg_iterations, yerr= freq_std, color='purple')
plt.scatter(frequencies, avg_iterations, color='purple')
plt.xlabel('Allele Frequency')
plt.ylabel('Time to Fixation')
plt.title('Allele Frequency vs Fixation', size='16')
plt.savefig("part3_version2.png")
plt.close()
