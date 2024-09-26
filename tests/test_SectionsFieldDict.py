import unittest
from pathlib import Path

from PyJotformAJM.SectionsFieldDict import SectionFieldsDict
from PyJotformAJM.PyJotformAJM import JotForm

test_api_key_path = Path('../Misc_Project_Files/TestFormAPIKey.key').resolve()
if test_api_key_path.is_file():
    with open(test_api_key_path, 'r') as f:
        API_KEY = f.read()
else:
    raise EnvironmentError(f"API key file not found at {test_api_key_path}")


class TestSectionFieldsDict(unittest.TestCase):
    def setUp(self):
        self.jf = JotForm(api_key=API_KEY, form_id='242693235658062')
        self.sfd = SectionFieldsDict(self.jf)

    def test_get_current_section_index_start(self):
        self.assertIsInstance(self.sfd.get_current_section_index_start('New Section')['section_index'], int)

    def test_get_next_section_index_start(self):
        try:
            self.assertIsInstance(self.sfd.get_next_section_index_start('New Section')['section_index'], int)
        except KeyError:
            self.assertIsInstance(self.sfd.get_next_section_index_start('New Section'), dict)
            self.assertEqual(len(self.sfd.get_next_section_index_start('New Section').keys()), 0)

    def test_get_section_fields(self):
        fields = self.sfd.get_section_fields('New Section')
        print(fields)
        self.assertIsInstance(fields, list)
        self.assertGreater(len(fields), 0)

    def test_str(self):
        self.assertIsInstance(str(self.sfd), str)


if __name__ == '__main__':
    unittest.main()
