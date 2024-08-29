from busca_sequencial import *
from busca_binaria import *
import csv

class ServidorDns:
    def __init__(self, ip, nome):
        self.ip = ip
        self.nome = nome

    def __str__(self):
       return f"(IP: {self.ip} - nome: {self.nome})"

servidores_dns = []
with open('dns-br.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=';')
  next(csv_reader, None)  # pula os cabeçalhos
  for row in csv_reader:
    servidor_dns = ServidorDns(row[0], row[1])
    servidores_dns.append(servidor_dns)

servidores_dns.sort(key=lambda s: s.ip)
# print([str(s) for s in servidores_dns])

print(busca_sequencial("187.32.81.223", servidores_dns))
print(busca_sequencial_recursiva("187.32.81.223", servidores_dns))
print(busca_binaria("187.32.81.223", servidores_dns))
print(busca_binaria_recursiva("187.32.81.223", servidores_dns))