import matplotlib.pyplot as plt
import random

DUMMY_TRIAL_RESULTS = [random.randint(40, 100) for _ in range(10)]

if __name__ == '__main__':
    plt.plot(range(1,11), DUMMY_TRIAL_RESULTS)

    # styling

    # plt.show()
    plt.savefig('scripts/outputs/trials.png')