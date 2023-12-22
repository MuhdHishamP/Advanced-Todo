from django.test import TestCase
from .models import tag as Tag, TodoDetails
from .serializers import tagSerializer, TodoSerializer
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model 
from django.core.exceptions import ValidationError
from django.utils import timezone

# TEST CODE FOR MODELS 

class TagModelTest(TestCase):
    def test_tag_creation(self):
        # Test the creation of a Tag instance
        tag_name = "Test Tag"
        tag = Tag.objects.create(tag_name=tag_name)
        
        # Check if the tag_name attribute is set correctly
        self.assertEqual(tag.tag_name, tag_name)
        
        # Check if the __str__ method returns the correct string representation
        self.assertEqual(str(tag), tag_name)


class TodoDetailsModelTest(TestCase):
    def test_create_todo(self):
        todo = TodoDetails.objects.create(
            title="Test Todo",
            description="This is a test todo item",
        )
        self.assertEqual(todo.title, "Test Todo")
        self.assertEqual(todo.description, "This is a test todo item")
        self.assertIsNotNone(todo.timestamp)
        self.assertEqual(todo.status, "OPEN")  # Check default status

    def test_due_date_validation(self):
        with self.assertRaises(ValidationError) as context:
            past_date = timezone.now() - timezone.timedelta(days=1)
            TodoDetails.objects.create(
                title="Invalid Due Date",
                description="Test",
                due_date=past_date.date(),  # Extract date from the timestamp
            )
        self.assertEqual(
            context.exception.args[0], "Due Date cannot be before Timestamp created."
        )

    def test_add_tags(self):
        todo = TodoDetails.objects.create(title="Todo with Tags")
        tag1 = Tag.objects.create(tag_name="Work")
        tag2 = Tag.objects.create(tag_name="Important")
        todo.tag.add(tag1, tag2)
        self.assertEqual(todo.tag.count(), 2)
        self.assertIn(tag1, todo.tag.all())
        self.assertIn(tag2, todo.tag.all())

# TEST CODE FOR SERIALIZERS 


class tagSerializerTest(TestCase):
    def test_tag_serialization(self):
        # Test the serialization of a Tag instance using tagSerializer
        tag_name = "Test Tag"
        tag = Tag.objects.create(tag_name=tag_name)
        serializer = tagSerializer(tag)
        
        # Check if the serialized data matches the expected data
        expected_data = {'tag_name': tag_name}
        self.assertEqual(serializer.data, expected_data)


class TodoSerializerTest(TestCase):
    def test_todo_serialization(self):
        title = "Test Todo"
        description = "This is a test todo item."
        todo = TodoDetails.objects.create(title=title, description=description)
        serializer = TodoSerializer(todo)
        expected_data = {
            'id': todo.id,
            'timestamp': todo.timestamp.isoformat().replace('+00:00', 'Z'),  # Adjust timestamp format
            'title': title,
            'description': description,
            'due_date': None,
            'tag': [],  # Adjust tag representation if needed
            'status': 'OPEN'  # Add status field
        }
        self.assertEqual(serializer.data, expected_data)

# TEST CODE FOR VIEWS


class TestViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(self.user)

    def test_tag_list(self):
        # Create tags
        tag1 = Tag.objects.create(tag_name='Work')
        tag2 = Tag.objects.create(tag_name='Personal')

        # Test GET list
        response = self.client.get('/api/tags/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['tag_name'], tag1.tag_name)
        self.assertEqual(data[1]['tag_name'], tag2.tag_name)

    def test_tag_create(self):
        # Test POST create
        data = {'tag_name': 'New Tag'}
        response = self.client.post('/api/tags/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Tag.objects.count(), 1)


    def test_todo_list(self):
        # Create todo items
        todo1 = TodoDetails.objects.create(title='Task 1', description='Description 1', status='OPEN')
        todo2 = TodoDetails.objects.create(title='Task 2', description='Description 2', status='DONE')

        # Test GET list
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['title'], todo1.title)
        self.assertEqual(data[1]['title'], todo2.title)

