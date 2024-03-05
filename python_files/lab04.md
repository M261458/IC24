# SD212 Lab 04

## [name] Type your name on the next line

Cory Daut


## [Q1]
> Who are your team's members?

Jillian Broduer, Cory Daut, Addison Neise, Daniel Prather


## [Q2]
> Enter the URL of the GitHub repository that contains your code and
> presentation materials.

https://github.com/M261458/IC24


## [Q3]
> Briefly describe the file organization in your GitHub repository,
> Where is your presentation? Where is your code and what does it do?


Once completing the project I moved all of the graphs, CSV's, python files, and the original data set to their respective repo. Then I left the powerpoint and the abstract out of the repos. The main code was Z_score_by_mean.py This found the Z score and this is the math we based all of our graphs off of. All of the code that made our graphs are in the code repo on github.


## [Q4]
> Say a few words about how your team worked together. Who took on the
> role as "team manager"? How did you organize and share your work?
Dan took the lead on figuring out the algorithm to find the differences in the two data sets; he did this by finding the Z score. After we were able to figure out that, each team member looked into various insights to make a graph. We ended up seeing the different nutrients and foods that needed to be analyzed, and which ones were stable. Then Jillian took the lead on the powerpoint designing it and Cory helped keep organization of the files. So we didn't necessarily have a team manager, but we stuck to our strengths and helped each other out when needed.


## [Q5]
> For the Info Challenge project,
> what outside data source(s) did you incorporate?

https://www.fda.gov/consumers/consumer-updates/flour-raw-food-and-other-safety-facts
https://www.healthline.com/health/food-nutrition/maitake-mushroom
We used these sources to go into our reasoning on why the mushrooms and kale were off standard deviation.


## [Q6]
> What did you have to do to *clean* and *processes* the data?

> (Include the provided datasets as well as any outside data that you
> found in your discussion. Just a few sentences giving the overall
> idea is fine.)

We found that there was missing data in many lines, so we needed to make sure that we accounted for that. Dan wrote an algorithm that took all of the means from both sets and created a new CSV that gave us all of our relevant information. We also used bash commands to cut down the CSV files to work with smaller CSV's when making our graphs.


## [Q7]
> What did you do to *analyze* the data?

> (Again, just a few sentences with an overall description is good.)

To analyze the data we read in the data frame with pandas and then filtered the df to only the columns we needed. Then we grouped all of the rows by nutrient id and then found the standard deviation of all the nutrient ids. Then take the absolute value of each component's mean and then divide that by the standard deviation of the specific nutrient group it is a part of. This can be found in Z-score_by_mean.py


## [Q8]
> How did you create *visualizations* of your analysis?

We used plotly and plotly express for our visualizations. With those two programs we made bar and pie graphs, and scatter plots.



## [Q9]
> What concrete recommendations or conclusions did you make?

We recommend that Maitake Mushrooms, Kale, Sunflower Seeds, Soy Flour and Chickpeas are the foods that need to be analyzed annually each year by the USDA. Along with keeping a close eye on Vitamin D2 nutrient.


## [Q10]
> What tips and suggestions do you have for next year's Info Challenge
> participants?

Before working on the data set, try and understand fully what the data set is made of and try to make a road map of where you want to go with the data set. Also to think of creative ways to go around missing data if there is any. Also enjoy it as much as possible and enjoy the time with your team.



