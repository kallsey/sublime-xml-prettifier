XML Prettifier
==============

This is a very simple plugin for [Sublime Text 2](http://www.sublimetext.com/2) that prettify (format with tabs and new lines) selected text in your active window.

Installation
------------

Place `XmlPrettify.py` under `~/Library/Application Support/Sublime Text 2/Packages/User/` if you’re a Mac and under `%APPDATA%\Roaming\Sublime Text 2\Packages\` if you’re a PC. Linux guys figure everything out themselves.

You also need to add key binding. Insert `{ "keys": ["super+shift+x"], "command": "xml_prettify" }` in Preferences / Key Bindings - User in the list between `[ ]`. In case you have not heard ‘super’ is the ‘command’ ⌘ key. If you have Windows, just write ‘ctrl’. 