

import os
import requests
import pyperclip
from argparse import ArgumentParser

URL_TRANSFER = 'https://transfer.sh'


def main(args):
    # Verificar que el archivo existe
    if not os.path.isfile(args.filename):
        raise FileNotFoundError
    
    print(f"󰅧  Uploading...")
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
            print(f"󰅠  Upload complete!\n{dl_url}Copied to your clipboard (ctrl+V)")
            pyperclip.copy(dl_url)

    except Exception as xcp:
        print(f"󰅤  Something wrong... {xcp}")



if __name__ == "__main__":
    parser = ArgumentParser(
        prog="PyTransfer",
        description="Script to quickly upload and share a file via transfer.sh")
    
    parser.add_argument(
        'filename',
        help="Path to file",
    )

    parser.add_argument(
        "-d", "--downloads", 
        type=int, #default=1, 
        help="Number of max downloads until deletion"
    )

    parser.add_argument(
        "-t", "--time", 
        type=int, #default=1, 
        help="Number of days available online."
    )

    args = parser.parse_args()
    main(args)