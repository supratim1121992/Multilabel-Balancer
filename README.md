# Multilabel-Balancer
Utility function to correct class imbalance in image annotations with multiple objects/labels.

Considering a data structure similar to the one displayed below where a majority class (0 in this case) is present in the dataset, it might be difficult to correct class imabalance by excluding certain images without losing some of the minority classes as well.

![Sample Data](https://github.com/supratim1121992/Multilabel-Balancer/blob/main/Sample_Data.png?raw=true)

The utility function provided here implements class imabalance correction by setting a threshold dynamically such that a minimum user defined ratio is always maintained while removing any records or images with the majority class over-represented. This helps in reducing the class imbalance and also preserves the existing minority class instances.

> **The function takes the following input arguments:**
 * **df:** The dataframe with the annotation data.
 * **id:** The unique identifier column name (image_name in sample).
 * **lab:** The target column name with the labels.
 * **maj_cls:** The majority class value (0 in sample).
 * **trs:** (*Default 1*) The initiating threshold to be used. 1 indicates that any images with 100% of the claases belonging to the majority class are removed.
 * **trs_red:** (*Default 0.005*) The amount by which the initiating threshold is reduced at every iteration to attain the minimum optimal threshold.
 * **trd_rat:** (*Default 5*) The minimum tradeoff ratio to consider for dropping samples. 5 indicates that for each case of the most infrequent minority class, at least 5 cases of the majority class should also be removed.
  
> **Output:** Dataframe with class imbalanced images removed along with a list of the ids removed.
