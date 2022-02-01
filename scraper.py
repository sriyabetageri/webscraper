from re import template
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("/Library/Application Support/Google/Chrome")


def scrape():
    headers = ["name","light_years_from_earth", "planet_mass","stellar_magnitude","discovery_date"]
    planet_data = []
    soup = BeautifulSoup(browser.page_source,"html.parcer")
    for ul_tag in soup.find_all("ul", attrs={"class","exoplanet"}):
        li_tags = ul_tag.find_all("li")
        temp_list = []
        for index, li_tag in enumerate(li_tags):
            if index == 0: 
                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")
        planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

scrape()
