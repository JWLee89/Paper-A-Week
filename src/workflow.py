

class Trainer:
    """
    A trainer is responsible for training a model.
    During the whole training cycle, there are always common processes.

    1. Prepare the dataset
        - Dataset must be prepared prior to training. This process involves
            1. Retrieving the dataset (stored online or on local disk)
            2. Preprocessing the data (transform the data for training network)
                - Augmentation, normalization, data cleaning etc.

    2. Prepare model
        - Before training a model it must be initialized. We can initialize the mode
        in the following ways.
            1. A framework may consist of multiple models

    3 Training the model


    Unlike other frameworks which restrict certain actions,
    the workflow model provides a set of templates to abide by while
    retaining the freedom of how to implement the training algorithm.

    To do so, we must minimize the bells and whistles, only providing the bare
    minimum to maximize the flexibility and freedom of developers. 
    """
    def __init__(self):
        pass

    def _prepare_dataset(self):
        pass

    def train(self):
        pass
