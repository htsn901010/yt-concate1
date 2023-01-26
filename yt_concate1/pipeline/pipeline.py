from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils)  # video URL links list
            except StepException as e:
                print('Exception happended:', e)
                break
