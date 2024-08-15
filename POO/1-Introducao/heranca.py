class Servidor:
    def __init__(self, nome, cpf, rg, endereco):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco

    def __str__(self):
        return f"Nome={self.nome}, CPF={self.cpf}, RG={self.rg}"

class Docente(Servidor):
    def __init__(self, nome, cpf, rg, endereco, matricula):
        super().__init__(nome, cpf, rg, endereco)
        self.matricula = matricula

class Terceirizado(Servidor):
    def __init__(self, nome, cpf, rg, endereco):
        super().__init__(nome, cpf, rg, endereco)

class TecnicoAdministrativo(Servidor):
    def __init__(self, nome, cpf, rg, endereco):
        super().__init__(nome, cpf, rg, endereco)

docente = Docente("Diego", "082302830", "233823", "Rua xxxxx", "123223")
print(docente)
terceirizado = Terceirizado("José", "23232323", "323222", "Rua XXXX")
print(terceirizado)
tecnico = TecnicoAdministrativo("Maria", "3222232", "23232", "Rua YYY")
print(tecnico)