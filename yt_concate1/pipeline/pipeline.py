from .steps.step import StepException


class Pipeline:
    def __int__(self, steps):
        self.steps = steps

    def run(self, data, inputs):
        data = None
        for step in self.steps:
            try:
                data = step.prcoess(data, inputs)
            except StepException as e:
                print('Exception happend:', e)
                break
