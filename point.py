import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_points_from_csv(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Extract latitude and longitude columns
    latitude = df['lat']
    longitude = df['lon']
    classes = df['lon']
    unique_classes = np.unique(classes)


    num_unique_classes = len(unique_classes)
    colors = plt.cm.tab10(np.linspace(0, 1, num_unique_classes))  # Using a colormap to generate distinct colors
    
    # Plot the points with different colors for each class
    for class_label, color in zip(unique_classes, colors):
        class_indices = classes == class_label
        plt.scatter(longitude[class_indices], latitude[class_indices], color=color, label=class_label, alpha=0.5)
    

    # Plot the points
    # plt.scatter(longitude, latitude, color='blue', alpha=0.5)  # alpha adjusts the transparency
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Figure of Points')
    plt.grid(True)
    plt.show()

# Example usage:
csv_file = 'all.csv'  # Replace 'your_file.csv' with the path to your CSV file
plot_points_from_csv(csv_file)