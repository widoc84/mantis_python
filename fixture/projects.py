from model.proj import Proj
import string
import random

class PH:
    def __init__(self, app):
        self.app = app


    def get_proj(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("td[class='menu'] a[href*='manage']").click()
        wd.find_element_by_css_selector("div[align='center'] a[href*='manage_proj']").click()
        list = []
        test = wd.find_elements_by_css_selector('tr[class*="row-"]')
        for i in test[1:-2]:
            list2 = i.find_elements_by_css_selector('td')
            tmp_list = []
            id = (i.find_element_by_css_selector('a').get_attribute('href')).split('=')[1]
            for i2 in list2:
                tmp = i2.text
                tmp_list.append(tmp)
            tmp_list = Proj(id=id,name=tmp_list[0],description=tmp_list[4])
            list.append(tmp_list)
        return list

    def add_proj(self,name,des):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        wd.find_element_by_css_selector("input[name='name']").click()
        wd.find_element_by_css_selector("input[name='name']").send_keys(name)
        wd.find_element_by_css_selector("textarea[name='description']")
        wd.find_element_by_css_selector("textarea[name='description']").send_keys(des)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        id = (wd.find_element_by_link_text('%s' % name).get_attribute('href')).split('=')[1]
        tmp = Proj(id=id,name=name,description=des)
        return tmp

    def del_proj(self,proj):
        wd = self.app.wd
        wd.find_element_by_css_selector("td[class='menu'] a[href*='manage']").click()
        wd.find_element_by_css_selector("div[align='center'] a[href*='manage_proj']").click()
        name = proj.name
        list = wd.find_elements_by_css_selector("a[href*='project_id']")
        wd.find_element_by_link_text('%s' % name).click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()

    def create_type(self, count):
        symbols = string.ascii_letters + string.digits
        return ''.join([random.choice(symbols) for i in range(count)])






