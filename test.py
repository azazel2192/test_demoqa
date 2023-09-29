from DemoQA import DataQA
from config import browser

def test_demoqa(browser):
    demoqa_page = DataQA(browser)
    demoqa_page.open_demoqa()
    demoqa_page.click_element_button()
    assert demoqa_page.check_url() == 'elements'
    demoqa_page.click_checkbox_button()
    assert demoqa_page.check_url() == 'checkbox'
    demoqa_page.click_home_dropdown_button()
    assert demoqa_page.check_home_dropdown_expanded() is True
    demoqa_page.click_download_dropdown()
    assert demoqa_page.check_downloads_dropdown_expanded() is True
    demoqa_page.click_wordfile_checkbox()
    assert demoqa_page.check_wordfile_checkbox() == 'You have selected :wordFile'
