class bicicleta:
    def __init__(self, cor, modelo, ano, valor) -> None:
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Piiiii")

    def parar(self):
        print("Velocidade: 0 km/h")
    
    def correr(self):
        print("Velocidade: 30 km/h")

bike_01 = bicicleta("Azul", "KsbV18", "2024", 2998.98)
bike_01.buzinar()