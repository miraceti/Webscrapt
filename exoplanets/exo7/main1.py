import flet as ft
import pandas as pd

df = pd.DataFrame({
        "test" : ['1', "20", "40"],
        "test1" : ['2', "21", "41"],
        "test2" : ['3', "22", "43"],
    })


def headers(df : pd.DataFrame) -> list:
    return [ft.DataColumn(ft.Text(header)) for header in df.columns]

def rows(df : pd.DataFrame) -> list:
    rows = []
    for index, row in df.iterrows():
        rows.append(ft.DataRow(cells = [ft.DataCell(ft.Text(row[header])) for header in df.columns]))
    return rows

            
def main(page :ft.Page):
    datatable = ft.DataTable(
        columns=headers(df),
        rows=rows(df))
    
    page.add(datatable)

if __name__ == '__main__':
    ft.app(target=main)