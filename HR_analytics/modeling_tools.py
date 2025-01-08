import pandas as pd
import numpy as np
import itertools
import scipy.stats as stats


# Drop Correlated Variables Considering correlation with Target

def drop_correlated(df: pd.DataFrame, target: str):

    """Remove variables highly correlated
    Arguments:
        df: dataframe
        target: target
    """

    df = df.copy()

    df_numeric = df.select_dtypes('number')

    combinations = list(itertools.combinations(df_numeric, 2))

    vars_to_drop = []

    for combination in combinations:

        correlation = abs(stats.pearsonr(df_numeric[combination[0]], df_numeric[combination[1]])[0])

        if correlation >= 0.9:

            corr_1 = abs(stats.pearsonr(df_numeric[combination[0]], df_numeric[target])[0])

            corr_2 = abs(stats.pearsonr(df_numeric[combination[1]], df_numeric[target])[0])

            if corr_1 > corr_2:

                vars_to_drop.append(combination[1])
            
            else:

                vars_to_drop.append(combination[0])
    
    print(vars_to_drop)

    return df.drop(columns=vars_to_drop)

# Analyze Chi2 of Object Variables

def analyze_chi2(df: pd.DataFrame, target: str):

    """Analyze Chi2 comparing Object Variables with Target

        df: dataframe
        target: target

        return: p-value, contingency table
    """

    for col in df.select_dtypes('object'):

        if col != target:

            print(f"{col} x {target} p-value: {stats.chi2_contingency(pd.crosstab(df[col], df[target]))[1]}")

            print(f"\n{pd.crosstab(df[col], df[target])}\n")