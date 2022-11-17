from openpyxl import load_workbook

class Planilha:
    """
        Classe responsável por extrair dados da planilha, tem 
        o método impletado nela:

        extrair -> retorna uma lista de dicionário, com os dados da planilha.

    """
    def __init__(self,caminho:str) -> None:
        self.caminho = caminho
        self.planilha = load_workbook(filename=self.caminho)
        self.sheet = self.planilha['Date']
    
    def extrair(self) -> list:
        """
            Método responável pela extração dos dados da planilha.

        Returns:
            list: retorna uma lista de dicionário.
        """
        data = []

        for linha in range(2,len(self.sheet['A'])+1):

            email = self.sheet['A%s' %linha].value
            nome = self.sheet['B%s' %linha].value 
            niver = (self.sheet['C%s' %linha].value)
            genero = self.sheet['D%s' %linha].value 
            sobre = self.sheet['E%s' %linha].value 
            serie = self.sheet['F%s' %linha].value 
            estilo_music = self.sheet['G%s' %linha].value
            filme = self.sheet['H%s' %linha].value 

            data.append({
                'email': email,
                'nome' : nome,
                'niver': niver,
                'genero': genero,   
                'sobre': sobre,     
                'serie': serie,
                'estilo_music': estilo_music,   
                'filme': filme
            })

        return data

