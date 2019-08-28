# Taking Board Games Seriously
(Leon Liu & Andrew Charlton - CIS3120 Group Project December 20th, 2018)

Abstract:
We selected a website that ranks board games by the website’s Geek Members Rating, Average Ratings, and number of Voters that participated each game. Given the fact the ratings are neck to neck, such as the Geek Ratings are compared against by the 100th of decimal ratings. We want to test how reliable the ranking system by plotting the Geek Ratings against Avg Ratings and providing analysis with the founding standard deviation results. Conclusion shows us the Voter contribution is a main driving factor for reliability. Our PY Plot example also shows Avg Ratings as more lenient, giving higher ratings versus Geek Ratings’s higher standard ratings. The statistics from overall Standard Deviation shows us, the most votes deserve more standing in their ranks meanwhile lesser votes are not as reliable because it has lesser data(voters) to work with.

Data:
We collected data from the website: “https://boardgamegeek.com/browse/boardgame“ Although there are 100 games on each page and 1035 pages total, we only selected the
first page that shows top 100 to be our main focus. The main table we collected data contains ranking 1 to 100 as its first column, follow with the Board game’s Name, Geek member Ratings, Average overall Ratings, and the Number of Voters participated per each game listed.
Programs:
• Dic_of_games.py – using BEAUTIFULSOUP from bs4 and REQUESTS, we created 2 functions:
o First function dicOfGames to scrape the top 100 board game Names, Geek Ratings, Avg Ratings, and Voters using lists and dictionary. The data scraped is placed into a dictionary and can be checked by entering a name of a game to retrieve the ratings and votes values.
o Second function ratingsList conglomerates all ratings and voter counts to their proper orders.
o We then use PICKLE to export data onto individual CSV files for dictionary, avg rating, geek ratings, and voters. Thereafter, the following programs will load the data as needed through the csv files created.
• Statistics_by_columns (imagine available under) – using PANDA, with DATAFRAME, we gather the MIN, MAX, MEDIAN, and STANDARD DEVIATIONS for each of Geek Ratings, Avg Ratings, and Voters
• Statistics_overall – using PANDA, with DATAFRAME, we collectively generated the standard deviation for each game, resulting in a complied list of true value of voter counts to their ratings. The main result that drives our conclusion.
• Plot_charts (image available under)– using MATPLOTLIB with PYPLOT, we created and compare against two dot charts (GeekRatings & AvgRatings)

Conclusions:
Typically, many users give more attention to the top ~30 of the list rather the bottom ~30. We draw our conclusion with first, the plot charts compared against to another shows Avg Ratings are noticeably higher than Geek Ratings, where they are more conservative in their ratings. Secondly, from the statistics overall results, the standard deviation is direct correlation to the number of voters that participated. What we found is, from the top 30 and bottom 30 is that some games are either overrated or underrated but seemly more popular.
Example #1: bottom 30 (image available below): Rank # 75: “Pandemic”
Geek Rating: 7.554
Avg Rating: 7.65
Voters: 78,938
Standard deviation of 45,558 (the highest of bottom 30 and top 30).
We can say Pandemic is likely more popular, active, and honest than most games given the number of voters that participated.
Example #2: top 30 (image available below):
Rank # 15: “Twilight Imperium (Fourth Edition)”
Geek Rating: 7.976
Avg Rating: 8.77
Voters: 4,715
Standard Deviation of 2,712 (the lowest of bottom 30 and top 30) The low voters count is possibly overrated and more prone to bias
Don’t miss out on bottom ranked games because some of them could be just what you’re looking for.
Contributions:
Web Scraping (dic_of_games.py) Statistics_overall.py Statistics_by_columns.py Plot_charts.py
Report
(Initiated, Edit, Comments by Andrew, Review by Leon) (Initiated by Leon, Edit and Comments by Andrew) (Initiated by Leon, Edit and Comments by Andrew) (Initiated by Leon, Edit and Comments by Andrew) (Initiated, Draft & Edits by Leon, Review by Andrew)

Images:
(Statistics for Geek Rating, Average Rating, and Voters)
  (Plot Charts, Top: Geek Ratings, Bottom: Average Ratings)

 Example # 2 (Standard Deviation for TOP 30 with example #15 highlighted)
Example # 1 (Standard Deviation for BOTTOM 30 with example #75 highlighted)
 
