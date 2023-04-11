# Import modules for: regular expressions; reading timestamps as date objects; loading files using regular expression;
# generate random numbers; reading JSONL files; working with XML files
import re
from datetime import datetime
from glob import glob
import jsonlines
import pandas as pd
import operator
from transformers import pipeline

# Initialise the Sentiment Analysis tool
sentiment_pipeline = pipeline(model="bhadresh-savani/distilbert-base-uncased-emotion")

# List all filenames with the .jsonl extension
files = glob("*.jsonl")

# For each file do:
for file in files:
    # create an empty list to save the spreadsheet rows
    data = []
    output_filename = file.replace("*.jsonl", "") + ".csv"
    # Read the file as a jsonlines one:
    with jsonlines.open(file) as comments:
        # For each line (i.e. metadata data-points for one comment) do:
        for comment in comments:
            # Extract the comment id ('cid') and save it to a variable
            comment_id = str(comment["cid"])
            print(f"Processing comment {comment_id}")
            # Check if the 'cid' contains a full stop character. If so, the comment is a reply to another comment: take the string on
            # the left of the full stop and assign it as value of the attribute 'comment_id', then the string on the right and assign
            # it as value of the attribute 'comment_reply_to' to preserve the original hierarchical structure
            if re.search("(.*?)\.(.*)", comment_id) is not None:
                comment_reply_to = str(
                    re.search("(.*?)\.(.*)", comment_id).group(1)
                )
                comment_id = str(
                    re.search("(.*?)\.(.*)", comment_id).group(2)
                )
            # If there is no full stop character, assign the 'comment_id' as value of the <comment> attribute 'comment_id' and the
            # value 'na' to the 'comment_reply_to' attribute
            else:
                comment_id = comment_id
                comment_reply_to = "na"

            # Extract other metadata data-points and assign them to a set of variables
            username = str(comment["author"])
            votes = str(comment["votes"])
            heart = str(comment["heart"])
            comment_timestamp = comment["time_parsed"]
            
            # At last, get the content of the comment (the actual message)
            comment_text = str(comment["text"])
            
            '''
            # Calculate the sentiment of the comment, and extract the four results to four different variables
            sa_text = analyzer.polarity_scores(comment_text)
            negative = sa_text["neg"]
            neutral = sa_text["neu"]
            positive = sa_text["pos"]
            compound = sa_text["compound"]
            
            # append all the extracted data to the list, formatting it as a csv line
            data.append([comment_timestamp, comment_id, comment_reply_to, username, comment_text, negative, neutral, positive, compound])
            '''
        # after all the comments have been extracted, sort them in chronological order using their timestamps
        data.sort(key=operator.itemgetter(0))
        
        # add a progressive number to the newly ordered comments, to preserve the chronological order
        for index, element in enumerate(data, start=1):
            element.insert(0, index)
        '''    
        # create a dataframe with all the collected comments
        csv_df = pd.DataFrame(data, columns=["turn", "comment_timestamp", "comment_id", "reply_to", "username", "comment_text", "negative", "neutral", "positive", "compound"])
        # write the dataframe to a csv file
        csv_df.to_csv(output_filename, sep="\t", index=False)
        '''