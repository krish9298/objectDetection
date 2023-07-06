import sys
from detection import convert_to_photo
from detection_fast import convert_to_photo_fast
import time


def timeStamp(list_time):

    format_time = dict()
    i = 0
    for time in list_time:
        m, s = divmod(time, 60)
        h, m = divmod(m, 60)
        format_time[str(i)] = {"%dh%02dm%02ds" % (h, m, s): time}
        i += 1
    return format_time


argument = sys.argv[1:]
count = len(argument)
if count != 3:
    print("Usage: [main.py] [video_path] [keyword] [type]")
else:
    file_path = argument[0]
    keyword = argument[1]
    algo_type = argument[2]

    algo_type = algo_type.lower()

    result = []
    start = time.time()
    if algo_type == 'fast':
        result = convert_to_photo_fast(file_path, keyword)

    elif algo_type == 'slow':
        result = convert_to_photo(file_path, keyword)
    end = time.time()
    final_result = timeStamp(result)

    for i, time in final_result.items():
        print(i, ": ", time)
    print('\n')
    print('Net running time: ',end-start)
