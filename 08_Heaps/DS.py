import numpy as np
n = [2, 5, 10, 30, 50, 100]#This is different sample size.
def generate_uniform():
    u = np.random.random()  # Uniform(0,1)
    x = 10 * u              # Transform to Uniform(0,10)
    return x

final_result = []

for i in n:
    result = []
    
    for _ in range(1000):
        count = 0
        
        for _ in range(i):
            
            count+= generate_uniform()
        result.append(count/i)
        
    final_result.append(result)

# The theoritical values of mean and var are.

population_mean = 5
population_variance = 100 / 12

# Calculate experimental mean and variance

for index in range(len(n)):
    
    experimental_mean = np.mean(final_result[index])
    
    experimental_variance = np.var(final_result[index])
    
    
    theoretical_mean = population_mean
    
    theoretical_variance = population_variance / n[index]
    
    
    print("Sample Size =", n[index])
    
    print("Experimental Mean =", experimental_mean)
    print("Theoretical Mean =", theoretical_mean)
    
    print("Experimental Variance =", experimental_variance)
    print("Theoretical Variance =", theoretical_variance)
    
    print()
    
    
    
import pandas as pd #For making the data table in organised manner.

data_table = []

for index in range(len(n)):
    
    experimental_mean = np.mean(final_result[index])
    experimental_variance = np.var(final_result[index])
    
    theoretical_mean = population_mean
    theoretical_variance = population_variance / n[index]
    
    data_table.append(([n[index],
        experimental_mean,
        theoretical_mean,
        experimental_variance,
        theoretical_variance
    ]))
    
    
df = pd.DataFrame(data_table,columns = ["Sample Size","Experimental Mean","Theoretical Mean","Experimental Variance",
        "Theoretical Variance" ])

pd.set_option('display.max_columns', None)
print(df)



import matplotlib.pyplot as plt #For Ploting the the graphs and the visual representation.


def normal_pdf(x, mean, std):
    
    return (1 / (std * np.sqrt(2 * np.pi))) * np.exp(
        -((x - mean) ** 2) / (2 * std ** 2)
    )


for index in range(len(n)):

    # Histogram of experimental sample means
    plt.hist(
        final_result[index],
        bins=30,
        density=True,
        alpha=0.6,
        edgecolor="black",
        label="Experimental"
    )

    
    # Theoretical standard deviation of X-bar
    theoretical_std = np.sqrt(population_variance / n[index])
    
    
    # Create x-values for the normal curve
    x = np.linspace(
        min(final_result[index]),
        max(final_result[index]),
        500
    )
    
    
    # Calculate theoretical normal PDF
    y = normal_pdf(
        x,
        population_mean,
        theoretical_std
    )
    
    
    # Overlay CLT normal curve
    plt.plot(
        x,
        y,
        linewidth=2,
        label="CLT Normal Distribution"
    )

    
    plt.title(f"Sampling Distribution of X̄ for n = {n[index]}")
    
    plt.xlabel("Sample Mean")
    
    plt.ylabel("Density")
    
    plt.legend()
    
    plt.show()
    
    
    
    
#----------------------------------------------------------------------------------------------------------------------
#let's do the Exponanational distribution.
    
n = [2, 5, 10, 30, 50, 100]


def generate_expo():
    u = np.random.random()  # Uniform(0,1)
    x = -np.log(1-u)              # Transform to expo(1)
    return x


final_result = []

for i in n:
    result = []
    
    for _ in range(1000):
        count = 0
        
        for _ in range(i):
            
            count+= generate_expo()
        result.append(count/i)
        
    final_result.append(result)

# The theoritical values of mean and var are.
# Theoretical population mean and variance
population_mean = 1
population_variance = 1

# Calculate experimental mean and variance

for index in range(len(n)):
    
    experimental_mean = np.mean(final_result[index])
    
    experimental_variance = np.var(final_result[index])
    
    
    theoretical_mean = population_mean
    
    theoretical_variance = population_variance / n[index]
    
    
    print("Sample Size =", n[index])
    
    print("Experimental Mean =", experimental_mean)
    print("Theoretical Mean =", theoretical_mean)
    
    print("Experimental Variance =", experimental_variance)
    print("Theoretical Variance =", theoretical_variance)
    
    print()
    
import pandas as pd

data_table = []

for index in range(len(n)):
    
    experimental_mean = np.mean(final_result[index])
    experimental_variance = np.var(final_result[index])
    
    theoretical_mean = population_mean
    theoretical_variance = population_variance / n[index]
    
    data_table.append(([n[index],
        experimental_mean,
        theoretical_mean,
        experimental_variance,
        theoretical_variance
    ]))
    
    
