import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def linear_regression(x = "petal_length_cm",
                      y = "sepal_length_cm", 
                      x_lab = "Petal Length (cm)",
                      y_lab = "Sepal Length (cm)", 
                      output = "linear_regression", 
                      group = "species",
                      path = "iris.csv"): # Function to perform linear regression on the data
    
    """Perform linear regression and create a graph containing slope and trendline.

    Parameters
    ----------
    x : str
        The x-axis data
    y : str
        The y-axis data
    x_lab : str
        The x-axis label
    y_lab : str
        The y-axis label
    output : str
        The output file
    group : str
        The group to plot
    path : str
        The path to the data file #Should I include a second path to an excel file that contains x_lab and y_lab?

    Returns
    -------
    slopes : list
        A list of the slopes of the linear regression for each group.
    intercepts : list
        A list of the intercepts of the linear regression for each group.
    r_values : list
        A list of the correlation coefficients for each group.
    p_values : list
        A list of the p-values for each group.
    stderrs : list
        A list of the standard errors for each group.
    """

    try:
        dataframe = pd.read_csv(path)
    except FileNotFoundError:
        print("Error: File not found")
        return
    except pd.errors.EmptyDataError:
        print("Error: Empty dataframe")
        return
    except pd.errors.ParserError:
        print("Error: Could not parse the file")
        return
    except Exception as e:
        print("Error:", e)
        return
    
    print("\nreading data from ", path)
    
    if group not in dataframe.columns:
        print("\nGroup not found in dataframe. Plotting all data.")
        x_data = dataframe[x]
        y_data = dataframe[y]
        regression = stats.linregress(x_data, y_data)
        slope = regression.slope
        intercept = regression.intercept

        plt.scatter(x_data, y_data)
        plt.plot(x_data, slope * x_data + intercept, label = 'Fitted line')
        plt.xlabel(x_lab)
        plt.ylabel(y_lab)
        print("\nx axis label: ", x_lab)
        print("\ny axis label: ", y_lab)
        plt.legend()
        save = output + ".png"
        print("\nsaving plot to ", save)
        plt.savefig(save)
        print("\nplot saved!")
    
    if group in dataframe.columns:
        for i in dataframe[group].unique():
            print("\nplotting ", i)
            x_data = dataframe[dataframe[group] == i][x]
            y_data = dataframe[dataframe[group] == i][y]
            
            if x_data.empty or y_data.empty:
                print("Error: Empty data")
                continue

            regression = stats.linregress(x_data, y_data)
            slope = regression.slope
            intercept = regression.intercept

            plt.scatter(x_data, y_data, label = i)
            plt.plot(x_data, slope * x_data + intercept, label = 'Fitted line')
            plt.xlabel(x_lab)
            plt.ylabel(y_lab)
            print("\nx axis label: ", x_lab)
            print("\ny axis label: ", y_lab)
            plt.legend()
            save = output + "_" + i + ".png"
            print("\nsaving plot to ", save)
            plt.savefig(save)
            print("\nplot saved!")

        print("\nAll plots generated!")

def main(): # Function to call the linear regression function
    import argparse

    # Create a command-line parser object
    parser = argparse.ArgumentParser()

    # Tell the parser what command-line arguments this script can receive
    parser.add_argument("-x", 
                        help="The x-axis data", 
                        default="petal_length_cm",
                        required=False)
    parser.add_argument("-y", 
                        help="The y-axis data", 
                        default="sepal_length_cm",
                        required=False)
    parser.add_argument("-x_lab",
                        help="The x-axis label",
                        default="Petal Length (cm)",
                        required=False)
    parser.add_argument("-y_lab",
                        help="The y-axis label",
                        default="Sepal Length (cm)",
                        required=False)
    parser.add_argument("-output",
                        help="The output file",
                        default="linear_regression",
                        required=False)
    parser.add_argument("-group",
                        help="The group to plot",
                        #default="species",
                        required=False)
    parser.add_argument("-path",
                        help="The path to the data file",
                        default="iris.csv",
                        required=False)

    # Parse the command-line arguments into a 'dict'-like container
    args = parser.parse_args()

    linear_regression(
            args.x,
            args.y, 
            args.x_lab,
            args.y_lab,
            args.output,
            args.group,
            args.path)

if __name__ == "__main__":
    main()