import pandas as pd

def r_e(variable, excel, sheet):
    """ Read excel
        Args = variables, excel to read, shhet of the excel
    """
    variable = pd.read_excel(excel, sheet_name=sheet, engine='openpyxl')

    return variable
