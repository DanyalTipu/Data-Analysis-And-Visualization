# Image Processing and Logistic Regression Tasks

This project involves several tasks related to image processing and logistic regression, implemented in the `image_processing.ipynb` Jupyter Notebook.

## Tasks

### 1. Design 1st Order Derivative and 2nd Order Derivative Filters

- **Objective**: Design filters for the 1st order derivative and 2nd order derivative and apply them to input images.
- **Details**: These filters are used to highlight edges in the images. The 1st order derivative (gradient) detects edges by looking for the maximum rate of change, while the 2nd order derivative (Laplacian) detects regions of rapid intensity change.
- **Implementation**: Refer to the `image_processing.ipynb` notebook.

### 2. Identify and Filter Noise in Images

- **Objective**: Identify the type of noise (Gaussian or Salt and Pepper) present in an image and apply the appropriate filter.
- **Details**: Gaussian noise is best addressed using Gaussian filters, whereas Salt and Pepper noise can be removed using median filters.
- **Implementation**: Refer to the `image_processing.ipynb` notebook.

### 3. Apply Logistic Regression on Sample Input Dataset

- **Objective**: Apply logistic regression on a sample input dataset with handcrafted features.
- **Details**: This task involves creating features from the dataset and using logistic regression to classify the data.
- **Implementation**: Refer to the `image_processing.ipynb` notebook.

### 4. Apply Noise Removal Filter and Then Logistic Regression

- **Objective**: Apply a noise removal filter (such as smoothing or low-pass filter) on images and then apply logistic regression.
- **Details**: This step is aimed at improving the quality of the images before classification to achieve better results.
- **Implementation**: Refer to the `image_processing.ipynb` notebook.

### 5. Apply Edge Detection Filter and Then Logistic Regression

- **Objective**: Apply an edge detection filter (high-pass filter) on images and then apply logistic regression.
- **Details**: Edge detection helps in highlighting the boundaries within images which can be crucial features for classification tasks.
- **Implementation**: Refer to the `image_processing.ipynb` notebook.

### 6. Combine Techniques and State Shortcomings

- **Objective**: Try a combination of the above techniques and discuss the shortcomings encountered.
- **Details**: Combining noise removal, edge detection, and logistic regression could lead to improved classification performance. However, it is important to analyze the impact and limitations of each combination.
- **Implementation**: Refer to the `image_processing.ipynb` notebook.

## Dependencies

- `numpy`
- `scipy`
- `matplotlib`
- `sklearn`
- `Pillow` (Python Imaging Library)

## Usage

To run the tasks, ensure you have the necessary dependencies installed. You can use the provided functions in the `image_noise_reduction.ipynb` notebook to process the images and perform logistic regression.

Install the dependencies using:
```sh
pip install numpy scipy matplotlib scikit-learn pillow
