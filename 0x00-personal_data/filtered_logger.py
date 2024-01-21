#!/usr/bin/env python3
"""Filter log and Log Formatter module"""
import logging
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Filter and obfuscate specified fields in a log message."""
    for field in fields:
        message = re.sub(f'{field}=[^ {separator}]*',
                         f'{field}={redaction}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter Class"""
    REDACTION = '***'
    FORMAT = '[HOLBERTON] %(levelname)s %(asctime)-15s: %(message)s'
    SEPARATOR = ';'

    def __init__(self, fields: List[str]):
        """Inherit"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Logging format function"""
        original_format = super().format(record)
        return filter_datum(self.fields,
                            self.REDACTION,
                            original_format,
                            self.SEPARATOR)
