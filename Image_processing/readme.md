# Image Processing Tasks

This project involves several image processing tasks implemented in the `image_processing.ipynb` Jupyter Notebook.

## Project Overview

The tasks include:
1. Converting RGB images to grayscale
2. Saving data into JSON format
3. Creating and plotting image histograms
4. Performing histogram normalization/equalization
5. Performing spatial filtering operations

## Tasks

### Task 1: Convert RGB Images to Grayscale

Convert RGB images to grayscale using the following formula:
\[ \text{grayscale image} = (0.3 \times R) + (0.59 \times G) + (0.11 \times B) \]

Use any RGB image of your choice, or the image provided below:

![Einstein Image](https://i0.wp.com/www.themarginalian.org/wp-content/uploads/2013/05/einstein1.jpg?w=680&ssl=1)

Refer to the `image_processing.ipynb` notebook for the code implementation.

### Task 2: Save Data into JSON Format

Save the processed data into a JSON file. This can include image metadata, processing results, or any other relevant information.

Refer to the `image_processing.ipynb` notebook for the code implementation.

### Task 3: Create and Plot Image Histogram

Write a function `make_histogram` that takes an image and its size as inputs and outputs the histogram of the image. Plot this histogram using `matplotlib`.

Refer to the `image_processing.ipynb` notebook for the code implementation.

### Task 4: Histogram Normalization/Equalization

Perform histogram normalization/equalization. Utilize the `make_histogram` function from the previous task. Write an additional function `cumulative_sum` to calculate the cumulative distribution function (CDF) for the histogram. Use the following formula to calculate the equalized histogram:
\[ \text{CSD_histogram} = \frac{(\text{CD} - \min)}{(\max - \min)} \times 255 \]

Refer to the `image_processing.ipynb` notebook for the code implementation.

### Task 5: Spatial Filtering Operation

Perform a spatial filtering operation on the following image. Calculate its size, resize it to 16x16, and use a kernel size of 3x3.

![Lenna Image](https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png)

Kernel:
\[ \begin{bmatrix}
3 & 0 & 3 \\
1 & 0 & 1 \\
3 & 0 & 3
\end{bmatrix} \]

Refer to the `image_processing.ipynb` notebook for the code implementation.

## Dependencies

- `numpy`
- `matplotlib`
- `Pillow` (Python Imaging Library)

## Usage

To run the tasks, ensure you have the necessary dependencies installed. You can use the provided functions in the `image_processing.ipynb` notebook to process the images and generate the required outputs.

Install the dependencies using:
```sh
pip install numpy matplotlib pillow
