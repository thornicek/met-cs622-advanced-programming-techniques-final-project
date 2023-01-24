# Final Project Tomas Hornicke CS622


My final project takes a keyword and downloades all the video based on the keyword from instagram and youtube. It then splits them into different scenes.

Note on presentation video: The reason why I couldn't split the scenes for the youtube video was because it only showed lyrics and the scene detect didn't detect a change of scene.

# Required libraries

tkinter
os
instaloader
selenium
webdriver
scenedetect

# Structure

My project is built using the Tkinter GUI for python. It consists of 4 python files; instagram.py, main.py, scenes.py and youtube_download.py

The main.py only has the template for the GUI, with the buttons containing functions for the downloading and splitting the videos from youtube and instagram.

The scenes.py file contains the find_scenes(), which uses scene detect Api to split the videos into different scenes.

The instagram.py file contains the download_instagram(), which initializes instaloader and downloads all the media from the hashtag keyword search into the Download_Instagram folder. It then has the keep_mp4_split(), which keeps all the video media and gets rid of all other types of media, it also calls the find_scenes() from scenes.py to split the video into different scenes. Finally the download_split_ig() calls the other two functions and is used for the GUI.

The youtube_download.py file has the get_links(), which uses selenium and the chrome driver to open the youtube search page and scrape all the urls into a list. Then the download_videos() downloads the videos into Downloads folder. The download_split() then calls the other two methods in the file along with the find_scenes() to split the files in the Downloads folder into scenes into the Split folder.

# Warning

Social media platforms are actively blocking bots and users from web scrapping their platform. Therefore in the near future, it is possible that API's, such as instaloader, can be blocked. 

Also be aware of trying to scrape the instagram platform too many times in one day. Instagram will assume you are a bot and will block the web scrapping.