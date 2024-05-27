# Implementing Recurrent Neural Network (RNN) from Scratch

This project involves the implementation of a Recurrent Neural Network (RNN) from scratch. Below are the steps involved in the implementation.

## Steps for Implementing RNN

1. **Importing the Libraries & Loading Dataset**:
   - Import necessary libraries for data manipulation and model building.
   - Load the dataset from the attached CSV file.

2. **Data Preprocessing & Training**:
   - **Tokenize Text**:
     - Convert text data into sentences and words.
   - **Remove Infrequent Words**:
     - Remove stopwords or infrequent words to improve model performance.
   - **Build Training & Test Dataset**:
     - Split the dataset into training and testing sets for model evaluation.

3. **Building the RNN**:
   - **Initialize Assistance Parameters**:
     - Set up parameters such as word dimension, hidden dimension, output dimension, and backpropagation through time (bptt_truncate).
   - **Initialize Network Parameters**:
     - Initialize weights (U, V, W) for the RNN model.
   - **Activation Function**:
     - Use the sigmoid activation function for the RNN model.
   - **Forward Propagation**:
     - Perform forward pass to make predictions.
     - Predict the highest score using the model.
   - **Calculate Loss**:
     - Create a loss function to measure errors and evaluate model performance.

**Note**: Evaluating loss depends on the size of the dataset, so try to minimize it by random initialization.

## Code File

The implementation of the RNN can be found in the following code file:
- `rnn.ipynb`: Contains the implementation of the Recurrent Neural Network (RNN).

## Dataset

The dataset used for training and testing the RNN is provided as a CSV file attached to this repository.

## Dependencies

To run the code, you'll need the following dependencies:

- NumPy: For numerical computations.
- Pandas: For data manipulation.

You can install the dependencies using pip:

```bash
pip install numpy pandas
