"""
Test routes for routes for authorizing users, app/main/routes
"""
# pylint: disable=redefined-outer-name,unused-argument

def test_version_page(client, login_user_response, user_dict, user_post_response, post_dict):
    """
    Test version route
    """
    response = client.get("/version")
    assert response.status_code == 200
    assert b"Version" in response.data
