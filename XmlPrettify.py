import sublime, sublime_plugin

class XmlPrettifyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		from xml.dom.minidom import parseString
		selection = self.view.sel()[0]
		dom = parseString(self.view.substr(selection).encode('utf-8'))
		prettified = dom.toprettyxml()
		self.view.replace(edit, selection, prettified)