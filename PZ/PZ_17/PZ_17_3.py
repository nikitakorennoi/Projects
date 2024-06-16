import os
# task 1
print(os.listdir('C:\\Users\\tess\\.vscode\\IS-25\\PZ\\PZ_11'))
# task 2
try:
    os.mkdir('./test')
    os.mkdir('./test/test1')
except:
    pass

# task 3
os.rename('C:\\Users/tess/.vscode/IS-25/PZ/PZ_6/1.txt', './test/1.txt')
os.rename('C:\\Users/tess/.vscode/IS-25/PZ/PZ_6/2.txt', './test/2.txt')
os.rename('C:\\Users/tess/.vscode/IS-25/PZ/PZ_7/test.txt', './test/test1/test.txt')

# task 4
path = os.listdir('./test')
for i in path:
    print((os.path.getsize(f'./test/{i}')), 'bytes')

# task 5
path = os.listdir('C:\\Users\\tess\\.vscode\\IS-25\\PZ\\PZ_11')
path = min(path, key=len)

print(os.path.basename(f'C:\\Users\\tess\\.vscode\\IS-25\\PZ\\PZ_11/{path}'))

# task 6

os.startfile('C:\\Users\\tess\\Desktop\\reports\\PZ_10.docx')

# task 7
os.remove('C:\\Users\\tess\\.vscode\\IS-25\\test\\test1\\test.txt')