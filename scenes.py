import os

import scenedetect
from scenedetect import open_video, ContentDetector, SceneManager, StatsManager


def find_scenes(video_path):
    """
    Given a video path, split all the video files into seperate scenes
    :param video_path: path were the downloaded videos resides
    :return:
    """
    video_stream = open_video(video_path)
    stats_manager = StatsManager()
    # Construct our SceneManager and pass it our StatsManager.
    scene_manager = SceneManager(stats_manager)
    # Add ContentDetector algorithm (each detector's constructor
    # takes various options, e.g. threshold).
    scene_manager.add_detector(ContentDetector())
    # Save calculated metrics for each frame to {VIDEO_PATH}.stats.csv.
    stats_file_path = '%s.stats.csv' % video_path
    # Perform scene detection.
    scene_manager.detect_scenes(video=video_stream)
    scene_list = scene_manager.get_scene_list()
    print(scene_list)
    for i, scene in enumerate(scene_list):
        print(
            'Scene %2d: Start %s / Frame %d, End %s / Frame %d' % (
                i + 1,
                scene[0].get_timecode(), scene[0].get_frames(),
                scene[1].get_timecode(), scene[1].get_frames(),))
    scenedetect.video_splitter.split_video_mkvmerge(video_path, scene_list,
                                                    output_file_template='./Split/$VIDEO_NAME.mkv', video_name=None,
                                                    show_output=False, suppress_output=None)



