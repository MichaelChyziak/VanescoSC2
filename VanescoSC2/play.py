#!/usr/bin/env python

#MIT License
#
#Copyright (c) 2017 TheChyz
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import VanescoSC2.sc2Initialization
import Agents.random_agent
import logging
import signal
import sys

def main():
    signal.signal(signal.SIGINT, signal_handler)

    logging.basicConfig(
        level=logging.DEBUG,  # Change to "level=loggin.DEBUG" to see debug messages
        format="%(levelname)-8s: %(message)s",
        datefmt="%d,%b,%Y %H:%M:%S",
        filename="log\info.log",
        filemode="w")
    logging.info("Log Start")

    sc2_socket = VanescoSC2.sc2Initialization.sc2Connection()
    VanescoSC2.sc2Initialization.sc2Start(sc2_socket)
    Agents.random_agent.run(sc2_socket)

def signal_handler(signal, frame):
    log = logging.getLogger(__name__)
    log.info("Program ended using ctrl+c")
    sys.exit(0)


if __name__ == "__main__":
    main()
