from bs4 import BeautifulSoup
from util import url_builder
import aiohttp
import asyncio
from backend.DB import Query
from log_config import get_logger
from DataTypes import Query, Date
from datetime import datetime, timedelta

logger = get_logger(__name__)


class Scraper:
    
    def __init__(self, fuel: str, area: str, station: str):
        logger.debug(f"Scraper object created with fuel: {fuel}, area: {area}, station: {station}")
        self.url = url_builder(fuel, area, station)

    async def fetch_page(self, session: aiohttp.ClientSession) -> str:
        async with session.get(self.url) as response:
            response.raise_for_status()
            return await response.text()
            
    async def get_data(self) -> Query:
        async with aiohttp.ClientSession() as session:
            page_content = await self.fetch_page(session)
            self.parse_gas_prices(page_content)
            
    def convert_time_passed_to_date_time(self, time_passed: str) -> Date:
        logger.debug(f"Converting time passed to date time: {time_passed}")
        hours = int(time_passed.split()[0])
        current_time = datetime.now()
        new_time = current_time - timedelta(hours=hours)
        date = Date(new_time.year, new_time.month, new_time.day)
        logger.debug(f"Converted time: {date}")
        return date

    def parse_available_stations(self, content: str):
        soup = BeautifulSoup(content, 'html.parser')
        dropdown = soup.find('select', {'id': 'ctl00_Content_P_PSC1_lstStations'})
        options = dropdown.find_all('option')
        option_values = [option.text for option in options]
        return option_values
        
        
    def parse_available_areas(self, content: str):
        soup = BeautifulSoup(content, 'html.parser')
        dropdown = soup.find('select', {'id': 'ctl00_Content_P_PSC1_lstAreas'})
        options = dropdown.find_all('option')
        option_values = [option.text for option in options]
        return option_values

    def parse_gas_prices(self, content: str):
        soup = BeautifulSoup(content, 'html.parser')
        rows = soup.find_all('tr') 
        
        for row in rows:
            price: float = float(row.find('div', class_='price_num').text.strip())
            station_name: str = row.find('dt').text.strip()  
            address: str = row.find('dd').text.strip()  
            area: str = row.find('a', class_='p_area').text.strip()  
            report_time: str = row.find('div', class_='tm').text.strip() 
            report_date: Date = self.convert_time_passed_to_date_time(report_time)
            
            logger.debug(f"Price: {price}")
            logger.debug(f"Station Name: {station_name}")
            logger.debug(f"Address: {address}")
            logger.debug(f"Area: {area}")
            logger.debug(f"Report Date: {report_date}")
            logger.debug("-------------")
            
        
