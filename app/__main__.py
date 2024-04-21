import argparse

from .utils import BackendConnector


def args_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-init_db', required=False, action='store_true')
    parser.add_argument('-off', required=False, type=int)
    parser.add_argument('-show', required=False, action='store_true')
    parser.add_argument('-run', required=False, type=int)
    return parser


if __name__ == "__main__":
    parser = args_parser()
    namespace = parser.parse_args()

    connect = BackendConnector()

    if namespace.off:
        connect.stop_bot(namespace.off)

    if namespace.run:
        connect.start_bot(namespace.run)

    if namespace.show:
        bots = connect.get_bots_list()
        for bot in bots:
            print(f"{bot['id']}) {bot['bot_name']}: active? - {bot['active']}")
