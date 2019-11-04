#functions to normalize sun, rain and wind

def normalize_sun(df):
    result = df.copy()
    max_value = df["Sunshine"].max()
    min_value = df["Sunshine"].min()
    result["Sunshine"] = (df["Sunshine"] - min_value) / (max_value - min_value)
    return result

def normalize_wind(df):
    result = df.copy()
    max_value = df["MeanWindSpeed"].max()
    min_value = df["MeanWindSpeed"].min()
    result["MeanWindSpeed"] = (df["MeanWindSpeed"] - min_value) / (max_value - min_value)
    
    max_value = df["MaxWindSpeed"].max()
    min_value = df["MaxWindSpeed"].min()
    result["MaxWindSpeed"] = (df["MaxWindSpeed"] - min_value) / (max_value - min_value)
    
    return result
