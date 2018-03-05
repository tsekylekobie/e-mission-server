"""
must install selenium (pip install selenium)
also install PhantomJS (brew/npm), and replace with executable_path
"""
from selenium import webdriver
info, control, emotion = 0, 0, 0
trials = 1000
path = '/Users/Jesse/Desktop/node_modules/phantomjs/lib/phantom/bin/phantomjs'
driver = webdriver.PhantomJS(executable_path=path)
for _ in range(trials):
    driver.get('https://tripaware.eecs.berkeley.edu')
    p_element = driver.find_element_by_id(id_='groupLink')
    if 'urap2017information' in p_element.get_attribute('href'):
        info += 1
    elif 'urap2017emotion' in p_element.get_attribute('href'):
        emotion += 1
    else:
        control += 1
print('info: ' + str(info/trials))
print('emotion: ' + str(emotion/trials))
print('control: ' + str(control/trials))