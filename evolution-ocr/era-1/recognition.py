import io
import cv2
import numpy as np
import pandas as pd
from PIL import Image
from matplotlib import pyplot as plt

def pil_to_binary(bytes_pil):    
    # Convert bytes to PIL image
    pil_image = Image.open(io.BytesIO(bytes_pil))
    
    # Convert to RGB first to ensure compatibility
    pil_image = pil_image.convert('RGB')
    
    # Convert PIL image to numpy array
    numpy_image = np.array(pil_image, dtype=np.uint8)
    
    # Convert to grayscale
    numpy_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2GRAY)

    # Apply binary threshold
    _, binary_image = cv2.threshold(numpy_image, 127, 255, cv2.THRESH_BINARY)

    return binary_image
def read_parquet_with_images(file_path):
    # Read parquet file
    df = pd.read_parquet(file_path)
    
    # Create a new list to store converted images
    converted_images = []
    labels = []
    
    sample_image = []
    sample_label = []
    print(f"Total images in the dataset: {len(df)}")

    # Iterate through each row
    for index, row in df.iterrows():
        pil_image = row['image']  # Assuming 'image' is the column name
        label = row['label']      # Assuming 'label' is the column name

        # Convert PIL image to cv2 format
        cv2_image = pil_to_binary(pil_image['bytes'])

        if index == 0 :
            sample_image.append(cv2_image)
            sample_label.append(label)
        else :
            converted_images.append(cv2_image)
            labels.append(label)
    
    return converted_images, labels, sample_image, sample_label

def template_matching(converted_images, sample_image):
    score_list = []
    for char_image in converted_images:
        difference = cv2.absdiff(char_image, sample_image)
        score = int(np.sum(difference))
        score_list.append(score)
    return score_list

def visualize_score(score_list, n_bins=10):
    sorted_scores = sorted(score_list)

    # Define bin parameters
    min_score = min(sorted_scores)
    max_score = max(sorted_scores)
    bin_width = (max_score - min_score) / n_bins

    # Create bin edges
    bin_edges = [min_score + i * bin_width for i in range(n_bins + 1)]

    # Create bins and count frequencies
    bin_counts = [0] * n_bins

    for i in range(n_bins):
        bin_start = bin_edges[i]
        bin_end = bin_edges[i + 1]
        
        # Count scores in this bin
        for score in sorted_scores:
            if bin_start <= score < bin_end or (i == n_bins-1 and score == bin_end):
                bin_counts[i] += 1


    # Plot bar chart
    plt.figure(figsize=(12, 6))
    plt.bar(range(n_bins), bin_counts, edgecolor='black', alpha=0.7)
    plt.xlabel('Score Bins')
    plt.ylabel('Frequency')
    plt.title('Binned Score Distribution')
    plt.tight_layout()
    plt.show()

def get_label_counts(labels):
    label_counts = pd.Series(labels).value_counts()
    label_counts = label_counts.sort_index()
    return label_counts

def main():
    image_path = "mnist.parquet"
    converted_images, labels, sample_image, sample_label = read_parquet_with_images(image_path)
    score_list = template_matching(converted_images, sample_image[0])

    # visualize_score(score_list)
    # print(get_label_counts(labels))

if __name__ == "__main__":
    main()