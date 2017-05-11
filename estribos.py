# coding=utf-8

"""Programa para calcular armadura proporcionada por estribos."""
import os
from colorama import Fore, Style, init, deinit


init()  # inicia colorama

ESTRIBOS = True

while ESTRIBOS:

    DIAMETRO = float(input('\nDiámetro en [mm] (0 para salir): '))

    if DIAMETRO == 0:

        ESTRIBOS = False
        deinit()  # termina colorama
        break

    SEPARACION = float(input('Separación en [cm]: '))

    os.system("cls")

    AREA = 2 * 3.14159 * (DIAMETRO / 10) ** 2 / 4

    AREA_ESTRIBOS = AREA / (SEPARACION / 100)

    FRASE1 = '\nS.M. Ø{:<.0f} @ {:<.1f} = {:>5.2f} cm²/m'.format(
        DIAMETRO, SEPARACION, AREA_ESTRIBOS / 2)
    FRASE2 = '\nD.M. Ø{:<.0f} @ {:<.1f} = {:>5.2f} cm²/m'.format(
        DIAMETRO, SEPARACION, AREA_ESTRIBOS)
    FRASE3 = '\nT.M. Ø{:<.0f} @ {:<.1f} = {:>5.2f} cm²/m'.format(
        DIAMETRO, SEPARACION, AREA_ESTRIBOS * 1.5)
    FRASE4 = '\nC.M. Ø{:<.0f} @ {:<.1f} = {:>5.2f} cm²/m'.format(
        DIAMETRO, SEPARACION, AREA_ESTRIBOS * 2)

    print(Fore.GREEN + FRASE1)
    print(Fore.RED + FRASE2)
    print(Fore.YELLOW + FRASE3)
    print(Fore.WHITE + FRASE4)
    print(Style.RESET_ALL)


