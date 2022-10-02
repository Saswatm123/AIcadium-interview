from joblib import load
import argparse
import pandas as pd

if __name__ == '__main__':

    # Initialize parser
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input_filename", help = "File name (without .csv ending) to read input data from ./input directory", required = True)
    parser.add_argument("-o", "--output_filename", help = "File name (without .csv ending) to output data to from ./output directory", required = True)
    parser.add_argument("-m", "--model", help = "Input model number from ./metadata directory (either 1 or 2, default 1)", default = 1)

    # Read arguments from command line
    args = parser.parse_args()

    print("Loading model metadata/model{}.model".format(args.model) )
    model = load('metadata/model{}.model'.format(args.model) )
    print("Finished loading model metadata/model{}.model".format(args.model) )

    print("Loading pipeline")
    data_transform_pipeline = load('metadata/pipeline.metadata')

    print("Loading input data from file input/{}.csv".format(args.input_filename) )
    data = pd.read_csv("./input/{}.csv".format(args.input_filename) )
    print("Finished loading input data from file input/{}.csv".format(args.input_filename) )

    print("Transforming data")
    data = data_transform_pipeline(data)
    print("Finished transforming data")

    predictions = model.predict(data.drop('Revenue', axis=1) )
    predictions = pd.DataFrame(predictions, columns = ['predictions'])

    predictions.to_csv("output/{}.csv".format(args.output_filename) )
    print("Finished writing predictions to output/{}.csv".format(args.output_filename) )
