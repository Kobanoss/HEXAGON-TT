from argparse import ArgumentParser

parser = ArgumentParser(description='TCP/UDP Swagger')
parser.add_argument("mode", type=str, choices=['UDPS', 'TCPS'],
                    help="Select mode: UDP-Server[UDPS] or TCP-Server[TCPS]")
parser.add_argument("wp", type=int,
                    help="Port number for HTTP server interface")
parser.add_argument("sp", type=int,
                    help="Port number for TCP/UDP server")


