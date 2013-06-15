#!/usr/bin/python
"""Example bot using KitnIRC. Just connects to a server."""
import argparse
import logging

import kitnirc.client


def main():
    parser = argparse.ArgumentParser(description="Example IRC client.")
    parser.add_argument("host", help="Address of an IRC server")
    parser.add_argument("nick", help="Nickname to use when connecting")
    parser.add_argument("-p", "--port", type=int, default=6667,
        help="Port to use when connecting")
    parser.add_argument("--username", help="Username to use. If not set, "
                                           "defaults to nickname.")
    parser.add_argument("--realname", help="Real name to use. If not set, "
                                           "defaults to username.")
    parser.add_argument("--password", help="IRC server password, if any.")
    args = parser.parse_args()

    # Logging initialization
    log_handler = logging.StreamHandler()
    log_formatter = logging.Formatter(
        "%(levelname)s %(asctime)s %(name)s:%(lineno)04d - %(message)s")
    log_handler.setFormatter(log_formatter)

    root_logger = logging.getLogger()
    root_logger.addHandler(log_handler)
    root_logger.setLevel(logging.DEBUG)

    c = kitnirc.client.Client(args.host, args.port)
    c.connect(
        args.nick,
        username=args.username or args.nick,
        realname=args.realname or args.username or args.nick,
        password=args.password,
    )
    c.run()


if __name__ == "__main__":
    main()

# vim: set ts=4 sts=4 sw=4 et:
