"""
Generate the satisfiability figure (main results) for GPTriage paper.
"""
import matplotlib.pyplot as plt
import statistics
import random

# fill in the below with actual data
categories = [
    f"Category {n}" for n in range(1, 11)
] + ["Overall"]

DUMMY_TRIAGE_RESULTS = [random.randint(40, 100) for _ in range(10)]
DUMMY_TRIAGE_RESULTS += [statistics.mean(DUMMY_TRIAGE_RESULTS)]

DUMMY_RETRIEVAL_RESULTS = [random.randint(20, 90) for _ in range(10)]
DUMMY_RETRIEVAL_RESULTS += [statistics.mean(DUMMY_RETRIEVAL_RESULTS)]

if __name__ == '__main__':
    plt.bar(categories, DUMMY_RETRIEVAL_RESULTS, align='edge', width=0.2)
    plt.bar(categories, DUMMY_TRIAGE_RESULTS, align='center', width=0.2)

    # styling

    # plt.show()
    plt.savefig('scripts/outputs/satisfiability.png')