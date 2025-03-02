# Data Crawler X
A Simple crawler using python and tweepy.

## How it works?
1. The script will connect to the Twitter API using your credentials.
2. It will then search for tweets containing the keyword you specified.
3. The script will then print out the tweets it found.
4. The script will also save the tweets to a csv file.

## How to use?
1. Install the required libraries by running
```bash
pip install -r requirements.txt
```

2. Place your `API` and `ACCESS` token into `.env.example` and rename it into `.env`
> You can get the token by creating an app on the Twitter Developer Dashboard. Refer to [this platform](https://developer.x.com) for more information.

3. Run the script by running
```bash
python main.py
```
Then, input keyword and data count.

4. The file will be saved as `CSV` and `JSON` files.