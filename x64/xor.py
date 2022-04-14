#!/usr/bin/env python3

#
# This payload requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from hatsploit.lib.encoder import Encoder
from pex.tools.encoder import EncoderTools


class HatSploitEncoder(Encoder, EncoderTools):
    details = {
        'Name': "x64 XOR Encoder",
        'Encoder': "x64/xor",
        'Authors': [
            'Ivan Nikolsky (enty8080) - encoder developer'
        ],
        'Description': "Simple XOR encoder for x64.",
        'Architecture': "x64"
    }

    options = {
        'KEY': {
            'Description': "8-byte key to encode.",
            'Value': 'P@ssW0rd',
            'Type': None,
            'Required': True
        }
    }

    def run(self):
        key = self.parse_options(self.options)
        count = - int(((len(self.payload - 1) / len(key)) + 1)
