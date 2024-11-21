import scrapy


class MopspiderSpider(scrapy.Spider):
    name = "mopspider"
    allowed_domains = ["concesiones.mop.gob.cl"]
    start_urls = ["https://concesiones.mop.gob.cl/proyectos/Paginas/construccion.aspx",
                  "https://concesiones.mop.gob.cl/proyectos/Paginas/proyectos_operacion.aspx",
                  "https://concesiones.mop.gob.cl/proyectos/Paginas/proyectos_Operacion_%20Construccion.aspx",
                  "https://concesiones.mop.gob.cl/proyectos/Paginas/Concesionesfinalizadas.aspx"]

    def parse(self, response):
        pages = response.css('li')        
        for page in pages:
            if page.css('a::attr(href)').get()[0:4] != 'http':
                yield {
                    'name': page.css('a::text').get(),
                    'link': page.css('a::attr(href)').get(),
                    'id': page.css('a::attr(href)').get().split('?')[1].split('=')[1]
                }

