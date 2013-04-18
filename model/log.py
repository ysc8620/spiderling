# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
import logging


class log:
    @staticmethod
    def read(file):
        try:
            fopen = open(file, 'r')
            data = fopen.read()
            fopen.close()
            return data
        except:
            pass

    @staticmethod
    def write(file, logs):
        try:
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S', filename=file,filemode='w')
            logging.info(logs)
        except Exception, e:
            print '-----------', Exception, e
            pass