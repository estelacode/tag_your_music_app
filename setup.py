# Autor: Estela Madariaga
# Fecha de creación: 2022


from setuptools import setup


setup(
    name = "tag_your_music_v2", # nombre  de la app
    version = "0.0.1",  # version de la app
    packages = ["src"], # paquetes que publica o utiliza
    entry_points = {"console_scripts":["tag_your_music_v2 = src.__main__:main"]}, # puntos de entrada, por donde vamos a llamar a la aplicacion.
    install_requires = open("requirements.txt").read().splitlines() # Paquetes  que se requieren
)