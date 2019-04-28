#!/usr/bin/env python3
	
import fileinput
import re
 


for line in fileinput.input():
    line = re.sub(r'\$\$([^$]*)\$\$', r'<math>\1</math>', line.rstrip())
    line = re.sub(r'\$([^$]*)\$', r'<math>\1</math>', line.rstrip())
    line = re.sub(r'\\textit\{([^}]*)\}', r"''\1''", line.rstrip())
    #line = re.sub(r'\\rowsp\{[^}]*\}', r"\\mathcal\{R\}(\\mathbf\1)", line.rstrip())
    line = re.sub(r'\\rowsp\{([^}]*)\}', r"\\mathcal{R}( \\mathbf \1)", line.rstrip())
    line = re.sub(r'\\colsp\{([^}]*)\}', r"\\mathcal{C}( \\mathbf \1)", line.rstrip())
    line = re.sub(r'\\mb', r'\\mathbf', line.rstrip())
    line = re.sub(r'\\mc', r'\\mathcal', line.rstrip())
    line = re.sub(r'\\rank', r'\\text{rank}', line.rstrip())
    line = re.sub(r'\\begin{itemize}', r'', line.rstrip())
    line = re.sub(r'\\end{itemize}', r'', line.rstrip())
    line = re.sub(r'\\item', r'*', line.rstrip())
    line = re.sub(r'\\begin{equation}', r'<math>', line.rstrip())
    line = re.sub(r'\\end{equation}', r'</math>', line.rstrip())
    print(line)
    
