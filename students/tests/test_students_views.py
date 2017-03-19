from datetime import datetime

from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse

from students.models import Student, Group

@override_settings(LANGUAGE_CODE='en')
class TestStudentList(TestCase):

    def setUp(self):
        group1, created = Group.objects.get_or_create(
        title="MtM-1")
        group2, created = Group.objects.get_or_create(
        title="MtM-2")
        Student.objects.get_or_create(
            first_name="Vitaliy",
            last_name="Podoba",
            birthday=datetime.today(),
            ticket='12345',
            student_group=group1)

        Student.objects.get_or_create(
            first_name="Anton",
            last_name="Podoba",
            birthday=datetime.today(),
            ticket='12345',
            student_group=group2)

        Student.objects.get_or_create(
            first_name="Vitaliy",
            last_name="Antonov",
            birthday=datetime.today(),
            ticket='12345',
            student_group=group2)

        Student.objects.get_or_create(
            first_name="Anton",
            last_name="Antonov",
            birthday=datetime.today(),
            ticket='12345',
            student_group=group2)
        # remember test browse
        self.client = Client()
        # remember url to our homepage
        self.url = reverse('home')
    def test_students_list(self):
        response = self.client.get(self.url)
        # have we receied OK status from the server?
        self.assertEqual(response.status_code, 200)
        # do we have student name on a page
        self.assertIn('Vitaliy', response.content)
        # do we have link to student edit form?
        self.assertIn(reverse('students_edit',
            kwargs={'pk': Student.objects.all()[0].id}),
            response.content)
        # ensure we got 3 students, pagination limit is 3
        self.assertEqual(len(response.context['students']), 3)
