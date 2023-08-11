import logging
logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)

import unittest
import sys
import argparse

formatter = logging.Formatter("[test][%(name)-16s]: %(message)s")

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subdir", nargs='?', type=str)
    args = parser.parse_args()

    start_dir = '.'
    if args.subdir:
        path_list = args.subdir.split('.')
        if len(path_list) > 1:
            start_dir = f'./{path_list[0]}/{path_list[0]}/{path_list[1]}'
        else:
            start_dir = f'./{args.subdir}'
    logger.debug(f'test start dir: {start_dir}')

    suite = unittest.TestLoader().discover(start_dir=start_dir, pattern='test_*.py')
    unittest.TextTestRunner(verbosity=2).run(suite)

# (from Keyrock root dir)
# python -m test [optional subdir, e.g keyrock_core]
# python -m test keyrock_core
# python -m test keyrock_core.config_loader