# Gamespot Scrapy Project

This project is configured to be hosted on [Scrapy Cloud](https://www.zyte.com/scrapy-cloud/).  

It uses [Zyte Smart Proxy Manager](https://scrapinghub.com/?rfsn=4170080.0597ad) as proxy service.  

The dataset for data from [gamespot.com](https://www.gamespot.com/) can be found [here](https://www.kaggle.com/datasets/patkle/all-video-game-review-scores-from-gamespotcom).  
A Jupyter Notebook with some EDA on that data can be found [here](https://www.kaggle.com/patkle/gamespot-score-analysis-playground).  
The dataset for [gamefaqs.gamespot.com](https://gamefaqs.gamespot.com/games/rankings?list_type=rate&view_type=1&min_votes=2) is hosted [here](https://www.kaggle.com/datasets/patkle/gamefaqs-82100-rankings-length-and-difficulty) with the notebook [here](https://www.kaggle.com/patkle/gamefaqs-rankings-exploration).

## games

The spider can be ran with
```zsh
python3 -m scrapy crawl games -a pages=5 -O games.csv
```

## gamefaqsrankings

The spider can be ran with
```zsh
python3 -m scrapy crawl gamefaqsrankings -a pages=5 -O gamefaqsrankings.csv
```

### Arguments

With `-a` you can specify arguments for the spider.  

|argument   |type  |description   | 
|---|---|---|
|pages   |int   |number of pages to scrape   |


## Setting up locally
  
When setting up this project locally you must create a **.env** file with the following data:  

|setting   |description   |  
|---|---|
|ZYTE_SMARTPROXY_APIKEY   |your smart proxy manager api key   |
  

## Deploy to Scrapy Cloud
There's a shortcut in the Makefile, just running `make deploy` will deploy the project to Scrapy Cloud (given that you provided the project ID in `scrapinghub.yml`).Don't forget to add the following settings in your cloud project's settings:
|setting   |description   | 
|---|---|
|ZYTE_SMARTPROXY_APIKEY   |your smart proxy manager api key   |
  
## Also, 
you could [buy me a coffe](https://www.buymeacoffee.com/kleinp) if you wanted to. I'd really appreciate that.  
