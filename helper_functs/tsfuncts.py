import pandas as pd, numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

def create_features_extracted_days(df: pd.DataFrame) -> pd.DataFrame:
    """_summary_
        Create time series features based on the time series index.
    Args:
        df (pd.DataFrame): _description_
    Returns:
        pd.DataFrame: _description_
    """
    # Old version
    # df['hour'] = df.index.hour
    # df['dayofweek'] = df.index.dayofweek
    # df['quarter'] = df.index.quarter
    # df['month'] = df.index.month
    # df['year'] = df.index.year
    # df['dayofyear'] = df.index.dayofyear
    # df['dayofmonth'] = df.index.day
    # df['weekofyear'] = df.index.isocalendar().week
    # More memory efficient
    return df.assign(
        hour=df.index.hour,
        dayofweek=df.index.dayofweek,
        quarter=df.index.quarter,
        month=df.index.month,
        year=df.index.year,
        dayofyear=df.index.dayofyear,
        dayofmonth=df.index.day,
        weekofyear=df.index.isocalendar().week)

def calculate_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    """Calculate metrics for time series predictions.
    
    Args:
        y_true (np.ndarray): True values.
        y_pred (np.ndarray): Predicted values.
    
    Returns:
        dict: Dictionary containing RMSE and MAE.
    """
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    return {'RMSE': round(rmse, 2), 'MAE': round(mae, 2)}

def df_average_error(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Calculate the average error for a given column in a DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame containing the true and predicted values.
        col (str): Column name for the predicted values.
    
    Returns:
        pd.DataFrame: DataFrame with the average error.
    """
    eval_error = df.copy()
    eval_error['error'] = np.abs(eval_error['load'] - eval_error[col])
    eval_error['date'] = eval_error.index.date
    
    return eval_error.groupby(['date'])['error'].mean().sort_values(ascending=False).head(4)

def split_sequence(data: np.ndarray, window_size: int, output_size: int) -> tuple:
    """_summary_
    it generates lags for time series data.
    Args:
        data (np.ndarray): _description_
        window_size (int): _description_
        output_size (int): _description_

    Returns:
        tuple: _description_
    """
    data = data.flatten()
    num_samples = len(data) - window_size - output_size + 1

    X = np.empty((num_samples, window_size), dtype=data.dtype)
    y = np.empty((num_samples, output_size), dtype=data.dtype)

    for i in range(num_samples):
        X[i] = data[i:i + window_size]
        y[i] = data[i + window_size:i + window_size + output_size]
    X = X.reshape((X.shape[0], X.shape[1], output_size))
    return X, y