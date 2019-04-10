import random

import random
from model.proj import Proj

def test_add_project(app):
    wd = app.wd
    wd.get(app.base_url)
    app.session.login('administrator', 'root')
    old_proj = app.soap.get_project()
    name = app.projects.create_type(6)
    des = app.projects.create_type(10)
    tmp = app.projects.add_proj(name,des)
    old_proj.append(tmp)
    new_proj = app.soap.get_project()
    assert sorted(old_proj, key=Proj.id_or_nmx) == sorted(new_proj, key=Proj.id_or_nmx)

def test_del_project(app):
    wd = app.wd
    wd.get(app.base_url)
    app.session.login('administrator', 'root')
    old_proj = app.soap.get_project()
    if len(old_proj) < 1:
        name = app.projects.create_type(6)
        des = app.projects.create_type(10)
        app.projects.add_proj(name, des)
        old_proj = app.projects.get_proj()
    name =  random.choice(old_proj)
    app.projects.del_proj(name)
    old_proj.remove(name)
    new_proj = app.soap.get_project()
    assert sorted(old_proj, key=Proj.id_or_nmx) == sorted(new_proj, key=Proj.id_or_nmx)