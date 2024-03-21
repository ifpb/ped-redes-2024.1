class CartaoMensagemSemHeranca:
    def __init__(self, destinario):
        self.destinario = destinario

    def enviar_mensagem_natal(self, remetente):
        print(f'Para: {self.destinario}')
        print(f'De: {remetente}')
        print('Feliz Natal!')

    def enviar_mensagem_aniversario(self, remetente):
        print(f'Para: {self.destinario}')
        print(f'De: {remetente}')
        print('Feliz Aniversário!')

    def enviar_mensagem_namorados(self, remetente):
        print(f'Para: {self.destinario}')
        print(f'De: {remetente}')
        print('Feliz dia dos namorados!')


class CartaoMensagem:
    def __init__(self, destinario):
        self.destinario = destinario

    def enviar_mensagem(self, remetente):
        print(f'Para: {self.destinario}')
        print(f'De: {remetente}')

class CartaoNatal(CartaoMensagem):
    def enviar_mensagem(self, remetente):
        super().enviar_mensagem(remetente)
        print('Feliz Natal!')

class CartaoAniversario(CartaoMensagem):
    def enviar_mensagem(self, remetente):
        super().enviar_mensagem(remetente)
        print('Feliz Aniversário!')

class CartaoDiaDosNamorados(CartaoMensagem):
    def enviar_mensagem(self, remetente):
        super().enviar_mensagem(remetente)
        print('Feliz Dia dos Namorados!')

if __name__ == '__main__':
    mensagens = [CartaoNatal('João'), CartaoAniversario('João'), CartaoDiaDosNamorados('João')]
    for mensagem in mensagens:
        print(isinstance(mensagem, CartaoMensagem))
        mensagem.enviar_mensagem('Maria') # polimorfismo
        print()