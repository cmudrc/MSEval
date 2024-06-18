from datasets import load_dataset
import pandas as pd

if __name__ == "__main__":

    dataset_all = load_dataset("cmudrc/Material_Selection_Eval", "all_responses")

    dataset_all_pd = dataset_all['train'].to_pandas()

    dataset_all_pd.to_csv('./data/csv_files/all_responses.csv', index=False)