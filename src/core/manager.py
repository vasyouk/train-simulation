from __future__ import annotations
from .other import Other
from .road import Road
from .terminal import Terminal
from .train import Train



class Manager:
    def __init__(self, trains, terminals, roads, other):
        self.trains: list[Train] = []
        self.terminals: list[Terminal] = []
        self.roads: list[Road] = []
        self.other: list[Other] = []

    def from_json(json_dict: dict) -> Manager:
        trains = []
        terminals = []
        roads = []
        other = None

        for train_json in json_dict.get("trains", []):
            train = Train(**train_json)
            trains.append(train)

        for terminal_json in json_dict.get("terminals", []):
            terminal = Terminal(**terminal_json)
            terminals.append(terminal)

        for road_json in json_dict.get("roads", []):
            road = Road(**road_json)
            roads.append(road)

        other = Other(**json_dict.get("other", {}))
        return Manager(trains, terminals, roads, other)

   