from nilearn import datasets
from typing import Dict, Any
import shutil
import os

def fetch_abide_dataset(n_subjects: int = 1, pipeline: str = 'cpac', output_dir: str ='data/preprocessed/abide') -> Dict[str, Any]:
    """_raw ABIDE dataset_

    Args:
        n_subjects (int, optional): _# of subjects to fetch_. Defaults to 1.
        pipeline (str, optional): _description_. Defaults to 'cpac'.
        output_dir (str, optional): _description_. Defaults to 'data/preprocessed/abide'.

    Returns:
        Dict[str, Any]: _description_
    """
    
    os.makedirs(output_dir, exist_ok=True)
    
    dataset = datasets.fetch_abide_pcp(
        n_subjects=n_subjects, 
        pipeline=pipeline, 
        band_pass_filtering=True
    )
    
    func_dir = f"{output_dir}/func_preproc"
    pheno_path = f"{output_dir}/phenotypic.csv"
    
    os.makedirs(func_dir, exist_ok=True)
    
    existing_files = len([f for f in os.listdir(func_dir) if f.endswith('.nii.gz')])
    
    saved_paths = []
    for i, (func_file, sub_id) in enumerate(zip(dataset.func_preproc, dataset.phenotypic['SUB_ID'])):
        target_path = f"{func_dir}/sub-{int(sub_id):07d}.nii.gz"  # ゼロ埋め統一
        shutil.copy(func_file, target_path)
        saved_paths.append(target_path)
    
    dataset.phenotypic.to_csv(pheno_path, index=False)
    
    final_count = len([f for f in os.listdir(func_dir) if f.endswith('.nii.gz')])
    new_files = final_count - existing_files
    
    return {
        'func_preproc_paths': saved_paths,
        'phenotypic_path': pheno_path,
        'n_subjects': n_subjects,
        'saved_files_count': new_files
    }

if __name__ == "__main__":
    info = fetch_abide_dataset(n_subjects=3)
    print(f"Requested: {info['n_subjects']} subjects")
    print(f"Phenotypic: {info['phenotypic_path']}")
    print(f"New func files saved: {info['saved_files_count']}")
    print(f"Saved paths: {info['func_preproc_paths'][:1]}...")
