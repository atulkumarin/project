# Demystifying POTUS, one tweet at a time...

## Project 
Final Data Story containing the principal analysis can be found [here](https://liabifano.github.io/project/history/)

The final notebook can be found [here](https://github.com/liabifano/project/blob/master/analysis/FinalNotebook.ipynb)

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
   

## Datasets

#### Tweets

The Trump Twitter Archive project collects and updates tweets by trump on an hourly basis. 
The data is available here - [TrumpTwitterArchiveGithub](https://github.com/bpb27/trump_tweet_data_archive). 
The data is arranged in an yearly fashion into two kinds of `JSONs` - `condensed` and `master` (Eg. - `master_2016.json.zip` and `condensed_2016.json.zip`).

We will be using the master JSON files which contains the full response from Twitter's API. 
This will later give us the flexibility to add more analysis or drop some fields, if not required. 
Note that the JSON file for the year 2017 in the archive keeps changing every hour as it is updated with latest tweets.

#### Sentimental Scores

VADER (Valence Aware Dictionary and sEntiment Reasoner) is a tool with lexicon for sentimental analysis and it is tunned and performs very well in social media.
The paper with more informations about who it is calculated and the performance can be found [here](http://comp.social.gatech.edu/papers/icwsm14.vader.hutto.pdf?lipi=urn%3Ali%3Apage%3Ad_flagship3_pulse_read%3BbAUS6s97R5uxMEV9nK7ePw%3D%3D). 
