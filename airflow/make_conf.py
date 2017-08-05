#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from jinja2 import Environment, FileSystemLoader

__author__ = 'Shinichi Nakagawa'

ENVIRONMENTS = (
    'AIRFLOW_HOME',
    'AIRFLOW_EXECUTOR',
    'AIRFLOW_DB_CONN',
    'AIRFLOW_WORKER',
    'AIRFLOW_WORKER_HOST',
    'AIRFLOW_WORKER_PORT',
    'AIRFLOW_WORKER_DATABASE',
    'AIRFLOW_EXAMPLES',
    'AIRFLOW_AUTH',
)


def create_airflow_cfg(path, tpl, filename='airflow.cfg', encoding='utf8'):
    """
    create airflow.cfg
    :param path: root path
    :param tpl: template file
    :param filename: output filename
    :param encoding: Encoding(default:utf8)
    """
    env = Environment(loader=FileSystemLoader(path, encoding=encoding))
    cfg_tpl = env.get_template(tpl)
    cfg = cfg_tpl.render({env: os.environ.get(env) for env in ENVIRONMENTS})
    file_path = '/'.join([path, filename])
    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, 'w', encoding=encoding) as f:
        f.write(cfg)
        f.close()


if __name__ == '__main__':
    create_airflow_cfg(path=os.environ.get('AIRFLOW_HOME'), tpl='airflow.tpl.cfg')
