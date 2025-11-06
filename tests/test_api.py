'''
Example 101: Add API Testing to Portfolio

'''

import pytest

class TestAPI:
    """API testing examples using Playwright's request context"""
    
    @pytest.fixture(autouse=True)
    def setup(self, playwright):
        self.request_context = playwright.request.new_context(
            base_url="https://jsonplaceholder.typicode.com"
        )
        yield
        self.request_context.dispose()
    
    def test_get_user_api(self):
        """Test GET request to retrieve user"""
        response = self.request_context.get("/users/1")
        
        assert response.status == 200
        data = response.json()
        assert data["id"] == 1
        assert "name" in data
        assert "email" in data
        print(f"Retrieved user: {data['name']}")
        
    def test_create_post_api(self):
        """Test POST request to create post"""
        new_post = {
            "title": "Test Automation Post",
            "body": "Created via Playwright API testing",
            "userId": 1
        }
        
        response = self.request_context.post("/posts", data=new_post)
        
        assert response.status == 201
        data = response.json()
        assert data["title"] == new_post["title"]
        assert "id" in data
        print(f"Created post with ID: {data['id']}")
        
    def test_update_post_api(self):
        """Test PUT request to update post"""
        updated_post = {
            "id": 1,
            "title": "Updated Title",
            "body": "Updated content",
            "userId": 1
        }
        
        response = self.request_context.put("/posts/1", data=updated_post)
        
        assert response.status == 200
        data = response.json()
        assert data["title"] == "Updated Title"
        
    def test_delete_post_api(self):
        """Test DELETE request"""
        response = self.request_context.delete("/posts/1")
        
        assert response.status == 200
        print("Post deleted successfully")