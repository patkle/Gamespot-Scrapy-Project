from scrapy import Request, Spider


class GameFAQsRankingsSpider(Spider):
    name = "gamefaqsrankings"

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.pages = int(kwargs.get("pages", 10))

    def start_requests(self):
        for i in range(1, self.pages + 1):
            yield Request(f"https://gamefaqs.gamespot.com/games/rankings?list_type=rate&view_type=1&min_votes=2&page={i}")

    def parse(self, response):
        for row in response.xpath(".//table/tbody/tr"):
            title = row.xpath("./td/a/text()").get()
            platform = row.xpath("./td/span/text()").get()
            _, rating, dificulty, length = row.xpath("./td/text()").getall()
            yield {
                "title": title,
                "platform": platform,
                "rating": rating,
                "dificulty": dificulty,
                "length": length,
            }
