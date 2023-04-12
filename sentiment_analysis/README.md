# Analysing the sentiment of Youtube comments using AI

1. First, let's install the required tools using the command below. This is the first of two downloads whose size may exceed 250MB, so be patient and only install them if you have an unmetered internet connection!

> `pip install transformers torch torchvision torchaudio`

2. Now open the [`yt-comments_sentimentAnalysis-AI.ipynb`](https://github.com/mdic/dh2023/blob/main/sentiment_analysis/yt-comments_sentimentAnalysis-AI.ipynb) script, and download it in the same folder where you downloaded the Youtube comments. As usual, open the link, then click on `Raw`; save the page that opens inside your project's folder, by naming it `yt-comments_sentimentAnalysis-AI.ipynb`.
3. Open the newly downloaded script in Jupyter after using the command below in your terminal to start Jupyter Lab:

> `jupyter lab`

4. If the script does not show the usual code blocks, right-click on the file and delete the `.txt` extension at the end of the filename if present once the file is saved). Then reopen the script and run the two blocks. **The first time you run the script, it will download the language model for sentiment analysis (approx. 280MB) so it will take some time (this step is not shown in the video further below)**.

5. Once the script has finished working, you will find a new `.csv` file in your folder: double-click on it and select "Tab" as "Delimiter" to correctly see the results. These are structured as exemplified below, and as you can see they include both the sentiment analysis calculated through the already-seen predefined-dictionary approach (columns `negative`, `neutral`, `positive`, `compound`), and the ones calculated by the newly-implemented AI (columns `anger`, `fear`, `love`, `surprise`, `joy`, `sadness`).  Predefined-dictionary calculated sentiment used four categories, with `compound` being a summary of the other three ones, and with values ranging from 0 (no presence of the sentiment) to 1 (max presence of the sentiment). AI-calculated sentiment is based on six different scores, each one referring to a different "sentiment" (see column names), with values ranging from 0 to 1 - where 1 indicates "certain" presence of the sentiment, and 0 absence.

| turn |   |   | comment_timestamp |   |   | comment_id                 |   |   | reply_to |   |   | username      |   |   | comment_text                                                                                     |   |   | negative |   |   | neutral |   |   | positive |   |   | compound |   |   | fear                  |   |   | joy                |   |   | anger                 |   |   | sadness              |   |   | love                  |   |   | surprise              |
|------|---|---|-------------------|---|---|----------------------------|---|---|----------|---|---|---------------|---|---|--------------------------------------------------------------------------------------------------|---|---|----------|---|---|---------|---|---|----------|---|---|----------|---|---|-----------------------|---|---|--------------------|---|---|-----------------------|---|---|----------------------|---|---|-----------------------|---|---|-----------------------|
| 1    |   |   | 1662545274.889934 |   |   | UgxRqHRnwAelIPmIW454AaABAg |   |   | na       |   |   | Kosmic        |   |   | Be sure to follow the Twitch stream so you can participate next time!http://www.twitch.tv/kosmic |   |   | 0.0      |   |   | 0.834   |   |   | 0.166    |   |   | 0.3802   |   |   | 0.0006110440008342266 |   |   | 0.9969204664230347 |   |   | 0.0010109911672770977 |   |   | 0.000612446223385632 |   |   | 0.0005889174644835293 |   |   | 0.0002562185109127313 |
| 2    |   |   | 1662545274.968195 |   |   | UgxYMZCFRGykyzF1GJt4AaABAg |   |   | na       |   |   | Brendan Rizzo |   |   | Once humans tie the TAS all the way through, this will become a legit category.                  |   |   | 0.0      |   |   | 1.0     |   |   | 0.0      |   |   | 0.0      |   |   | 0.04108056798577309   |   |   | 0.8597100377082825 |   |   | 0.08644036203622818   |   |   | 0.00863378494977951  |   |   | 0.0023000056389719248 |   |   | 0.0018352839397266507 |
  
  
Steps 2-5 can be reviewed in the video below:


https://user-images.githubusercontent.com/13422439/231217788-b1ca3db4-f548-4ef8-b808-569f8609d75f.mp4


