import pandas as pd


class SquadParser:
    def __init__(self, squad_path: str, team_name: str):
        self.squad_path = squad_path
        self.team_name = team_name

    def read_excel(self):
        df = pd.read_excel(self.squad_path)

        return df


if __name__ == '__main__':
    path = '/Users/ammar.elsherebasy/Desktop/Next Gen/Squads/Brondby IF.xlsx'
    sp = SquadParser(squad_path=path, team_name='Brøndby IF')
    parsed_excel = sp.read_excel()
    print(parsed_excel.head(40))
