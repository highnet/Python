# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

def frog_jump(numberOfPlatforms):
    currentPlatform = 0
    jumps = 0
    while(currentPlatform != numberOfPlatforms):
        target = np.random.randint(currentPlatform+1,numberOfPlatforms+1)
        currentPlatform = target
        jumps = jumps + 1
    return jumps


if __name__ == "__main__":
    max_platforms = 1000
    experiment_iterations = 100
    avg_data = []
    for i in range(1,max_platforms):
        raw_data = []
        for j in range(0,experiment_iterations):
            raw_data.append(frog_jump(i))
        avg_data.append(np.mean(raw_data))
    plt.plot(range(1,max_platforms),avg_data)
    plt.show()
