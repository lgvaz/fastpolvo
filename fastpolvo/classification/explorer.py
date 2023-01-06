# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/05a_classification.explorer.ipynb.

# %% auto 0
__all__ = ['DataExplorer']

# %% ../../nbs/05a_classification.explorer.ipynb 4
from fastai.vision.all import *
import polvo as pv

# %% ../../nbs/05a_classification.explorer.ipynb 5
class DataExplorer(pv.classification.DataExplorer):
    def __init__(self, x_tl, y_tl): 
        id2label = y_tl.vocab.__getitem__
        label2id = {l: i for i, l in enumerate(y_tl.vocab)}.__getitem__
        super().__init__(y_tl, x_tl.__getitem__, id2label, label2id)
        
    @classmethod
    def from_datasets(cls, dss):
        return cls(dss.tls[0], dss.tls[1])
