#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from cerberus import Validator
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser


__author__ = 'Shinichi Nakagawa'


class AirflowUser(object):

    SCHEMA = {
        'name': {
            'type': 'string',
            'required': True,
            'empty': False,
            'min': 4,
        },
        'email': {
            'type': 'string',
            'required': True,
            'empty': False,
            'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        },
        'password': {
            'type': 'string',
            'required': True,
            'empty': False,
            'min': 8,
        }
    }

    def __init__(self, **kwargs):
        self.params = kwargs
        pass

    def create(self):
        """
        create user
        """
        user = PasswordUser(models.User())
        user.username = self.params.get('name')
        user.email = self.params.get('email')
        user.password = self.params.get('password')
        session = settings.Session()
        session.add(user)
        session.commit()
        session.close()


@click.command()
@click.option('--name', '-n', required=True, help='Your name')
@click.option('--email', '-e', required=True, help='Your e-mail')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='Your password')
def main(name, email, password):
    """
    Create Airflow user
    :param name: name
    :param email: email
    :param password: passowrd
    """
    params = {'name': name, 'password': password, 'email': email}
    v = Validator(AirflowUser.SCHEMA)
    if not v.validate(params):
        print(v.errors)

    c = AirflowUser(name=name, password=password, email=email)
    c.create()


if __name__ == '__main__':
    main()
