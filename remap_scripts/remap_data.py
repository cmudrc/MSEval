import pandas as pd

# Load the CSV file into a pandas DataFrame
file_path = './data/csv_files/all_responses.csv'
df = pd.read_csv(file_path)

# drop people that did not have material experience
df = df[df['material_familiarity'] == 'Yes']


# Mapping questions to 'design' and 'criteria'
design_map = {
    range(1, 5): "kitchen utensil grip",
    range(5, 9): "spacecraft component",
    range(9, 13): "underwater component",
    range(13, 17): "safety helmet",
}
criteria_map = {
    1: "lightweight",
    2: "heat resistant",
    3: "corrosion resistant",
    4: "high strength",
}

# Expand these mappings to cover all questions
design_dict = {}
criteria_dict = {}
for k, v in design_map.items():
    for i in k:
        design_dict[i] = v

for i in range(1, 17):
    criteria_dict[i] = criteria_map[(i - 1) % 4 + 1]

# Materials list for columns
materials = ["Steel", "Aluminium", "Titanium", "Glass", "Wood", "Thermoplastic", "Elastomer", "Thermoset", "Composite"]



# Create a new DataFrame to hold the mapped data
mapped_data = []

# Extract and map the data from the original DataFrame
for q_num in range(1, 17):
    # q_cols = [f"Q{q_num}_{material}" for material in materials]
    for material in materials:
        for index, row in df.iterrows():
            mapped_data.append({
                "design": design_dict[q_num],
                "criteria": criteria_dict[q_num],
                "material": material.lower(),
                "response": row[f"Q{q_num}_{material}"]
            })

# Convert the mapped data to a DataFrame
mapped_df = pd.DataFrame(mapped_data)

# downsample the kitchen utensil grip and lightweight to 750
filtered_df = mapped_df[(mapped_df['design'] == 'kitchen utensil grip') & (mapped_df['criteria'] == 'lightweight')]
downsampled_df = filtered_df.sample(n=800, random_state=2)
mapped_df = pd.concat([mapped_df[~((mapped_df['design'] == 'kitchen utensil grip') & (mapped_df['criteria'] == 'lightweight'))], downsampled_df])


# Show a sample of the new DataFrame to verify the transformation
print(mapped_df.head())

print(mapped_df.groupby(['design', 'criteria'])['response'].count().reset_index(name='count'))

print(mapped_df.count())

mapped_df.to_csv('./remap_scripts/survey_responses_mapped.csv', index=False)
