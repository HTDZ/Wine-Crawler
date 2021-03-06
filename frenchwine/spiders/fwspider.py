#french wine spider

from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from frenchwine.items import FrenchwineItem

class FrenchwineSpider(BaseSpider):
	handle_httpstatus_list = [403, 404]
	name = "frenchwine"
	allowed_domains = ["wine-searcher.com"]
	start_urls = []
	step = 25
	i = 1
	while i <= 7626:
	    url = "http://www.wine-searcher.com/biz/producers/france?s=" + str(i)
	    i = i + step
	    start_urls.append(url)
#	print start_urls
	def    parse(self, response):
	    item = FrenchwineItem()
	    sel = Selector(response)
	    items = []
#	    item["title"] = sel.xpath('//td[@class="wlrwdt wlbdrl vtop"]/a/text()').extract() 
#	    item["title_bot"] = sel.xpath('//td[@class="wlrwdt wlbdrl noborderbtm vtop"]/a/text()').extract()
	    item["link"] = sel.xpath('//td[@class="wlrwdt wlbdrl vtop"]/a/@href').extract()
	    item["link_bot"] = sel.xpath('//td[@class="wlrwdt wlbdrl noborderbtm vtop"]/a/href').extract()
	    items.append(item)
	    return items
		
