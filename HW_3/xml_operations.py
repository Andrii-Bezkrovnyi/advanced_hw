"""Task 3-2: Create an XML file with nested elements and perform XPath-like queries."""
import xml.etree.ElementTree as ET


def create_xml_file(filename: str) -> None:
    """Create an XML file with nested elements and save it."""
    university = ET.Element("university")

    # Faculty 1
    faculty1 = ET.SubElement(university, "faculty", name="Engineering")
    student1 = ET.SubElement(faculty1, "student", id="1")
    ET.SubElement(student1, "name").text = "Alice"
    ET.SubElement(student1, "grade").text = "A"

    student2 = ET.SubElement(faculty1, "student", id="2")
    ET.SubElement(student2, "name").text = "Bob"
    ET.SubElement(student2, "grade").text = "B"

    # Faculty 2
    faculty2 = ET.SubElement(university, "faculty", name="Science")
    student3 = ET.SubElement(faculty2, "student", id="3")
    ET.SubElement(student3, "name").text = "Charlie"
    ET.SubElement(student3, "grade").text = "A+"

    # Save XML to file
    tree = ET.ElementTree(university)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    print(f"XML file '{filename}' created successfully.")


def search_with_xpath(filename: str) -> None:
    """Perform XPath-like queries on the XML document."""
    tree = ET.parse(filename)
    root = tree.getroot()

    print("\n--- XPath Queries ---")

    # Find all students
    all_students = root.findall(".//student")
    print(f"Total students: {len(all_students)}")

    # Find all students with grade 'A'
    grade_a_students = root.findall(".//student[grade='A']")
    print("Students with grade A:")
    for s in grade_a_students:
        print(" →", s.find("name").text)

    # Find all students in the 'Engineering' faculty
    engineering_students = root.findall(".//faculty[@name='Engineering']/student/name")
    print("\nEngineering Faculty students:")
    for name in engineering_students:
        print(" →", name.text)

    # Faculties with students having grade 'A+' (Python filter)
    faculties_with_a_plus: list[str] = []
    for faculty in root.findall(".//faculty"):
        for student in faculty.findall("student"):
            grade = student.find("grade")
            if grade is not None and grade.text == "A+":
                faculties_with_a_plus.append(faculty.attrib["name"])
                break

    print("\nFaculties with students having grade A+:")
    for name in faculties_with_a_plus:
        print(" →", name)


if __name__ == "__main__":
    file_name = "university.xml"
    create_xml_file(file_name)
    search_with_xpath(file_name)
