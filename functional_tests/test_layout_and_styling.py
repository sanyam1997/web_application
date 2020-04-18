from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling( self ) :
        # Sanyam goes to the home page
        self.browser.get( self.live_server_url )
        self.browser.set_window_size( 1024 , 768 )

        # He notices that the input box is nicely centered
        # inputbox = self.browser.find_element_by_id( "id_new_item" )
        inputbox = self.browser.find_element_by_id( "id_new_item" )
        self.assertAlmostEqual(
            inputbox.location[ 'x' ] + inputbox.size['width'] / 2 ,
            512 ,
            delta = 10
        )
        # He starts a new list and sees the input
        # is centered too
        inputbox.send_keys( "testing" )
        inputbox.send_keys( Keys.ENTER )
        self.wait_for_row_in_list_table( "1: testing" )
        inputbox = self.browser.find_element_by_id( "id_new_item" )
        self.assertAlmostEqual(
            inputbox.location[ 'x' ] + inputbox.size['width'] / 2 ,
            512 ,
            delta = 10
        )
