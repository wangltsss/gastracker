from urllib.parse import urlencode
from log_config import get_logger

logger = get_logger(__name__)


def url_builder(fuel: str, area: str, station: str) -> str:
    logger.debug(f"Building URL with fuel: {fuel}, area: {area}, station: {station}")
    base_url = "https://www.kwgasprices.com/GasPriceSearch.aspx?typ=adv&fuel={}&srch=1&state=ON&site=KW,Toronto&tme_limit=24".format(fuel.capitalize())
    params = {}
    if area:
        params['area'] = area.capitalize()
    if station:
        params['station'] = station.capitalize()
    query_string = urlencode(params)
    logger.debug(f"URL built: {base_url + '&' + query_string}")
    return base_url + '&' + query_string
