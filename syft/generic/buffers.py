from collections import OrderedDict
from syft.generic.object import AbstractObject


class Buffers(AbstractObject):
    """ The purpose of this class is to maintain all the buffer information
    that are generated by the model which are not recognised as parameters"""
    def __init__(self):
        super().__init__()
        self.buffer = OrderedDict()

    # Gathers buffer from torch's nn.Module and stores it in buffer dictionary
    def named_buffer(self, nn_self):
        for name, buf in nn_self.named_buffers():
            self.buffer[name] = buf

    # Returns the values in stored buffer
    def get_buffer(self):
        return self.buffer