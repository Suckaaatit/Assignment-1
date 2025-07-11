# Assignment-1
USEREADY


Power Load Prediction Project 
The main goal was to see if I could get a computer to predict the load type on a power grid (LIGHT, MEDIUM, or MAXIMUM LOAD) using some historical data.

It's a pretty standard classification problem, but it was a great way to practice the whole data science workflow from start to finish.

What's the Goal? 
The objective here was to build a model that can accurately classify the power LOAD TYPE. I used a dataset with features like ENERGY USAGE, REACTIVE POWER, and CO2 LEVELS to make the predictions.

The Dataset 
The dataset (LOAD_DATA.CSV) contains a few key columns:

DATE_TIME: When the reading was taken.

USAGE_KWH: How much energy was being used.

LAGGING_CURRENT_REACTIVE_POWER_KVARH: One type of reactive power.

LEADING_CURRENT_REACTIVE_POWER_KVARH: Another type of reactive power.

CO2(PPM): CO2 levels.

NSM: Number of seconds from midnight.

LOAD_TYPE: The target we want to predict (LIGHT, MEDIUM, or MAXIMUM LOAD).

How I Tackled It 
I followed a few key steps to get from the raw data to the final predictions.

1. The Clean-Up (Data Preprocessing)
First things first, I had to clean up the data.

Loaded the LOAD_DATA.CSV file.

The column names had weird characters and spaces, so I standardized them to make them easier to work with (e.g., Date Time became DATE_TIME).

Checked for any missing (NAN) values and filled them in using the MEDIAN for numbers and the MODE for text. This way, the models wouldn't crash.

2. Making New Features (Feature Engineering)
The DATE_TIME column had a ton of useful info, so I extracted a few new features from it to help the model find patterns:

The HOUR of the day.

The DAYOFWEEK.

The MONTH.

3. The Big Split (Train/Test Split)
For the validation, the requirement was to use the LAST MONTH of data as the TEST SET. This is a good way to check if the model can predict for the near future. So, all data before the LAST MONTH was used for TRAINING, and the final month was held back for TESTING.

4. Model Time! (Training & Evaluation)
This was the fun part. I threw a few different classification models at the problem to see which one would perform best:

LOGISTIC REGRESSION

DECISION TREE

RANDOM FOREST

After training each one, I tested it on the unseen data (that LAST MONTH) and checked the ACCURACY, PRECISION, RECALL, and F1-SCORE to see how well it did.

How to Run It 
It's pretty straightforward to run this yourself.

Make sure you have Python and libraries like PANDAS and SCIKIT-LEARN installed.

Bash

pip install pandas scikit-learn
Place the LOAD_DATA.CSV file in the same directory as the script/notebook.

Run the Python script or the Jupyter Notebook. It will print out all the steps, including the final ACCURACY and classification reports for each model.

Results & Conclusion 
In the end, the RANDOM FOREST model turned out to be the most accurate! It did a pretty good job of classifying the different load types on the test data. 
<img width="479" height="248" alt="image" src="https://github.com/user-attachments/assets/c94c19ee-097f-4b86-bf81-d9b432657852" />
This result is for Logistic Regression
<img width="367" height="191" alt="image" src="https://github.com/user-attachments/assets/0c1b94de-e49d-4833-8d22-41d79bb37987" />
This is the result for Decision Tree 
<img width="350" height="166" alt="image" src="https://github.com/user-attachments/assets/af66aa19-d6c3-4b21-bc17-3e08e36416e8" />
This is the result for Random Forest



