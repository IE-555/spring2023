# Write a Brief Descriptive Title Here

Authors:  **Mihir Ravindra Jadhav**, **Poorva Bhatia**, **Pushkar Shirish Kulkarni**, **Ankita Anand**.

YouTube Video:  [Link](http://your_link_goes_here)

---

**NOTE**:  The *italicized* content below is for your reference only.  Please remove these comments before submitting.


---
## Task List
*The table below will serve as your Progress Report (due by end of day on Monday, May 8).  Be sure to list all tasks that you need to complete to finish your analysis and to successfully complete the requirements of this project.*

| ID | Task Description | Due Date | Status |
| --- | --- | --- | --- |
| 1 | Research and study the YouTube API documentation | 2023-04-19 | DONE |
| 2 | Setup YouTube API credentials and authorize requests | 2023-04-21 | DONE |
| 3 | Searching and writing Python code to call the YouTube API and retrieve video metadata and metrics with appropriate referencing | 2023-05-01 | DONE |
| 4 | Cleaning and preprocessing dataset using Pandas library | 2023-05-11 | WIP |
| 5 | Perform exploratory data analysis and generate insights | 2023-05-12 | WIP |
| 6 | Create data visualizations using data visualization libraries and generate corresponding line charts, bar charts, histograms, etc. to analyze different matrices such as view count, like and dislike count, for a particular YouTube channel | 2023-05-13 | PENDING |
| 7 | Write final project report of findings which will include project objectives, data analysis, methodology and conclusions | 2023-05-15 | PENDING |
| 8 | Record, edit and upload YouTube video showcasing project | 2023-05-15 | PENDING |
| 9 | Commit final changes to the README.md file in GitHub Repository | 2023-05-16 | PENDING |
| 10 | Check for final changes and submit the entire project with all the necessary documentation and referencing | 2023-05-17 | PENDING |

--- 

## Introduction
*The purpose of this section is to provide some background about your project.  For example, your introduction should discuss*
- *The purpose of your project;*
- *The type of data you're using;*
- *What you're doing with this data;*
- *What types of analysis you're conducting;*

*Your introduction should make the reader excited to read the rest of this document.*

---

## References
*In this section, provide links to your references and data sources.  For example:*
- Source code was adapted from [the magic source code farm](http://www.amagicalnonexistentplace.com)
- The code retrieves data from [the organization for hosting cool data](http://www.anothermagicalnonexistentplace.com)
- The forecasting models were modified from [some academic research paper](http://www.linktotheacademicpaperyouused.com)

---

## Requirements
*In this section, provide detailed instructions for installing any necessary pre-requisites.  This could include:*
- *Python packages/libraries;*
- *API keys;*
- *etc.*

---

## Explanation of the Code
*In this section you should provide a more detailed explanation of what, exactly, your Python script(s) actually do.  Your classmates should be able to read your explanation and understand what is happening in the code.*

The code, `needs_a_good_name.py`, begins by importing necessary Python packages:
```
import matplotlib.pyplot as plt
```

- *NOTE:  If a package does not come pre-installed with Anaconda, you'll need to provide instructions for installing that package here.*

We then import data from [insert name of data source].  We print the data to allow us to verify what we've imported:
```
x = [1, 3, 4, 7]
y = [2, 5, 1, 6]

for i in range(0,len(x)):
	print "x[%d] = %f" % (i, x[i])		
```
- *NOTE 1:  This sample code doesn't actually import anything.  You'll need your code to grab live data from an online source.*  
- *NOTE 2:  You will probably also need to clean/filter/re-structure the raw data.  Be sure to include that step.*

Finally, we visualize the data.  We save our plot as a `.png` image:
```
plt.plot(x, y)
plt.savefig('samplefigure.png')	
plt.show()
```

The output from this code is shown below:

![Image of Plot](samplefigure.png)

---

## How to Run the Code
*Provide step-by-step instructions for running the code.  For example, I like to run code from the terminal:*
1. Ensure that you have registered for the [insert name of API] API key.  (You may reference the instructions for doing this.)

2. Ensure that you have installed necessary Python packages. (Again, you may include a reference here to a prior section in the README that provides the instructions.)


2. Open a terminal window.

2. Change directories to where `needs_a_good_name.py` is saved.

3. Type the following command:
	```
	python needs_a_good_name.py
	```

- *NOTE: You are welcome to provide instructions using Anaconda, IPython, or Jupyter notebooks.*

---

## Results from your Analysis
*Last, but not least, you need to demonstrate your results.  You should include figures and/or tables of results.  What worked well?  What could be improved?*
