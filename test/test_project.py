import random

def test_add_project(app):
    old_proj = app.projects.get_proj()
    name = app.projects.create_type(6)
    des = app.projects.create_type(10)
    app.projects.add_proj(name,des)
    new_proj = app.projects.get_proj()
    assert len(old_proj) + 1 == len(new_proj)

def test_del_project(app):
    old_proj = app.projects.get_proj()
    if len(old_proj) < 1:
        name = app.projects.create_type(6)
        des = app.projects.create_type(10)
        app.projects.add_proj(name, des)
        old_proj = app.projects.get_proj()
    name =  random.choice(old_proj)
    app.projects.del_proj(name)
    new_proj = app.projects.get_proj()
    assert len(old_proj) - 1 == len(new_proj)