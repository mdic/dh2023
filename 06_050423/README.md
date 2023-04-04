# Analysing the sentiment of Youtube comments

1. First, let's install the required tools:

> `pip install youtube-comment-downloader vaderSentiment jsonlines`

1. Then we need to download some comments

> `youtube-comment-downloader --url "https://www.youtube.com/watch?v=IDCODE" --output name_of_output.jsonl`

1. Now we can use the [yt-comments_sentimentAnalysis.ipynb]() script to automatically calculate the sentiment for the downloaded comments
Download the [script]() in the same folder where you downloaded the Youtube comments, and run the two blocks. The script will generate a spreadsheet, with one comment per row.