# Analysing the sentiment of Youtube comments

1. First, let's install the required tools:

> `pip install youtube-comment-downloader vaderSentiment jsonlines`

1. Then we need to download some comments

> `youtube-comment-downloader --url "https://www.youtube.com/watch?v=IDCODE" --output name_of_output.jsonl`

1. Now we can use the [yt-comments_sentimentAnalysis.ipynb](https://github.com/mdic/dh2023/blob/main/06_050423/yt-comments_sentimentAnalysis.ipynb) script to automatically calculate the sentiment for the downloaded comments
Download the [script](https://github.com/mdic/dh2023/blob/main/06_050423/yt-comments_sentimentAnalysis.ipynb) in the same folder where you downloaded the Youtube comments: open the link, then click on `Raw`; save the page that opens inside your project's folder, by naming it `yt-comments_sentimentAnalysis.ipynb` (delete the `.txt` extension at the end of the filename if present once the file is saved).  
Then open the script in Jupyter and run the two blocks. The script will generate a spreadsheet with one comment per row, as exemplified below

| turn |   |   | comment_timestamp |   |   | comment_id                 |   |   | reply_to |   |   | username |   |   | comment_text                                                                                     |   |   | negative |   |   | neutral |   |   | positive |   |   | compound |
|------|---|---|-------------------|---|---|----------------------------|---|---|----------|---|---|----------|---|---|--------------------------------------------------------------------------------------------------|---|---|----------|---|---|---------|---|---|----------|---|---|----------|
| 1    |   |   | 1662300046.944393 |   |   | UgxRqHRnwAelIPmIW454AaABAg |   |   | na       |   |   | Kosmic   |   |   | Be sure to follow the Twitch stream so you can participate next time!http://www.twitch.tv/kosmic |   |   | 0.0      |   |   | 0.834   |   |   | 0.166    |   |   | 0.3802   |
| 2    |   |   | 1662300047.005199 |   |   | UgznIlEE37xTnzLvj9d4AaABAg |   |   | na       |   |   | Falkite  |   |   | that was easy! all mario had to do was break the sound barrier                                   |   |   | 0.096    |   |   | 0.701   |   |   | 0.203    |   |   | 0.4003   |
