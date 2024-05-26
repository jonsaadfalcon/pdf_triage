from __future__ import annotations
from pathlib import Path

import click
import json


@click.command()
@click.argument("dataset_path", type=Path)
def analyze_preference(
        dataset_path: Path
) -> None:
    with dataset_path.open() as fp:
        dataset = json.load(fp)

    for document in dataset:
        for page in document['results']['content']['0']['pages']:
            for task in page['tasks']:
                if task['user_response']:
                    print(task['user_response'])


if __name__ == '__main__':
    analyze_preference()