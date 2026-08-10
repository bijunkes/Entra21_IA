# Crie uma função que receba a temperatura
# em celcius e converte para fahrenheit
def celcius_to_farenheit(temp: float) -> float:
    return temp * (9/5) + 32

# Crie uma função que receba a temperatura
# em fahrenheit e converte para celsius
def farenheit_to_celcius(temp: float) -> float:
    return (temp - 32) * (5/9)

# Crie uma função que receba a temperatura
# em celsius e converte para kelvin
def celcius_to_kelvin(temp: float) -> float:
    return temp + 273.15

# Crie uma função que receba a temperatura
# em kelvin e converte para celsius
def kelvin_to_celcius(temp: float) -> float:
    return temp - 273.15

# Crie uma função que receba a temperatura
# em fahrenheit e converte para kelvin
def farenheit_to_kelvin(temp: float) -> float:
    return farenheit_to_celcius(temp) + 273.15

# Crie uma função que receba a temperatura
# em kelvin e converte para fahrenheit
def kelvin_to_farenheit(temp: float) -> float:
    return celcius_to_farenheit(temp) - 273.15
