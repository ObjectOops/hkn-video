#!/bin/bash

ffmpeg -f concat -safe 0 -i video_list.txt full_video.mp4
