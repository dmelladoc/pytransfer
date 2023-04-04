

import os
import sys
from glob import glob
import requests
import pyperclip
from argparse import ArgumentParser, FileType

URL_TRANSFER = 'https://transfer.sh'


def main(args):
    # Verificar que el archivo existe
    if not os.path.isfile(args.filename):
        raise FileNotFoundError
    
    print(f"󰅧  Subiendo...")
    try:
        with open(args.filename, "rb") as data:
            conf_file = {args.filename: data}
            headers = dict()

            if args.time is not None:
                headers['Max-Days'] = str(args.time)
            if args.downloads is not None:
                headers["Max-Downloads"] = str(args.downloads)
            
            req = requests.post(
                URL_TRANSFER,
                files=conf_file,
                headers=headers,
            )

            dl_url = req.text
            print(f"Subida Terminada!\n{dl_url}\nCopiado en tu portapapeles (ctrl+V)")
            pyperclip.copy(dl_url)

    except Exception as xcp:
        print(f"Algo fallo con la subida... {xcp}")



if __name__ == "__main__":
    parser = ArgumentParser(
        prog="PyTransfer",
        description="Permite subir un archivo a transfer.sh")
    
    parser.add_argument(
        'filename',
        help="Ruta a archivo a subir.",
    )

    parser.add_argument(
        "-d", "--downloads", 
        type=int, #default=1, 
        help="Maximo de descargas que pueden realizarse."
    )

    parser.add_argument(
        "-t", "--time", 
        type=int, #default=1, 
        help="Numero de dias a mantener el archivo"
    )

    args = parser.parse_args()
    main(args)