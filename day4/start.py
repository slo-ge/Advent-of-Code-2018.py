import datetime
from collections import Counter


class TaskLine(object):

    def __init__(self, time, task):
        self.time = time
        self.task = task


with open('input', 'r') as input:
    time_tracks = input.read().splitlines()


    def sanitize_track_line(line):
        time, task = line.split("]")
        time = datetime.datetime.strptime(time[1:], '%Y-%m-%d %H:%M')
        if '#' in task:
            task = task.split(' ')[2]  # starts shift, only id returned

        return TaskLine(time, task)


    sanitized_tracks = [sanitize_track_line(line) for line in time_tracks]
    sanitized_tracks.sort(key=lambda l: l.time)
    to_id = {}
    current_id = ''

    for track in sanitized_tracks:
        if track.task.startswith('#'):
            current_id = track.task
            if current_id not in to_id:
                to_id[current_id] = []
        else:
            to_id[current_id].append(track)
            value = track

    highest = {'sum': 0, 'minutes': []}
    max_minutes_asleep = {'id': '', 'minute': 0, 'times': 0}
    for key, value in to_id.items():
        sum_minutes_asleep = 0
        exact_minutes = []

        for i in range(0, len(value), 2):
            asleep = value[i]
            awake = value[i + 1]
            sum_minutes_asleep += awake.time.minute - asleep.time.minute

            for minute in range(asleep.time.minute, awake.time.minute):
                exact_minutes.append(minute)

        if sum_minutes_asleep > highest['sum']:
            highest = {'id': key, 'sum': sum_minutes_asleep, 'minutes': exact_minutes}

        # TODO: PART 2
        try:
            minute, times = Counter(exact_minutes).most_common(1)[0]
            if times > max_minutes_asleep['times']:
                max_minutes_asleep = {'id': key, 'minute': minute, 'times': times}
        except IndexError:
            pass

    minute, times = Counter(highest['minutes']).most_common(1)[0]
    print('Part 1:', int(highest['id'][1:]) * minute)
    print('Part 2:', int(max_minutes_asleep['id'][1:]) * max_minutes_asleep['minute'])
