import pandas as pd, numpy as np
from pandas.tseries.holiday import USFederalHolidayCalendar

class Manipulate:
    def __init__(self):
        self.cal = USFederalHolidayCalendar()

    def create_date(self, df, x, lag_n):
        df = df.copy()
        df['date'] = pd.to_datetime(df['date'])
        df['weekday'] = df['date'].dt.day_name()
        df['month'] = df['date'].dt.month_name()

        df = pd.get_dummies(df, columns=['weekday', 'month'], prefix='is')
        
        holidays = self.cal.holidays(start=df['date'].min(), end=df['date'].max())
        df['is_holiday'] = df['date'].isin(holidays).astype(int)
        
        df['t'] = (df['date'] - df['date'].min()).dt.days
        df['t_lg'] = np.log1p(df['t'])
        
        for lag in range(1, lag_n + 1):
            df[f'lag{lag}'] = df[x].shift(lag)
        
        df['rolling_mean_7'] = df[x].rolling(window=7).mean()
        df['rolling_std_7'] = df[x].rolling(window=7).std()
        df['rolling_mean_30'] = df[x].rolling(window=30).mean()
        df['rolling_std_30'] = df[x].rolling(window=30).std()
        
        df = df.fillna(0)
        return df