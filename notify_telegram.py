#!/usr/bin/env python3
# coding: latin-1

try:
    import telepot
    import os.path
    import argparse
    import socket
    import configparser
except ImportError:
    print("[ERROR] cant import library.")
    exit(1)
"""
Description: Just a simple notifier and file sender via telegram BOT ;)
bugs: brunosilvaferreira@protonmail.com
Date: Oct 2018
Usage: 
    python notify_telegram.py -c "/home/user/notify_telegram2.cfg" -t "BOT2" -f "/var/log/daemon.log" "logs"
    python notify_telegram.py -t "BOT1 "Task 101 done." 
    python notify_telegram.py -c "/home/user/notify_telegram.cfg" "Task 102 done."
    python notify_telegram.py -f "/etc/passwd" "Look at this lusers"
    python notify_telegram.py "hey there!"
"""
if __name__ == '__main__':
    usage = '''usage: %(prog)s [-c "CFGFILENAME"] [-t "CFGTITLE"] [-f "FILENAME"] "msg"'''
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("msg", type=str, action="store", default="", help="The content of message that will be send. Used as file caption if -f parameter is used.")
    parser.add_argument("-c", "--cfgfilename", type=str, action="store", dest="cfgfilename", default="notify_telegram.cfg", help="OPTIONAL -\
     The config filename that will be used to store the token and id. Default is notify_telegram.cfg")
    parser.add_argument("-t", "--cfgsection", type=str, action="store", dest="cfgsection", default="DEFAULT", help="OPTIONAL - if you have \
    more than 1 one section you can specify which you will use.")
    parser.add_argument("-f", "--filename", type=str, action="store", dest="filename", help="OPTIONAL - Send a file instead of a message.(MAX 50MB)")
    parser.add_argument('--version', action='version', version='%(prog)s 0.1 - Oct 2018 - brunof')
    args = parser.parse_args()

    if os.path.isfile(args.cfgfilename):
        cfgfilename = args.cfgfilename
        configs = configparser.ConfigParser()
        configs._interpolation = configparser.ExtendedInterpolation()
        configs.read(cfgfilename)

        cfgsection = args.cfgsection
        token = configs.get(cfgsection, 'token', fallback="Cant get a token!")
        id = configs.get(cfgsection, 'id', fallback="Cant get an id!")
        hostname = socket.gethostname()
        bot = telepot.Bot(token)
        msg = args.msg            
        if args.filename:
            if os.path.isfile(args.cfgfilename):
            
                filename = args.filename
                bot.sendDocument(id, document=open(filename, 'rb'), caption=msg)
                
            else:
            
                print("[ERROR] Filename provided is not ok")    
                exit(1)

        else:
            
            bot.sendMessage(id, hostname+": "+msg)

    else:
        print("[ERROR] No config file founded.")
        exit(1)

exit(0)
