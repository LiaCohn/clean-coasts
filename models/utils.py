import numpy as np


def remove_high_corr(df, target="test_result_num", threshold=0.6):
    """
    return dataframe without corrlation that can be drop.

    args:
    df = dataframe
    target = string of the target
    threshold = default 0.6
    """
    target_col = df.pop(target)
    df.insert(len(df.columns), target, target_col)
    cor_matrix = df.corr().abs()
    corr_df = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))

    cols = corr_df.columns.to_list()
    list_corr_not_empty = []

    for i in range(len(cols) - 1):
        tmp = []
        for j in range(len(cols) - 1):
            if abs(corr_df.iloc[i, j]) >= threshold and cols[i] is not cols[j]:
                tmp.append(cols[j])
        if len(tmp) > 0:
            tmp.append(cols[i])
            list_corr_not_empty.append(tmp)

    def Key(p):
        return corr_df[target][p]

    stay = [max(sub, key=Key) for sub in list_corr_not_empty]
    drops = [c for sub in list_corr_not_empty for c in sub if c not in stay]
    # distance_to_ashdod_port -> hifa_port_dis. city_jinny_ranking -> city rank
    cols = list(set(drops))
    if "hifa_port_dis" in cols:
        cols.remove("hifa_port_dis")
        cols.append("distance_to_ashdod_port")
    if "city rank" in cols:
        cols.remove("city rank")
        cols.append("city_jinny_ranking")
    cols = list(set(cols))
    return df.drop((cols), axis=1)


def remove_if_exist(df):
    to_remove = [
        "coast_name",
        "coast_desc",
        "city",
        "check station",
        "key",
        "coast_num",
        "center",
        "North",
        "Eilat",
        "South",
        "rain-2days",
        "month",
        "Unnamed: 0",
    ]
    cols_to_remove = [col for col in to_remove if col in df.columns]
    # Remove columns from the DataFrame
    df = df.drop(cols_to_remove, axis=1)
    return df
