import os
from instaloader import Instaloader, Hashtag
from scenes import find_scenes

def download_instagram(keyword, path):
    """
    Given a path and query, download all posts to the given path

    :param keyword: query to search
    :param path: target download path
    :return:
    """
    print("running...")
    L = Instaloader()
    hashtag = Hashtag.from_name(L.context, keyword)
    for post in hashtag.get_top_posts():
        print("looping")
        L.download_post(post, target= path[2:])
    print("finished..")


def keep_mp4_split(path):
    """
    Given a path, delete all the non videos from directory and split the video files into scenes.

    :param path: target path for download
    :return:
    """
    for file in os.listdir(path):
        if not file.endswith(".mp4"):
            os.remove(path + "/" + file)
        else:
            print(path + "/" + file)
            find_scenes(path + "/" + file)



def download_split_ig(keyword):
    """
    Given a query keyword, downlaod videos and split into scenes
    :param keyword: query to search
    :return:
    """
    try:
        path = "./Download_Instagram"
        download_instagram(keyword, path)
        keep_mp4_split(path)
        return True
    except Exception as e:
        print(e)
        return False




