# XML 1 - Find the Score

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    return sum(len(child.attrib) for child in node.iter())

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
