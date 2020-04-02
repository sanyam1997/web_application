from selenium import webdriver
import unittest

class NewVisitorTest( unittest.TestCase ) :

    def setUp( self ) :
        self.browser = webdriver.Firefox( )

    def tearDown( self ) :
        self.browser.quit( )

    def test_can_start_a_list_and_retrieve_it_later( self ) :
        # Sanyam has heard about this cool new online to-do app. He goes
        # to checkout its homepage.
        self.browser.get( "http:/localhost:8000" )

        # She notices the page title and header mention to-do lists
        self.assertIn( 'To-Do' , self.browser.title )
        self.fail( 'Finish the test.' )

        # He is invited to a to-do item straight away.

        # He types "Buy peacock feathers" into a text box ( Sanyam' hobby is typing in
        # fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in to-do list

        # There is still a text box inviting her to add another item. He
        # enters "Use peacock feathers to make a fly" ( Sanyam is very methodical )

        # The page updates again, and now shows both items on her list

        # Sanyam wonders whether the site still remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # text to that effect.

        # He visits the URL - his to-do list is still there.

if __name__ == "__main__" :
    unittest.main( warnings = 'ignore' )

if __name__ == "__main__" :
    unittest.main( warnings = 'ignore' )
