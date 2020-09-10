import os
import json
import stepper
from config import get_config


def get_state():
    with open("state.json") as file:
        return json.load(file)


def set_state(stepper_position):
    with open("state.json") as file:
        return json.dump({"stepper_position": stepper_position}, file)


def get_stepper_position(position, config):
    return position / 100 * config["steps_in_range"]


def adjust(position):
    config = get_config()
    stepper_position = get_stepper_position(position, config)
    state = get_state()
    if state["stepper_position"] != stepper_position:
        steps = stepper_position - state["stepper_position"]
        stepper.step(steps, config["interstep_delay"])
        set_state(stepper_position)
