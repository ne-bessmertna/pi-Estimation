import Estimation
import Comparison


def continue_request():
    """Check whether the user wants to continue running program."""
    request = input('Would you like to continue? Yes/No\n').lower()
    while True:
        if request == 'no':
            return '3'
        elif request == 'yes':
            return None
        else:
            request = input("Please, enter your answer as yes or no.\n").lower()


def initialize():
    """Get a request from user and call functions to launch estimation/comparison."""
    est_requests = ['1', '1)', 'one', 'first', 'estimate', 'estimate π', 'estimate pi', 'e']
    comp_requests = ['2', '2)', 'two', 'second', 'compare', 'compare π', 'compare π values', 'compare pi',
                     'compare pi values', 'values']
    quit_requests = ['3', '3)', 'three', 'third', 'quit']
    estimations = []
    user_input = 0
    while user_input not in quit_requests:
        print('Please, specify what you would like to do this time:\n1) Estimate π\n2) Compare π values\n3) Quit')
        user_input = input().lower()
        if user_input in est_requests:
            est_result = Estimation.estimate()
            estimations.append(est_result)
            print(f"With {est_result[1]} number of points, estimated π is {est_result[0]}.")
            user_input = continue_request()
        elif user_input in comp_requests:
            Comparison.compare(estimations)
            user_input = continue_request()
        else:
            print('Your request is invalid. Please, enter your choice as 1, 2 or 3:')
            user_input = input().lower()
    print("See you next time!")


if __name__ == "__main__":
    print('Welcome to Monte Carlo\'s π Estimation!')
    initialize()