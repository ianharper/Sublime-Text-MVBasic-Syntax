import sublime
import sublime_plugin


class mvBasicReindentCommand(sublime_plugin.TextCommand):
	def getBlockCount(self, scopes):
		block_count = 0
		for scope in scopes:
			if scope[:10] == 'meta.block': block_count += 1
		return block_count
		
	def setIndentLevel(self, scopes, base_indent_level, indent_comments):
		scopes = scopes.split(' ')
		if not(indent_comments) and scopes[1][:30] == 'punctuation.definition.comment': return 0
		if scopes[1][:20] == 'entity.name.function': return 0
		return self.getBlockCount(scopes) + int(base_indent_level)


	def run(self, edit):
		base_indent_level = sublime.load_settings('MVBasic-Syntax.sublime-settings').get('base_indentation_level', 2) 	
		indent_comments = sublime.load_settings('MVBasic-Syntax.sublime-settings').get('indent_comments', False) 	

		full_region = sublime.Region(0,self.view.size())
		source_text = self.view.substr(full_region).split('\n')
		for line in range(self.view.rowcol(self.view.size())[0]  + 1):
			line_start = self.view.find(r"\S", self.view.text_point(line,0)).a
			scopes = self.view.scope_name(line_start)	
			indent_level = self.setIndentLevel(scopes, base_indent_level, indent_comments)
			source_text[line] = '\t' * indent_level + source_text[line].lstrip()

		self.view.replace(edit, full_region, '\n'.join(source_text))

