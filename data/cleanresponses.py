from datasets import load_dataset
import pandas as pd

if __name__ == "__main__":

    dataset_clean = load_dataset("cmudrc/Material_Selection_Eval", "clean_responses")

    dataset_clean_pd = dataset_clean['train'].to_pandas()

    dataset_clean_pd.to_csv('./data/csv_files/clean_responses.csv', index=False)