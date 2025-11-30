#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def _convert_value(text):
    if text == "True":
        return True
    if text == "False":
        return False
    if text is None:
        return None
    try:
        if "." in text:
            return float(text)
        return int(text)
    except (ValueError, TypeError):
        return text


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = _convert_value(child.text)
    return result