df = pd.DataFrame(data_table,columns = ["Sample Size","Experimental Mean","Theoretical Mean","Experimental Variance",
        "Theoretical Variance" ])
pd.set_option('display.max_columns', None)
print(df)


import matplotlib.pyplot as plt


def normal_pdf(x, mean, std):
    
    return (1 / (std * np.sqrt(2 * np.pi))) * np.exp(
        -((x - mean) ** 2) / (2 * std ** 2)
    )


for index in range(len(n)):

    # Histogram of experimental sample means
    plt.hist(
        final_result[index],
        bins=30,
        density=True,
        alpha=0.6,
        edgecolor="black",
        label="Experimental"
    )

    
    # Theoretical standard deviation of X-bar
    theoretical_std = np.sqrt(population_variance / n[index])
    
    
    # Create x-values for the normal curve
    x = np.linspace(
        min(final_result[index]),
        max(final_result[index]),
        500
    )
    
    
    # Calculate theoretical normal PDF
    y = normal_pdf(
        x,
        population_mean,
        theoretical_std
    )
    
    
    # Overlay CLT normal curve
    plt.plot(
        x,
        y,
        linewidth=2,
        label="CLT Normal Distribution"
    )

    
    plt.title(f"Sampling Distribution of X̄ for n = {n[index]}")
    
    plt.xlabel("Sample Mean")
    
    plt.ylabel("Density")
    
    plt.legend()
    
    plt.show()
    
    
    
    
#----------------------------------------------------------------------------------------------------------------------
    
#let's try the Normal distridution.
n = [2, 5, 10, 30, 50, 100]
   

def generate_normal():
    
    u1 = np.random.random()
    u2 = np.random.random()
    
    # Box-Muller transformation
    z = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
    
    # Transform N(0,1) into N(5,4)
    x = 5 + 2 * z
    return x

final_result = []

for i in n:
    result = []
    
    for _ in range(1000):
        count = 0
        
        for _ in range(i):
            
            count+= generate_normal()
        result.append(count/i)
        
    final_result.append(result)

# The theoritical values of mean and var are.

population_mean = 5
population_variance = 4

# Calculate experimental mean and variance

for index in range(len(n)):
    
    experimental_mean = np.mean(final_result[index])
    
    experimental_variance = np.var(final_result[index])
    
    
    theoretical_mean = population_mean
    
    theoretical_variance = population_variance / n[index]
    
    
    print("Sample Size =", n[index])
    
    print("Experimental Mean =", experimental_mean)
    print("Theoretical Mean =", theoretical_mean)
    
    print("Experimental Variance =", experimental_variance)
    print("Theoretical Variance =", theoretical_variance)
    
    print()
  
  
import pandas as pd

data_table = []

for index in range(len(n)):
    
    experimental_mean = np.mean(final_result[index])
    experimental_variance = np.var(final_result[index])
    
    theoretical_mean = population_mean
    theoretical_variance = population_variance / n[index]
    
    data_table.append(([n[index],
        experimental_mean,
        theoretical_mean,
        experimental_variance,
        theoretical_variance
    ]))
    
    
df = pd.DataFrame(data_table,columns = ["Sample Size","Experimental Mean","Theoretical Mean","Experimental Variance",
        "Theoretical Variance" ])
pd.set_option('display.max_columns', None)
print(df)


import matplotlib.pyplot as plt


def normal_pdf(x, mean, std):
    
    return (1 / (std * np.sqrt(2 * np.pi))) * np.exp(
        -((x - mean) ** 2) / (2 * std ** 2)
    )


for index in range(len(n)):

    # Histogram of experimental sample means
    plt.hist(
        final_result[index],
        bins=30,
        density=True,
        alpha=0.6,
        edgecolor="black",
        label="Experimental"
    )

    
    # Theoretical standard deviation of X-bar
    theoretical_std = np.sqrt(population_variance / n[index])
    
    
    # Create x-values for the normal curve
    x = np.linspace(
        min(final_result[index]),
        max(final_result[index]),
        500
    )
    
    
    # Calculate theoretical normal PDF
    y = normal_pdf(
        x,
        population_mean,
        theoretical_std
    )
    
    
    # Overlay CLT normal curve
    plt.plot(
        x,
        y,
        linewidth=2,
        label="CLT Normal Distribution"
    )

    
    plt.title(
    f"Sampling Distribution of X̄ for N(5,4), n = {n[index]}")

    
    plt.xlabel("Sample Mean")
    
    plt.ylabel("Density")
    
    plt.legend()
    
    plt.show()
    
    
    
    