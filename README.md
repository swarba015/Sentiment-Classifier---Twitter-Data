# Twitter Sentiment Analysis
## Overview
This repository contains the code for a Twitter Sentiment Analysis project. The project aims to analyze the sentiment of tweets based on the presence of positive and negative words. It involves reading data from a CSV file containing tweets, calculating positive and negative scores for each tweet, and writing the results to a new CSV file.

## Project Description
The project consists of a Python script that performs the following tasks:

1. Reading Tweet Data: Reads tweet data from an existing CSV file named project_twitter_data.csv.
2. Sentiment Analysis: Analyzes each tweet to calculate the count of positive and negative words using predefined lists of positive and negative words.
3. Calculating Net Score: Determines the net score of each tweet by subtracting the negative score from the positive score.
4. Writing to CSV: Writes the results, including the number of retweets, replies, positive score, negative score, and net score, to a new CSV file named resulting_data.csv.
   
## Installation
No specific installation is required other than a Python environment. Ensure you have Python installed on your system.

## Usage
Place project_twitter_data.csv in your working directory. This file should comprise tweet texts, retweet counts, and reply counts.
Execute the Python script. It reads data from project_twitter_data.csv, conducts sentiment analysis, and writes outcomes to resulting_data.csv.
Access resulting_data.csv in your working directory to review the analysis results.

## Data Privacy
Due to privacy concerns, the actual tweet data (project_twitter_data.csv) is not available in this repository. Users of this script should supply their own tweet data in the prescribed format.

## Data Format
The project_twitter_data.csv file should have the following format:

1. The first column contains the tweet text.
2. The second column contains the number of retweets.
3. The third column contains the number of replies.

The resulting_data.csv file will have the following columns:
- Number of Retweets
- Number of Replies
- Positive Score
- Negative Score
- Net Score
  
## Contributing
Contributions to improve the analysis or extend the project's scope are welcome. Please feel free to fork the repository and submit your pull requests for review.
