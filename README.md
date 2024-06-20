# MSEval
This repository is created for the research done by the Design Research Collective and Autodesk Research - Dataset on Material Selection Evaluation.
This repository shows an example of how to extract the MSEval dataset from HuggingFace and its usage.

## Abstract
The task of material selection plays a pivotal role in a large number of industries, from manufacturing to construction. Material selection is usually carried out after several cycles of conceptual design, during which designers iteratively refine the design solution and the intended manufacturing approach. In design research, material selection is typically treated as an optimization problem with one correct answer, and restricted to specific types of objects or design functions which can be computationally expensive and time-consuming to accurately represent human-level capabilities. In this paper, we introduce MSEval, a novel benchmark designed to facilitate evaluation and modify the behavior of a foundation model through different existing techniques in the context of material selection for conceptual design.  By concentrating on different tasks by modifying the input fed into the language model, our benchmark delivers a more meaningful and robust evaluation of foundation models’ performance in this niche domain.

## Getting Started
Before downloading any files or running any scripts, make sure you have datasets and pandas installed.

To install required dependencies:

```bash
pip install datasets
```
```bash
pip install pandas
```
or 
```bash
conda install -c huggingface -c conda-forge datasets
```
```bash
conda install -c conda-forge pandas
```

## Repository
```
📦 MSEval
├─ data  # Scripts to extract data from Huggingface in csv format
    ├─ csv_files
    ├─ allresponses.py # Script to extract all data (contains empty responses)
    ├─ cleanresponses.py # Script to extract filtered data (does not contain empty responses)
    ├─ keyquestions.py # Script to extract key to columns
├─ remap_scripts  # Example script used to remap the keys from the dataset
```

The dataset is hosted on Huggingface and can be found [here](https://huggingface.co/datasets/cmudrc/Material_Selection_Eval).