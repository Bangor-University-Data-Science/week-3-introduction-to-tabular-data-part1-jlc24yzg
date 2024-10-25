import pandas as pd
def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    my_dict = {}
    
    for feature in categorical_features:
        my_dict[feature] = df[feature].unique().tolist()
    return my_dict
    
    pass  # Implement the logic here

    