# main.py

from fastapi import FastAPI, HTTPException
from wine_data_filter import WineDataFilter
import matplotlib.pyplot as plt
import os

app = FastAPI()

# Load dataset
DATASET_PATH = "winequality-red.csv"
wine_filter = WineDataFilter(DATASET_PATH)

@app.get("/")
def root():
    return {"message": "Welcome to the Wine Quality API!"}

@app.get("/filter/{quality}")
def filter_wine(quality: int):
    try:
        filtered_data = wine_filter.filter_by_quality(quality)
        if filtered_data.empty:
            raise HTTPException(status_code=404, detail="No data found for this quality.")

        # Generate a distribution plot for alcohol content
        plt.figure(figsize=(8, 6))
        filtered_data['alcohol'].hist(bins=20, color='blue', alpha=0.7)
        plt.title(f"Alcohol Distribution for Quality {quality}")
        plt.xlabel('Alcohol')
        plt.ylabel('Frequency')
        image_path = f"static/alcohol_distribution_quality_{quality}.png"
        os.makedirs("static", exist_ok=True)
        plt.savefig(image_path)
        plt.close()

        return {
            "message": f"Filtered data for quality {quality} and visualization saved.",
            "image_path": image_path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
