# AIcadium-interview
This is my submission for the AIcadium take-home assessment. This README explains the file structure of the repository and how to use it.

The EDA notebook contains the Exploratory Data Analysis step of the project. In it, I experiment with data exploration, feature engineering, model selection, and pipeline creation.
There are comments/visualizations to explain some of what I was thinking, as well as some of the results that led me to those conclusions. The final models are not *perfect*, but they work fine for this take-home.
I would have spent much more time on the model experimentation and really tried to focus on performance if this were not a take-home excercise. In this notebook, I also save to disk the 
data transformation pipeline & two output models that can be used, where the user can select which one to use. These are saved in the `./metadata` folder.

The `./input` folder is the input directory that a user should write data to, in a `.csv` file, for the main program to be able to find it. The name of the input file can be
provided as an argument to the main program.
For demo, I simply copied over the file that was included in the email into this `./input` folder, the same file that is included in the root directory. 
The only requirement is that it is a `.csv` file.

The `./output` folder is the output directory that the main program will write data to in a `.csv` file. The name of the output file can be provided as an argument to the
main program.

The `./utils.py` file contains code that originated in the EDA notebook that I later abstracted out to another file, so that this code could be reused in the main program. This is also
important so that the `joblib` (another version of `pickle`) `load` and `dump` functions work with dependencies as expected.

The main program is the `./model.py` file. This is used as a CLI to the functionality of the repo. This program is called as such:
```
python model.py -i <input file name without .csv suffix> -o <desired output file name without .csv suffix> -m <model number, currently only 1 or 2, but as new models are added this can be scaled up>
```

so an example call could look like this
```
python model.py -i coding_round_data -o output -m 1
```
This results in the main program reading from `./input/coding_round_data.csv`, loading up `./metadata/model1.model`, transforming the data so the model can read it using the pipeline developed in the EDA notebook
and stored in the `utils.py` file, doing prediction using this transformed data, and writing it to `./output/output.csv`.

I would like to restate that the modeling is not perfect since the email said to not treat this like a kaggle competition and to focus more on the other parts of ML pipeline creation
such as "data exploration, feature engineering, model selection, and pipeline creation" and that I would make the modeling much better if this were the focus of this project
and if I had more time to work on this.
