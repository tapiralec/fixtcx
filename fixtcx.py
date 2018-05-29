import xml.etree.ElementTree
from sys import argv
import fileinput


def Process(fin):
    e = xml.etree.ElementTree.parse(fin)
    xml.etree.ElementTree.register_namespace('', "http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2")
    root = e.getroot()

    ignorefirst = True

    for track in root.iter('{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Track'):
        for trackpoint in track.getchildren():
            dist = trackpoint.find('{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}DistanceMeters')
            if (ignorefirst):
                ignorefirst = False
            else:
                if dist.text=='0.0':
                    track.remove(trackpoint)
                    print("removed zero-distance trackpoint")
    print("complete!")

    
    e.write("output"+argv[1], encoding="UTF-8", xml_declaration=True)


if __name__=="__main__":
    Process(argv[1])

