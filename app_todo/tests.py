from django.test import TestCase
from .models import tag as Tag, TodoDetails
from .serializers import tagSerializer, TodoSerializer
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User  # Import User model

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
    def test_todo_creation(self):
        # Test the creation of a TodoDetails instance
        title = "Test Todo"
        description = "This is a test todo item."
        todo = TodoDetails.objects.create(title=title, description=description)
        
        # Check if the title and description attributes are set correctly
        self.assertEqual(todo.title, title)
        self.assertEqual(todo.description, description)
        
        # Check if the __str__ method returns the correct string representation
        self.assertEqual(str(todo), title)

    def test_status_choices(self):
        # Test that the status field is set to a valid choice
        todo = TodoDetails.objects.create(title="Test", description="Test")
        valid_statuses = ['OPEN', 'WORKING', 'DONE', 'OVERDUE']
        
        # Check if the status is one of the valid choices
        self.assertIn(todo.status, valid_statuses)

    def test_due_date_null_allowed(self):
        # Test that due_date can be set to None
        todo = TodoDetails.objects.create(title="Test", description="Test", due_date=None)
        
        # Check if the due_date is set to None
        self.assertIsNone(todo.due_date)

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


class TodoViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test tag
        self.tag = Tag.objects.create(tag_name='Test Tag')

        # Create a test TodoDetails instance
        self.todo = TodoDetails.objects.create(
            title='Test Todo',
            description='Test Description',
            due_date='2023-12-31',
            status='OPEN'
        )
        self.todo.tag.add(self.tag)

        # Set up the client for making API requests
        self.client = APIClient()

        # Authenticate the client with the test user
        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        # Clean up after the test
        self.client.force_authenticate(user=None)

    def test_get_todo_list(self):
        # Send GET request to the API endpoint for TodoView
        response = self.client.get('/api/todos/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response contains the title of the test todo
        self.assertIn('Test Todo', response.data[0]['title'])

    def test_create_todo(self):
        # Define data for creating a new todo
        data = {
            'title': 'New Todo',
            'description': 'New Description',
            'due_date': '2023-12-31',
            'status': 'OPEN',
            'tag': [self.tag.id],  # Provide the tag ID
        }

        # Send POST request to the API endpoint for creating todos
        response = self.client.post('/api/todos/', data)

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the created todo exists in the database
        self.assertTrue(TodoDetails.objects.filter(title='New Todo').exists())
