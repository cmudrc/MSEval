# MSEval
This repository is created for the research done by the Design Research Collective and Autodesk Research - Dataset on Material Selection Evaluation.
This repository shows an example of how to extract the MSEval dataset from HuggingFace and its usage.

# Abstract
The task of material selection plays a pivotal role in a large number of industries, from manufacturing to construction. Material selection is usually carried out after several cycles of conceptual design, during which designers iteratively refine the design solution and the intended manufacturing approach. In design research, material selection is typically treated as an optimization problem with one correct answer, and restricted to specific types of objects or design functions which can be computationally expensive and time-consuming to accurately represent human-level capabilities. In this paper, we introduce MSEval, a novel benchmark designed to facilitate evaluation and modify the behavior of a foundation model through different existing techniques in the context of material selection for conceptual design.  By concentrating on different tasks by modifying the input fed into the language model, our benchmark delivers a more meaningful and robust evaluation of foundation models’ performance in this niche domain.

# Getting Started
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

# Repository
```
📦 MSEval
├─ data  # Scripts to extract data from Huggingface in csv format
    ├─ csv_files
    ├─ allresponses.py # Script to extract all data (contains empty responses)
    ├─ cleanresponses.py # Script to extract filtered data (does not contain empty responses)
    ├─ keyquestions.py # Script to extract key to columns
├─ remap_scripts  # Example script used to remap the keys from the dataset
├─ MSEval_Demo.ipynb # Example demo of extraction of dataset from HuggingFace and usage to compare scores from an AI model
```

The dataset is hosted on Huggingface and can be found [here](https://huggingface.co/datasets/cmudrc/Material_Selection_Eval).

# Demo
The **MSEval_Demo.ipynb** notebook provides a step-by-step walkthrough of the process of extracting the MSEval dataset from HuggingFace, along with a demonstration of how to use it for evaluating algorithmic models.
## Reasoning and Research Methods:
The MSEval dataset was designed to evaluate the performance of algorithmic models in the specific task of material selection within conceptual design. The material selection process involves making critical decisions that impact product performance, cost, and sustainability, making it an essential aspect of many industries, including manufacturing and construction.

In the demo, we showcase how to extract the MSEval dataset, which consists of expert evaluations from human professionals, capturing how materials are evaluated based on several design briefs and criteria. These responses are intended to serve as a benchmark for testing LLMs by comparing their outputs to the human evaluations captured in the dataset.

The demo is structured as follows:

1. Dataset Extraction:
The notebook demonstrates how to download and extract the dataset from HuggingFace. The data includes both complete and incomplete survey responses from a wide array of professionals in materials science and design. The demo shows the usage of the cleaned responses, which are the complete responses.

2. Applying the Dataset for AI Evaluation:
Using a foundation model, we demonstrate how to perform evaluations by feeding the model the same task prompts as those given to human participants in the survey. The results are compared to the ground truth (human responses) to evaluate the model’s ability to mimic human-level reasoning in material selection tasks.

3. Scoring and Benchmarking:
The notebook includes an example of how to score the performance of a language model against the MSEval dataset, providing metrics that illustrate the alignment between the model’s decisions and human expert evaluations.

# Statistical Evaluations for future work
We also used this dataset for evaluation using statistical techniques which are shown in another repository [here](https://github.com/grndnl/llm_material_selection_jcise/blob/main/evaluation/z-score.py) and [here](https://github.com/grndnl/llm_material_selection_jcise/blob/main/evaluation/mean_distance.py). We exhibit the usage of mean distance and z-score as a metric to evaluate the model. We encourage people who want to use this dataset to make use of these metrics as well.

## Citing MSEval
```bibtex
@misc{jain2024msevaldatasetmaterialselection,
      title={MSEval: A Dataset for Material Selection in Conceptual Design to Evaluate Algorithmic Models}, 
      author={Yash Patawari Jain and Daniele Grandi and Allin Groom and Brandon Cramer and Christopher McComb},
      year={2024},
      eprint={2407.09719},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2407.09719}, 
}
```
