"""
Simple Python implementation to convert video file formats.
Depending on the file size the time to convert can take a while.
Also the video file(s) you wish to alter must be in the same directory as the code file.

:params input_file_type - input file(s) type example .mkv, .avi, ...
:params output_file_type - out file(s) type, what type do you desire (type must be included in ffmpeg).

Modules used:
Glob - included in Anaconda Python packages.
FFmpy - can be downloaded using pip install.
FFmpeg is needed in order to run FFmpy, which can be found at https://ffmpeg.org/
"""

from ffmpy import FFmpeg
import glob

# Variables to change input find type and output file type. These are the only instances that need to be altered.
input_file_type = '.mkv'
output_file_type = '.mp4'

# Glob: Find all files (*) with a type that matches input_file_type variable (.mkv by default).
file_list = glob.glob('*' + input_file_type)
print(file_list)

# For each file found by glob in the list, save it as the converted file type using the original name.
for i in range(0, len(file_list)):
    # Split on suffix.
    video = file_list[i].split(input_file_type)
    # print(video)

    # Save the original name without the suffix.
    file_title = video[0]
    # print(file_title)

    # Construct the files needed using the name and input and output types.
    input_file = file_title + input_file_type
    output_file = file_title + output_file_type
    # print(input_file)
    # print(output_file)

    # call the FFmpeg constructor.
    ff = FFmpeg(inputs={input_file: None}, outputs={output_file: None})
    # Run the constructor and save after conversion is complete.
    ff.run()
