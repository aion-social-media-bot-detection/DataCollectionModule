# DataCollectionModule

This module is the component of aion-social-media-bot-detection resposible for collection data from social media. In this case we begin with twitter.

Following are the parameters that can be used to fetch data

1. StartDate: The date from which data needs to be fetched
2. Days: The number of days for which data needs to be fetched
3. queries: A list containing all the topics or terms data needs to be fetched
4. maxTweets: The maximum number of tweets that needs to be pulled for each day

All of these parameters can be updated in the queries.json file

To run the module type <code>python exporter.py</code> in the command line
