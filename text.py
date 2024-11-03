from dataclasses import dataclass


@dataclass
class Text:
    text: str
    '''"rot13" or "rot47" for now'''
    rot_type: str
    '''"encrypted" or "decrypted"'''
    status: str
