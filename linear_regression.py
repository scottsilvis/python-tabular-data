import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def linear_regression(x, y, x_lab, y_lab, output, path = "iris.csv"): # Function to perform linear regression on the data
    dataframe = pd.read_csv("iris.csv")
    x = dataframe.petal_length_cm
    y = dataframe.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    plt.legend()
    plt.savefig(output)
    quit()

def main(): # Function to call the linear regression function
    import argparse

    # Create a command-line parser object
    parser = argparse.ArgumentParser()

    # Tell the parser what command-line arguments this script can receive
    parser.add_argument("-x", 
                        help="The x-axis data", 
                        required=False)
    parser.add_argument("-y", 
                        help="The y-axis data", 
                        required=False)
    parser.add_argument("-x_lab",
                        help="The x-axis label",
                        required=False)
    parser.add_argument("-y_lab",
                        help="The y-axis label",
                        required=False)
    parser.add_argument("-output",
                        help="The output file",
                        required=False)
    parser.add_argument("-path",
                        help="The path to the data file",
                        required=False)

    # Parse the command-line arguments into a 'dict'-like container
    args = parser.parse_args()

    linear_regression(
            args.x,
            args.y, 
            args.x_lab,
            args.y_lab,
            args.output,
            args.path)

if __name__ == "__main__":
    main()