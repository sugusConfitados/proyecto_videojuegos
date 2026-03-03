import pandas as pd


def guardar_parquet(path: str, df: pd.DataFrame) -> None:
    """
    Guarda un DataFrame en un archivo .parquet
    """
    df.to_parquet(path)
