import pandas as pd

def get_requests_by_type(log_df):
    df_methods_1 = log_df.copy()

    # generating methods column
    df_methods_1["method"] = df_methods_1.apply(
        lambda row: row["url"].split()[0], axis=1)
    df_methods_2 = pd.DataFrame(df_methods_1["method"])

    # grouping by method
    df_methods_2["cnt"] = 0
    df_meths = df_methods_2.groupby(
        by=["method"], as_index=False).count().reset_index(drop=True)

    # removing trash
    return df_meths.loc[(df_meths["method"].astype(
        'str').str.len() < 10)].reset_index(drop=True)

def get_frequent_requests(log_df):
    df_urls = pd.DataFrame(log_df.iloc[:, 1])
    df_urls["cnt"] = 0
    df_urls2 = df_urls.copy()
    df_urls2["url_without_params"] = df_urls.apply(
        lambda row: row["url"].split()[1], axis=1)
    del df_urls2["url"]
    df_urls_g = df_urls2.groupby(
        by=["url_without_params"], as_index=False).count()
    return df_urls_g.sort_values("cnt", ascending=False).head(
        10).reset_index(drop=True)

def get_client_errors_requests(log_df):
    df_filtered = log_df.query(
        "status >= 400 and status < 500 and size != '-'").iloc[:, 0:4].copy()
    df_filtered["size"] = df_filtered["size"].astype(int)
    return df_filtered.sort_values(
        "size", ascending=False).head(5).reset_index(drop=True)

def get_frequent_users(log_df):
    df_5xx = log_df.query("status >= 500 and status < 600").iloc[:, [0]]
    df_5xx["cnt"] = 0
    return df_5xx.groupby(by=["ip"], as_index=False).count().sort_values(
        "cnt", ascending=False).head(5).reset_index(drop=True)