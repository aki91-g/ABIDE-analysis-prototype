from nilearn.maskers import NiftiLabelsMasker
from nilearn import datasets
from typing import List, Dict
import numpy as np
import os

def extract_timeseries(func_paths: List[str]) -> Dict[str, np.ndarray]:
    """_NIfTI → AAL timeseris_

    Args:
        func_paths (List[str]): _description_

    Returns:
        Dict[str, np.ndarray]: _description_
    """
    atlas = datasets.fetch_atlas_aal()
    masker = NiftiLabelsMasker(
        labels_img=atlas.maps, 
        standardize='zscore_sample' # type: ignore
    )
    
    timeseries = {}
    for func_path in func_paths:
        sub_id = os.path.basename(func_path).split('-')[1].split('.')[0]
        ts = masker.fit_transform(func_path)
        timeseries[sub_id] = ts
    
    return timeseries
