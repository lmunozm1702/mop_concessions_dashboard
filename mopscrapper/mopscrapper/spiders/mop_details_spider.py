import scrapy
import json


class MopDetailsSpiderSpider(scrapy.Spider):
    name = "mop_details_spider"
    allowed_domains = ["concesiones.mop.gob.cl"]
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(MopDetailsSpiderSpider, self).__init__(*args, **kwargs)
        self.start_urls = self.get_urls('https://concesiones.mop.gob.cl', 'mopspider.json')

    def get_urls(self, domain, filename):
        ''' 
        get the urls from the json file

        Parameters
        ----------  
        domain: str
            domain of the website
        filename: str
            name of the json file

        Returns
        -------
        list
            list of urls
        '''

        lines = []
        urls = []
        
        #open the json file and get the urls
        with open(filename, 'r') as f:
            lines = json.load(f)
        
        #get the urls and add the domain
        for line in lines:
            urls.append(domain + line['link'])

        return urls
    
    def parse(self, response):
        details_data = response.css('p.fecha')
        result = {
            'id': response.url.split('?')[1].split('=')[1],
            'status': self.get_status(response.url.split('?')[0]),
            'url': response.url,
        }
        for detail in details_data:
            data = self.parse_detail(detail)
            if data != None:
                result[data[0]] = data[1]

        yield result


    def parse_detail(self, detail):
        result = []
        result = detail.css('p.fecha').get().split('</b>')
        if len(result) == 2:
            result[0] = result[0].replace('<p class="fecha"><b>', '').replace(':', '').strip()
            result[1] = result[1].replace('\"', '').replace('</p>', '').strip()
            return result
        else:
            return None
    
    def get_status(self, url):
        result = url.split('/')[-1].split('.')[0]
        match result:
            case 'detalleHidricas':
                return 'Construcción'
            case 'detalleExplotacion':
                return 'Operación'
            case 'detalleConstruccion':
                return 'Construcción y Operación'
            case 'Detalleconcesionesfinalizadas':
                return 'Finalizada'
            case 'detalle_adjudicacion':
                return 'Adjudicación'
            case _:
                return 'Desconocido'