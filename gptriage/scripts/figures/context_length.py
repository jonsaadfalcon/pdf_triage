"""
Generate context length figure for GPTriage paper.
"""
import matplotlib.pyplot as plt
import statistics
import random

# fill in the below with actual data
DUMMY_DOCUMENTS = [random.randint(100, 20000) for _ in range(100)]
DUMMY_CONTEXTS  = [2000, 4000, 8000, 16000]
DUMMY_SCORES_R  = [50, 60, 67, 75]
DUMMY_SCORES_T  = [25, 32, 56, 80]
DUMMY_GPTRIAGE  = 82.0


if __name__ == '__main__':
    quantiles = statistics.quantiles(DUMMY_DOCUMENTS, n=4)

    # plot the retrieval model performance
    plt.plot(
        DUMMY_CONTEXTS,
        DUMMY_SCORES_R,
    )

    # plot the truncation model performance
    plt.plot(
        DUMMY_CONTEXTS,
        DUMMY_SCORES_T
    )

    # plot the document length quantiles as vertical lines
    plt.vlines(quantiles, 0, 100)

    # plot the triage performance


    # styling

    # plt.show()
    plt.savefig('scripts/outputs/context_length.png')