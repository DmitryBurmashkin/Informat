#It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child.
# Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it
# (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.
import pandas as pd


def chickenpox_by_sex():
    try:
        df = pd.read_csv('./NISPUF17.csv', usecols = ['HAD_CPOX', 'SEX', 'P_NUMVRC'])

        male_had_with_vaccine  = df[(df.HAD_CPOX == 1) & (df.P_NUMVRC > 0) & (df.SEX == 1)]
        male_hadnt_with_vaccine = df[(df.HAD_CPOX == 2) & (df.P_NUMVRC > 0) & (df.SEX == 1)]
        male_ratio = len(male_had_with_vaccine) / len(male_hadnt_with_vaccine)

        girl_had_with_vaccine = df[(df.HAD_CPOX == 1) & (df.P_NUMVRC > 0) & (df.SEX == 2)]
        girl_hadnt_with_vaccine = df[(df.HAD_CPOX == 2) & (df.P_NUMVRC > 0) & (df.SEX == 2)]
        girl_ratio = len(girl_had_with_vaccine) / len(girl_hadnt_with_vaccine)

        conclusion = {"male": round(male_ratio, 4),
              "female": round(girl_ratio, 4)}

        print(conclusion)
    except IOError:
        print('Ошибка: положите файл в ту же директорию, что и файл Burmashkin_DA_12_11.py')
chickenpox_by_sex() 