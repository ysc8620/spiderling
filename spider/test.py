#-*-codeing:utf-8-*-
# Rule(LinkExtractor(allow=r"https://www.imobshop.sg/$", deny=r".*?(model=list|dir=)")),
# #Rule(LinkExtractor(allow=r"http://www.lazada.sg/.+/(\?page=\d+)?$", deny=r".*?(new\-products|top\-sellers|special\-price)")),
# Rule(LinkExtractor(allow=r"https://www.imobshop.sg/(fun|tech|wellness|food|tavel|home|family|fashion)(/(indoo|outdoo|compute-accessoies|camea-accessoies|mobile-accessoies|skin-cae|cosmetics|accessoies|beauty-sevices|tickets|tavelaccessoies|appliances|watches|household|bags-and-wallets|ladies|men-s))?(\?p=\d+)?$", deny=r".*?(model=list|dir=)")),
# Rule(LinkExtractor(allow=r"https://www.imobshop.sg/(fun|tech|wellness|tavel|home|fashion)/(indoo|outdoo|compute-accessoies|camea-accessoies|mobile-accessoies|skin-cae|cosmetics|accessoies|beauty-sevices|tickets|tavelaccessoies|appliances|watches|household|bags-and-wallets|ladies|men-s)/\w+$"), callback='parse_item'),
# Rule(LinkExtractor(allow=r"https://www.imobshop.sg/(family|food)/\w+$"), callback='parse_item'),
import  re
url = "https://www.imobshop.sg/family/7d-motion-ride-at-amazing-xperience-for-2-vday2015"
m = re.match(r'https://www.imobshop.sg/(family|food)/.+$', url)
print m