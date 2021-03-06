### This is a report of project in the course [Data visualization](https://edu.epfl.ch/coursebook/en/data-visualization-COM-480) of EPFL. The project is divided into [milestone1](#1), [milestone2](#2) and [milestone3](#3).

### Please view current progress of our website via https://dvpatricks.github.io/index.html

### If you have further questions about the project, please contact:

- [Guosheng Feng](guosheng.feng@epfl.ch)

- [Haixin Shi](haixin.shi@epfl.ch)

- [Zhiye Wang](zhiye.wang@epfl.ch)


<h1 id="1"> Milestone 1 (Friday 8th April) </h1>

## Dataset

For this project, we decided to explore [Games of All Time from Metacritic](https://www.kaggle.com/datasets/xcherry/games-of-all-time-from-metacritic). It was found on [Kaggle](https://www.kaggle.com/)

### Data Quality

It contains 8831 different games from [metacritic](https://www.metacritic.com/browse/games/score/metascore/all/all/filtered), and offers us 9 attributes including **user score, meta score, platform information, description, developer, url to game, genre, rating (E, M, T etc), type (multi/single player)** of each game, so it is abundant to be explored. 

From a quick look, it provides data in good quality:
- **`Completeness`**: There is no missing data.
- **`Consistency`**: For each column, data inside is in the same type or format.
- **`Accuracy`**: User score and meta score are all in normal distribution.

### Data Prepossesing

The KEY reason that we selected this dataset is that we found the URL column inside the dataset, from which we could use web crawler to gather **Release Time** of each game! 

By using the time information, we can boost the information contained in the dataset a lot. For example, we can add time-axis on different dimensions, and depict the variation trend, which is very promising! 

Apart from release time, we can also gather other information like the comments from players, but it is not the main part.

Actually, we have collected time information by using Python Crawler, and the code is provided [here](https://github.com/com-480-data-visualization/datavis-project-2022-patricks/blob/main/Python_Crawler.py)

After colleting release time of each game, we can focus ourselves on data visualization in next two milestones!

## Problematic

### Overview

Through this project, we aim to provide a one-stop webpage with cool interaction that will deliver the interesting information of games evolving through time. 

### Motivation

Our motivation is to enable users to get insights to the dynamic information of game evolution in multiple dimensions at a single stop. The potential user types of our website can be:

- **`Players`**: By selecting rating(Game Target audients), type (multi/single player), genre, and etc, according to their personal preference, they will get some recommendations from our website. Or they just input a name of game(if applicable), and then they can be shown with abundant information related to the game that interests them.

- **`Game Companies`**: Game companies can get insight into the trend of game evolution, so in this case, they can move their targets to a specific direction respect to popular game genre, type and platform. Based on the information we provide, they can set the rules to hire people, like hiring software engineers with the knowledge of popular game platforms and types.

- **`Investors`**: Investors can view all positions or impact of different game companies, so they can make decision from their intuition of the market evolusion. As for the identifies of games, our platform can help investors adapt their attentions.

For all users, we can provide the relationship between user score and meta score, so they can have a better understanding of game scores in other platforms.

### Dimensions

The primary dimension of the visualization is as followings:
- **`Game Description`**: To outline a specific game, we will show the word cloud of this game by collecting information from different axis.
- **`Relationship Analysis`**: We will analyze the relationship between different attributes. For example, would platform affect the score of a game? How much it would affect?
- **`Popularity Analysis`**: We will show changing trend of popularity of game genres, platforms, rating, and developers.


## Exploratory Data Analysis
<img src="./pics/genre_percent.png" width="450">

**`Percentage of top 10 genres`** : The pie chart shows the top-10 most popular game genres (based on the game number produced among all the years). It is apparent from the figures that action game is most popular among all games.

<img src="./pics/meta-user_score_regress.png" style="zoom:67%;" >

**`Meta-user score regression analysis`** :Regression of meta-score and user-score. All the points are located adjacent on either side of the regression line, which shows that although there are positive correlation between user and expert people's feedback, there are also discrepancies which we want further dig into.

<img src="./pics/meta-user_score.png" style="zoom:50%;" >

**`Basic statistic for user and meta (expert) score`** :The table shows a basic statistic of user score and meta score for each game including mean, standard deviation, quantile,etc. We found that the user score has larger standard variation value, and also  extreme feedbacks such as a score "2" for a poor game.

<img src="./pics/platform_rank.png" style="zoom: 75%;" >

**`Platform score rank`** :Rank of different platforms. Nentindo-64 and stadia rank first and second, which outperform all other platforms. We could also observe that some recent console playtforms have higher mean game scores such as "Play-station 5" and "Xbox-series-x", which is in line with current market's trend. ([PS5 Sold Out News](https://www.pushsquare.com/guides/ps5-stock-where-to-buy-playstation-5-and-when-in-march-2022))

<img src="./pics/platform_scores.png" style="zoom:80%;" >

**`Platform score distribution`** :Score distribution for platforms, from which we know most games obtain a score between 70 and 85, and the PC is the most common platform for games, followed by Sony's PlayStation4 and PlayStation3



<img src="./pics/type_score.jpg">

**`Score Distribution for single-player and multi-player game`** : Here we plot the user and meta score distribution for single and multi player games. We could observe two interesting points here:

1. The Meta Score distribution has a gap between the range 60-80, while user score distributed more smoothly.

2. When look at the Kernal Density Estimation (KDE) Curve, we could see that normal Users may prefer give higher scores for single-player games while those "Experts" prefer multi-player games.

   

<img src="./pics/Average_meta_scores_over_each_year.png" style="zoom:85%;" >

**`Average meta scores over the years`** : As shown above, the average scores for each year are higher during 1995-1999, which shows that some "old fashion" games are really in favord. Then the average scores go down after the year 2000, which may attribute to the fact that there are more game pipelines appeard, which produce many profit-oriented low-quality games.

> For other pre-analysis of the dataset, please refer to https://github.com/com-480-data-visualization/datavis-project-2022-patricks/blob/main/data_analysis.ipynb





## Related Work
- **`Q1`**: What others have already done with the data?

Recommender System, like the [author](https://game-recommender-engine.herokuapp.com/) of this dataset. Besides, other people may perform Descriptive Analysis and Visualization and EDA-Exploratory Analysis.

- **`Q2`**: Why is your approach original?

We crawled the release date data of the games from orginal websites. The extra information is a good complementary to the original data so that we analyzed the data in a time series and drew some interesting and important fact.

- **`Q3`**: What source of inspiration do you take? Visualizations that you found on other websites or magazines (might be unrelated to your data).

We use pie chart, bar chart and line chart in our analysis. For each kind of the chart, the bar chart uses the height of the column to reflect the differences in data. The naked eye is very sensitive to height difference and the recognition effect is good. Line charts are suitable for large two-dimensional data sets, especially where trends are more important than individual data points. The pie chart shows the proportion of a certain part in the whole.



<h1 id="2"> Milestone 2 (Friday 6th May) </h1>

The initial version of our website is accessible on https://dvpatricks.github.io/index.html

<h2 id="figure1"> Figure 1 (WHO ARE THE TOP GAME COMPANIES?) </h2>

- **`Introduction`** Every bubble represents a company and the size of each bubble means the number of games that corresponding company publishes.  When we move our mouse to a specific company, the circles with mouse on would become large; and at left side there would appear top 6 games of that company. When we move out the mouse, the size of circle would return to normal size and the games would disappear.

- **`Usage`** This graph can vividly show the circulation as well as market share of different game companies. What is more, for a specific game, you can find the most popular games published by it so as to have a basic impression on it.

- **`Progress`** In the next milestone, we would change the color of bubbles into the logos of corresponding companies. Besides, we would provide the real data of a specific company when moving mouse on it.(Currently, it is static which means that now it would always show the same figure about six top games.)

<img src="./pics/Bubble Char.jpg" style="zoom:67%;" >

<h2 id="figure2"> Figure 2 (WHICH PLATFORM WILL YOU CHOOSE?) </h2>

- **`Introduction`** It is a **ranking** bar chart that count the number of games released per platform per year from 1995 to 2021. Every annual data will last for about three seconds and we also draw a transition animation between two frames to present the chance process. When users hover their mouse on the plot, the animation will pause and wait for a further check from the users. When users move their mouse from the plot, the animation will continue to play.

- **`Usage`** This is a module for entertainment. For a game enthusiast, this module can help users understand the history and current status of various game platforms. 

- **`Progress`** The current progress we made in this module is we have implemented the initial data race demo. It still needs to be prettified and add hover events. The figure below is a demo and shows what we have done for now. We add some comments on the sketch to describe features and functions of our module.


<img src="./pics/data_race_sketch.png" style="zoom:67%;" >

<h2 id="figure3"> Figure 3 (MAYBE SOME RECOMMENDATION?) </h2>

- **`Introduction`** In the circle, a group of points represents the games from a company. The links between points represenst similarity between two games with respect to genre, rating(E, M, T etc), and type(multi/single player). When we move our mouse to a point, it would hightlight links from this point to other points, namely games.

- **`Usage`** This graph can help game players to find out some games that are similar to their favorite games. Besides, it can also help companies to find their competitors. As for investers, they can have a better understanding of the games that they invest.

- **`Progress`** In the next milestone, we want to deliver more information via the links like the similarity ratios corresponding to genre, rating(E, M, T etc), and type(multi/single player).

<img src="./pics/Circle Chart.jpg" style="zoom:67%;" >


<h2 id="figure4"> Figure 4 (WHAT KIND OF THE GAME DO YOU LIKE?) </h2>

- **`Introduction`** It is made up with selectors and scatter plot. There are three **selectors**(rating, platform and genre for now) at top of the figure. Users are able to set conditions and filter out the games that meet the criteria. For the **scatter** part, x-axis stands for user score and y-axis represents meta score. Filtered games are going to be shown on the figure according to their scores. When users hover their mouse on the points, A hover box will display a breif discription about the game. If users are interested in the description, they can futher click the points and enter the games website. 

- **`Usage`** This module aims at helping and accelerating the process when finding potential interested games. Scores for games from meta and other users are obvious to the users in a scatter plot. Below is an initial version of the module and we further add some comments about what need to be improved and implemented.

- **`Progress`** The current progress is we have implemented three easy ***select*** labels(single choice). We can extract key words from the ***select*** and filter data according to the conditions. We attach an event ***onchange*** to the select and when detected there is a change in the ***select***, it will replot the picture. Also every points in the plot has events ***mouseover*** and ***mouseout***. Concrete events are still need to be implemented.


<img src="./pics/scatter_plot_sketch.png" style="zoom:67%;" >

## **Tools to be used and inspirations from lectures**

For [Figure 1](#figure1), we prepare data and use d3.js to draw this graph. We find **[reference code](https://observablehq.com/@d3/bubble-chart)** here.

For [Figure 2](#figure2), we use d3.js to draw barplot and bundle the data with the barplot. We find **[reference code](https://observablehq.com/@d3/bar-chart-race)** here.

For [Figure 3](#figure3), we prepare data and use d3.js to draw this graph. We find **[reference code](https://observablehq.com/@d3/bilevel-edge-bundling)** here.

For [Figure 4](#figure4), we use d3.js to obtain conditions embeded in the selectors and filter data used for drawing scatter plot. We also need bootstrap to pretty our button and selector. We also need to draw a scatter plot and bundle attached information with the points. We find **[reference code](https://observablehq.com/@d3/scatterplot)** here.

We have collected a lot of inspirations from the lecture slide ???Graph Visualization??? provided by KIRELL BENZI. To be more specific, in Figure 3, we would deliver the similarity score of two games via the tickness of the link between them. Besides, in Figure 1, we use size of the node to deliver the number of games that a company publishes.

We want chanllenge ourselves to build a map to show the address information about game developers, which was inspired by the  lecture slide ???Map??? provided KIRELL BENZI.

<h1 id="3"> Milestone 3 (Friday 3th June) </h1>

## Process Book
We have discussed what we did in our process book, which is very detailed, please refer to https://github.com/com-480-data-visualization/datavis-project-2022-patricks/blob/main/Process_Book.pdf.

## Screencast
We have made a screencast to present our product, please refer to **[here](https://youtu.be/m2d1bH9zOfo)**

# Technical Setup
We use D3.js and Bootstrap to implement our fancy website. And our local server is jekyll, use `bundle exec jekyll serve` command at scr file of our repository can run the website loacally.
