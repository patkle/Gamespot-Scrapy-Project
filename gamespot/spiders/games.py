from scrapy import Request, Spider


class GamesSpider(Spider):
    name = "games"

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.pages = int(kwargs.get("pages", 10))

    def start_requests(self):
        for i in range(1, self.pages + 1):
            yield Request(f"https://www.gamespot.com/games/reviews/?review_filter_type%5Bplatform%5D=all&review_filter_type%5Bgenre%5D=&review_filter_type%5BtimeFrame%5D=&review_filter_type%5BstartDate%5D=&review_filter_type%5BendDate%5D=&review_filter_type%5BminRating%5D=&review_filter_type%5Btheme%5D=&review_filter_type%5Bregion%5D=&review_filter_type%5Bletter%5D=&sort=gs_score_desc&page={i}")

    def parse(self, response):
        for card in response.xpath(".//div[contains(@class, 'card-item__main')]"):
            yield {
                "platforms": card.xpath(".//div[@class='card-item__content ']/span/text()").get(),
                "title": card.xpath(".//h4[@class='card-item__title ']/text()").get().split("Review")[0].strip(),
                "score": card.xpath(".//div[contains(@class, 'review-ring-score__score')]/text()").get(),
                "score_text": card.xpath(".//span[contains(@class, 'review-ring-score__text')]/text()").get(),
                "updated_on": card.xpath(".//time/@datetime").get(),
                "no_of_comments": card.xpath(".//div[@class='card-metadata ']/div[2]/span/text()").get(),
                "no_of_upvotes": card.xpath(".//div[@class='card-metadata ']/div[3]/span/text()").get(),
            }
