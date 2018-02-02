import os
import markdown


EXTENSIONS = ['markdown.extensions.toc',
              'markdown.extensions.smarty',
              'markdown.extensions.fenced_code',
              'markdown.extensions.nl2br',
              'markdown.extensions.headerid',
              'markdown.extensions.codehilite']
md = markdown.Markdown(extensions=EXTENSIONS,
                       extension_configs={
                        'markdown.extensions.codehilite': {
                            'noclasses': True
                        }
                       })

BASE = './'

def build_doc(file_name):
    if file_name.endswith('.md'):
        print(file_name)
        title = file_name[:-3]
        new_file_name = title+'.html'
        full_path = os.path.join(BASE, file_name)
        out_path = os.path.join(BASE, new_file_name)
        md.convertFile(full_path, out_path)
        print(title)

if __name__ == "__main__":
	from sys import argv
	print(argv)
	for file_name in argv:
		build_doc(file_name)