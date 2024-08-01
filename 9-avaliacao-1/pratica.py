from abc import ABC, abstractmethod


class PortaIndisponivel(Exception):
    pass

class DispositivoDeRede(ABC):
    def __init__(self, nome, endereco_ip):
        self.nome = nome
        self.endereco_ip = endereco_ip
        self.__portas = []

    @abstractmethod
    def configurar(self):
        pass

    @property
    def portas(self):
        return self.__portas
    
    @portas.setter
    def portas(self, portas):
        assert isinstance(portas, list), "Portas precisa ser uma lista"
        assert all(isinstance(p, int) for p in portas), "Portas precisa ser uma lista de inteiros"
        self.__portas = portas

    def conectar(self, dispositivo, porta):
        if porta not in self.portas or porta not in dispositivo.portas:
            raise PortaIndisponivel(f'A porta {porta} não está disponível')
        self.portas.remove(porta)
        dispositivo.portas.remove(porta)
        print(f'{self.nome} conectado a {dispositivo.nome} na porta {porta}')


class Firewall(DispositivoDeRede):
    def configurar(self):
        print(f'[{self.nome}] configurado com sucesso')

class Roteador(DispositivoDeRede):
    def __init__(self, nome, endereco_ip, protocolo):
        super().__init__(nome, endereco_ip)
        self.protocolo = protocolo

    def configurar(self):
        print(f'[{self.nome}] configurado com sucesso')

class Switch(DispositivoDeRede):
    def __init__(self, nome, endereco_ip, vlan):
        super().__init__(nome, endereco_ip)
        self.vlan = vlan

    def configurar(self):
        print(f'[{self.nome}] configurado com sucesso')

if __name__ == '__main__':
    try:
        # d1 = DispositivoDeRede('Roteador', '127.0.0.1')
        # d1.portas = [80, 8080, 443]

        # d2 = DispositivoDeRede('Switch', '192.168.0.1')
        # d2.portas = [80, 8080, 21, 22]

        # d1.conectar(d2, 443)

        f = Firewall('Firewall', '192.1.1.1')
        f.portas = [80, 8080, 443]
        s = Switch('Switch', '10.0.0.1', 10)
        s.portas = [80, 8080, 21, 22]
        r = Roteador('Roteador', '192.2.1.1', 'TCP')
        r.portas = [80, 8080, 443]
        for dispositivo in [f, s, r]:
            dispositivo.configurar()

    except AssertionError as e:
        print(e)
    except PortaIndisponivel as e:
        print(e)