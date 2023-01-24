from __future__ import unicode_literals

from typing import List, Optional

import youtube_dl
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from scenes import find_scenes

from selenium.webdriver.remote.webelement import WebElement



def download_split(keyword):
    """
    Given a query keyword, download and split videos by calling the find_scenes() and download_videos()

    :param keyword: term to search on Youtube
    :return: True if video downloaded and split, False if error occurs
    """
    try:
        links = get_links(keyword)
        video_locations = download_videos(links, keyword)
        for video_location in video_locations:
            find_scenes(video_location)
        return True
    except Exception:
        return False



def get_links(query: str) -> List[str]:
    """
    Given a query, download all Youtube video results on the first page.

    :param query: term to search on Youtube
    :return: list of links to videos on first results page
    """
    keywords = query.split(" ")
    url_params: Optional[str] = None
    if len(keywords) > 1:
        url_params = "+".join(keywords)
    else:
        url_params = query
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.youtube.com/results?search_query=" + url_params)

    # find url by xpath and put into links list
    video_elements: List[WebElement] = driver.find_elements("xpath", '//*[@id="video-title"]')
    links: List[str] = []
    for web_element in video_elements:
        links.append(web_element.get_attribute('href'))
    # print links list
    print(links)
    # get rid of the first None object in the list
    links.pop(0)
    return links


# method to download videos from list into Downloads dir
def download_videos(video_links_list: List[str], keyword) -> List[str]:
    """
    Given a list of youtube links, download the videos.

    :param video_links_list: list of links to youtube videos
    :param download_options: dict containing download options regarding video/sound quality
    :return: None
    """
    video_locations = []
    for count, video_link in enumerate(video_links_list):
        file_location = f'./Downloads/{keyword}_{count}.mp4'
        video_locations.append(file_location)
        download_options: dict = {'outtmpl': f'{file_location}'}
        with youtube_dl.YoutubeDL(download_options) as ydl:
            ydl.download([f'{video_link}'])
    return video_locations




