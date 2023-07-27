# WhatsApp Text Analysis

WhatsApp is one of the most commonly used chat applications. Given its amazing and user-friendly interface, it attracted a lot of people. The inclusion of emojis, images, features like deleting messages, and several others make it interesting.

This project aims to analyze WhatsApp chat data to understand the statistics of a conversation and identify trends between individuals or a group of people. The main focus of this project is to identify keywords and perform text analysis.

## Getting Started

To get started with the WhatsApp text analysis, follow the steps below to extract your WhatsApp chat data:

1. Open the WhatsApp application on your device.
2. Select a chat or a group chat you want to analyze and open the chat box.
3. For Android users:
   - Tap the three dots located at the top of the application.
   - Select and click on "Export chat".
4. For iPhone users:
   - Click on the "contact name" at the top of the chat.
   - Scroll to the bottom of the page and find the "Export Chat" option.
5. Export the chat to your email and download it on your local machine.

## Requirements

Before running the code provided in `WPData.ipynb`, make sure you have the following packages installed:

- numpy
- pandas
- seaborn
- matplotlib
- emoji
- re
- datetime
- csv
- calendar
- wordcloud

You can install these packages using the following command:

```bash
pip install numpy pandas seaborn matplotlib emoji wordcloud
```

## Code Description

The `WPData.ipynb` contains Python code that performs various analyses on the WhatsApp chat data. The code uses the provided data in the text file and extracts the information using regular expressions. It then writes the extracted data to a CSV file for further analysis.

The provided code snippet can be summarized as follows:

1. Import necessary packages: Imports required libraries for data manipulation and visualization.
2. Define a regex pattern: Creates a regex pattern to extract date, time, sender, and message from each line of the WhatsApp chat.
3. Read and extract data from the text file: Reads the text file containing WhatsApp chat data and extracts the required information using the regex pattern.
4. Write the extracted information to a CSV file: Writes the extracted data to a CSV file named "output.csv" for further analysis.
5. Visualize data: The code provides various visualizations, such as bar plots and word clouds, to analyze the chat data.

## Running the Code

To run the code, follow the steps below:

1. Ensure you have the required packages installed as mentioned in the "Requirements" section.
2. Place the WhatsApp chat text file (named "_chat.txt") in the appropriate location or modify the `t_file` variable to specify the correct path to the file.
3. Run the code cell by cell in the Jupyter Notebook (`WPData.ipynb`).

## Data Analysis

The code provided performs several data analyses on the WhatsApp chat data:

1. Visualizing message count by the sender: Plot a bar graph to show the number of messages sent by each sender.
2. Analyzing media sharing: Identifies messages with media content and counts the number of media shared by each sender.
3. Identifying busy hours: Determines the busiest hours of conversation by counting the number of messages sent during each hour of the day.
4. Counting emojis: Counts the number of emojis used in the chat.
5. Extracting the day from dates: Extract the day of the week from each date and adds it as a new column to the data.
6. Analyzing messages sent on each day: Plot a bar graph to show the distribution of messages sent on each day of the week.
7. Creating a heatmap: Generates a heatmap to visualize the interaction between different senders on different days.
8. Word cloud: Creates a word cloud to display frequently used words in the chat.

Feel free to modify the code or use the provided insights to perform more in-depth analyses of your WhatsApp chat data.
