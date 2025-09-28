import matplotlib.pyplot as plt
import statistics
import math


def error_analysis(error: float, mean_n):
    """Make basic conclusions on found values"""
    if error > 1:
        print("It indicates that you took too small number of points in at least one of your π estimations.\n"
              "To improve the result, try to use n bigger than 100,000.")
    else:
        print(f"Since the error is small, it can be assumed that {mean_n} of points is enough for π estimation."
              f"\nNote, however, that choosing random points leads to possibility of different results with same input"
              f" data.")


def calculation(pi_values: list, n_values: list):
    """Compute mean of estimated π values and error percentage in comparison with actual π"""
    mean_pi = statistics.mean(pi_values)
    error = math.fabs((math.pi - mean_pi) / math.pi) * 100
    print(f'Average value of your π is {mean_pi}.')
    print(f'If actual value of π is {math.pi}, your percentage error is {error:.4f}%.')
    mean_n = int(statistics.mean(n_values))
    error_analysis(error, mean_n)


def visualize(pi_values: list):
    """Graph a boxplot of estimated π values range."""
    plt.figure(figsize=(3, 5), dpi=200)
    plt.boxplot(pi_values)
    plt.xlabel("Values of π")
    plt.title("Comparison of Estimated π Values")
    plt.xticks([])
    plt.grid()
    plt.show()


def check_estimations(estimations: list):
    """Check if the list is appropriate for comparison"""
    if len(estimations) <= 2:
        print('You need at least three estimated values of π to compare them.')
        return False
    else:
        return True


def compare(estimations: list):
    """Make a range of estimated π values and visualize it."""
    pi_values = []
    n_values = []
    if check_estimations(estimations):
        for i in estimations:
            pi_values.append(i[0])
            n_values.append(i[1])
        visualize(pi_values)
        calculation(pi_values, n_values)