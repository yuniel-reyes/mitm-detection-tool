import time

# Number of dots to print
def print_dots():
    num_dots = 20

    for _ in range(num_dots):
        print(".", end="", flush=True)  # Print a dot without a newline and flush the output
        time.sleep(1)  # Add a delay to control the speed of printing
    print('\n')

