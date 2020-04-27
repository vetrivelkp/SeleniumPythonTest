from Utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage
from pageObject.CheckoutPage import CheckoutPage
from pageObject.Confirm import ConfirmPage

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopitems()
        log.info("loading products page")
        products = checkoutpage.getproductstitle()

        #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")

        # //div[@class='card h-100']/div/h4/a
        # product =//div[@class='card h-100']
        i = -1
        for product in products:
            i += 1
            productname = product.text
            log.info(productname)
            if productname == "Blackberry":
                # Add item into cart
                log.info("Item Matched")
                checkoutpage.getaddtocart()[i].click()
        log.info("Item added to cart")

        checkoutpage.getcheckoutinshop().click()
        confirmpage = checkoutpage.getcheckoutincart()

        confirmpage.getlocation().send_keys("ind")
        self.objectpresence("India")
        confirmpage.getselectloc().click()
        log.info("Country selected")
        confirmpage.gettermsandcond().click()
        confirmpage.getsubmit().click()

        successtext = confirmpage.getsubmitmessage().text
        #successtext = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successtext
        log.info("Purchase successful with messaage "+successtext)

        try:
            self.driver.get_screenshot_as_file("screen.png")
        except AttributeError:
            log.error("Taking screenshot failed")

