import pandas as pd
def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [df.select_dtypes(include=['float64'])],  # Fill with continuous numerical features
            'discrete': [df.select_dtypes(include=['int64'])]  # Fill with discrete numerical features
        },
        'categorical': {
            'nominal': [df.select_dtypes(include=['object', 'category', 'bool'])],  # Fill with nominal categorical features
            'ordinal': [df.select_dtypes(include=['bool'])]  # Fill with ordinal categorical features
        }
    }
    return feature_types
