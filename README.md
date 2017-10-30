# Which and when people support Trump's ideas?
## Abstract
Nowadays twitter is a crucial tool to win elections due to its high power of distribution across the world's network.
The goal of this project is analyse how society supports and how ideas are spread across the network.

In order investigate such question our proposal is analyse the tweets posted by Trump in twitter over time to discover 
what is the main focus of his campaign, how it changes and 
how the society reacts to his discurse and proposals. 

The [trumptwitterarchive](http://www.trumptwitterarchive.com/) is a project that have 
been collecting Trump's twitters since 2009 but the main focus in this project will be the period of his campaign.



## Research Questions
- **What are the main topics?**
   
   The tweets will be split into clusters based on its main topic. The cluster might be extract by a heuristic logic
    based on a descriptive analysis of tweets or by 
    [Latent Dirichlet allocation (LDA)](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)if is feasiable.
   
- **How is the impact of each topic over time?**

    Based on the topic's cluster, the idea is analyse how much retweets and likes each topic has over time.  

- **How is the impact of each topic by geolocation?** 

    Based on the topic's cluster, the idea is analyse how much retweets and likes each topic has by geolocation.

- **Sentimental analysis over time of the tweets**
    
    Construct a score for each tweets and topics based on the amount of positive and negative words. To develop it, 
    a dataset of word's scores will be needed and better description can be found in [`Dataset`](#Dataset).


## Dataset 
The main dataset with all tweets posted by Trump is available [here](https://github.com/bpb27/trump_tweet_data_archive) 
since 2009 and the repository is updated every hour. In order to develop this project we will setup a `as-of` to freeze 
our dataset otherwise each time that the analyse is runned, it might get different results. The window time to be 
analysed is still undefined because we need to analyse the data before to choose a feasible amount of data to deal 
in a single machine.

In order to work on sentimental analysis, a extra dataset with word's scores will be needed, there are a lot available 
datasets such as [lexicon](https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html#lexicon), 
[sentiwordnet](http://sentiwordnet.isti.cnr.it/), among others. A list of datasets is available [here](https://medium.com/@datamonsters/sentiment-analysis-tools-overview-part-1-positive-and-negative-words-databases-ae35431a470c).


## A list of internal milestones up until project milestone 2
- Choose the word's scores dataset based on the amount of words available and context (which is the context that the scores were built on).
- Discovery the window time feasible to develop the project in a machine with 8GB of RAM. The period of campaign must be include in this interval.
- Clean stop words from dataset.
- Descriptive and exploratory analysis of tweets' text.
- Check if LDA model is a feasible approach to find topics and then classify tweets.
- Have a final proposal of the topics that will be analysed to answer the [`Research Questions`](#Research-Questions).

## Questions for TAa
- Can I put my main function in a python project instead of putting everything in the `jupyter notebook`? So I can write unit tests and also don't turn `jupyter notebook` too dirty 