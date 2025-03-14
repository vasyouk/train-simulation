from datetime import datetime, timedelta
from modules.initialize import from_json
import json

INPUT_JSON_FILE_PATH = "input_train_sim.json"
with open(INPUT_JSON_FILE_PATH, "r") as file:
    json_database = json.load(file)
data = from_json(json_database)

# function (road Raduzhney-Polyarny)
def go_away(distance, speed):
    for train in data["trains"]:
        # distance = {roads.distance}  # подключить roads distance
        distance = self.road.distance
        speed = self.train.speed
        time_required_hours = distance / speed
        hours = int(time_required_hours)
        minutes = int((time_required_hours - hours) * 60)
        start_time = datetime(2021, 11, 1, 0, 0, 0)
        time_delta = timedelta(hours=hours, minutes=minutes) #
        end_time = start_time + time_delta
        time_train = end_time, self.train.name # запись
        return time_train
print (go_away())
    


