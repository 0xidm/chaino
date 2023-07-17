#!/usr/bin/env python3

import os
import json
import random
import logging

import click

from chaino.utils import init_logger, blocks_to_txs_csv
from chaino.scheduler.block import BlockScheduler
from chaino.nested_filestore import NestedFilestore


@click.group()
def cli():
    pass

@cli.command()
@click.argument('chain', type=str)
@click.argument('block_start', type=int)
@click.argument('block_end', type=int)
@click.argument('filestore', type=str)
def download(chain, block_start, block_end, filestore):
    "Write blocks from blockchain to disk"
    block_scheduler = BlockScheduler(
        chain=chain,
        filestore_path=filestore
    )

    for block_number in range(block_start, block_end):
        block_scheduler.add_task(block_number=block_number)

    block_scheduler.start()

@cli.command()
@click.argument('block_start', type=int)
@click.argument('block_end', type=int)
@click.argument('filestore', type=str)
def transactions_csv(block_start, block_end, filestore):
    "Print transactions as CSV"
    filestore = NestedFilestore(
        root_path=os.path.expanduser(filestore),
        hierarchy_order=[3, 3, 3],
    )
    blocks_to_txs_csv(filestore, block_start, block_end)


if __name__ == "__main__":
    init_logger(level=os.getenv("LOG_LEVEL", "INFO"))
    cli()
