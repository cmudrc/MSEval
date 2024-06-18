from datasets import load_dataset
import pandas as pd

if __name__ == "__main__":

    dataset_kq = load_dataset("cmudrc/Material_Selection_Eval", "additional_data")

    dataset_kq_pd = dataset_kq['train'].to_pandas()

    dataset_kq_pd.to_csv('./data/csv_files/key_questions.csv', index=False)