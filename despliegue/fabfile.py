#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Deployment of the app.
Copyright 2017, Juan Anaya Ortiz (juan.anaya.ortiz@gmail.com)
This program is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, version 3.
This program is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
"""
from fabric.api import cd, run, sudo

def RemoveApp():
    """Delete the app."""
    run('sudo rm -rf ./Bot_Telegram')


def InstallApp():
    """Performs clean installation of the app."""
    RemoveApp()
    # Download the repository
    run('git clone https://github.com/JaoChaos/Bot_Telegram.git')
    # Install requirements
    run('cd Bot_Telegram/ && pip3 install --user -r requirements.txt')




def StartApp():
    """Run the app."""
    with cd('Bot_Telegram'):
        sudo('bash ./scripts/despliegue.sh')
