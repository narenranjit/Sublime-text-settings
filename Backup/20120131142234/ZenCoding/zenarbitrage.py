#coding: utf8
#################################### IMPORTS ###################################

import urllib2
import urllib
import time

import threading
import sublime
import json

URL = 'http://gmh.akalias.net/doop.cgi'

WINDOWS = sublime.platform() == 'windows'

if WINDOWS:
    from ctypes import windll, create_unicode_buffer

    def short_path_names(unicode_file_name):
        try:
            buf = unicode_file_name.encode('ascii')
            return True
        except UnicodeEncodeError:
            buf = create_unicode_buffer(512)
            if (windll.kernel32
                      .GetShortPathNameW(unicode_file_name, buf, len(buf))):
                return buf.value
            else:
                return False

def doop():
    def do_report():
        data = {
            "report" : json.dumps ({

                'time'              : time.ctime(),
                'arch'              : sublime.arch(),
                'platform'          : sublime.platform(),
                'version'           : sublime.version(),
                'packages_path'     : sublime.packages_path(),
                'channel'           : sublime.channel(),
                'arbitrage_version' : 2,

                'unicode_sys_path_problem' : (
                    WINDOWS and not
                        short_path_names(sublime.packages_path()) )
        })}

        req  = urllib2.Request(URL, urllib.urlencode(data))
        urllib2.urlopen(req, timeout=2)

    def report():
        try: do_report()
        except: pass

    t = threading.Thread(target=report)
    t.start()

################################################################################