# Demystifying POTUS, one tweet at a time...

## Project Miletone 2
The analysis regarding the milestone 2 can be found [here](https://github.com/liabifano/project/blob/master/analysis/Project-MileStone2-Updated.ipynb)

## Abstract
Twitter plays a crucial role in politics these days. Gone are the days of door-to-door campaigning and trying to reach the last man. Today, power is weilded by those who can tweet. A carefully worded 140 character phrase carries the ability to swing states and potentially change the course of an entire nation. The goal of our project is to analyse the impact of Twitter on society and understand how ideas are spread across a network.

In order to investigate this question, our proposal is to analyse the tweets posted by Trump on Twitter over time to discover 
what was the main focus of his campaign, how it changed and how the society reacts to his discourses and proposals. 

The [Trump Twitter Archive](http://www.trumptwitterarchive.com/) is a project that has been collecting Trump's tweets since 2009 but the main focus of this project will be the period of his campaign.


## Research Questions

- **How linguistic tones create an impact?**

   Sentiment Analysis - breaking down tweets into positive, neutral and negative remarks to figure out how Trump uses language to create an impact. This might also extend to recording the use of exclamation marks and capitalised words to measure the unambiguity of the tweet emotion.
   Ego Analysis - finding occurences involving the use of self to promote an idea/situation. This might give us important insights about the impact of his tweets.
   
- **Is it okay to generalize the sentiments based on ALL the tweets?**

   Source Anaylsis - almost all major political players have an additional media team who handle their Twitter Account. Same can be said about Trump. We can analyze the metadata to find out if the tweet has been sent out by the media team or Trump himself. For example, we can have a look at the source of the tweet. (sent by iPhone/Android). This can help us in analyzing the tweets in a better way.

- **Is it all about the timing?**

   Temporal Analysis - this involves a broad spectrum of topics, ranging from analyzing Trump's favorite time of the day to tweet vs its impact to how his number of followers get affected as an aftermath of a sensational tweet and in general, analyzing the changing preference of voters through time.
   
- **What are the distinct themes across tweets?**
   
   Clustering Analysis - the tweets will be split into clusters based on its main topic. The cluster might be extracted by a heuristic logic based on a descriptive analysis of tweets or by [Latent Dirichlet allocation (LDA)](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) if it is feasible. We can then perform aforementioned temporal analysis for each topic.
   
- **Does location matter?** 

    Spatial Analysis - based on the topic's cluster, the idea is to analyse how much retweets and likes each topic has by geolocation.


## Dataset 

The main dataset with all tweets posted by Trump is available [here](https://github.com/bpb27/trump_tweet_data_archive) 
since 2009 and the repository is updated every hour. In order to develop this project we will setup an `as-of` to freeze 
our dataset otherwise each time that the analysis is run, it might give different results. The window time to be 
analyzed is still undefined because we need to analyse the data beforehand in order to choose a feasible amount of data to deal with in a single machine.

In order to work on sentimental analysis, an extra dataset with word scores will be needed. There are a lot available 
datasets such as [lexicon](https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html#lexicon), 
[sentiwordnet](http://sentiwordnet.isti.cnr.it/), among others. A list of datasets is also available [here](https://medium.com/@datamonsters/sentiment-analysis-tools-overview-part-1-positive-and-negative-words-databases-ae35431a470c).


## A list of internal milestones up until project milestone 2

- Choose the word scores dataset based on the amount of words available and context (what is the context upon which the scores were built).
- Discover the window time feasible to develop the project in a machine with 8GB of RAM. The period of campaign must be included in this interval.
- Clean stop words from dataset.
- Descriptive and exploratory analysis of tweets' text.
- Check if LDA model is a feasible approach to find topics and then classify tweets.
- Have a final proposal of the topics that will be analysed to answer the [`Research Questions`](#Research-Questions).

## Questions for TAa
- Can I put my main function in a python project instead of putting everything in the `jupyter notebook`? So I can write unit tests and also don't turn `jupyter notebook` too dirty 
