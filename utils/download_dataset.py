from sklearn.datasets import fetch_openml

def download_and_save_to_csv(data_id=42712, output_path="data/raw/bike_sharing.csv"):
    dataset = fetch_openml(data_id=data_id, as_frame=True, parser="auto")
    df = dataset.frame
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category')
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    download_and_save_to_csv()