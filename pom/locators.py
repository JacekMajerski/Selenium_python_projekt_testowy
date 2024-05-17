from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
#Lokalizatory- Czy buttony dawać wielkimi literami? Czy przyjąć jakąś kolejność? jeśli tak to jaką?

    GO_BUTTON = (By.ID, 'submit')
    username_textbox = (By.ID, 'username')
    register_username_textbox = (By.ID, 'reg_email')
    password_textbox = (By.ID, 'password')
    register_password_textbox = (By.ID, 'reg_password')
    login_button = (By.CSS_SELECTOR, "[name='login']")
    register_button = (By.CSS_SELECTOR, "[name='register']")
    not_correct_password = (By.CSS_SELECTOR, ".woocommerce-error")
    create_account_button = (By.CSS_SELECTOR, ".btn-primary")
    username_ethereal = (By.CSS_SELECTOR, "div:nth-of-type(2) tr:nth-of-type(2) code")
    name_in_my_account =(By.CSS_SELECTOR, "strong:nth-of-type(1)")
    lost_your_password = (By.CSS_SELECTOR, ".woocommerce-LostPassword > a")
    lost_user_login = (By.ID, "user_login")
    reset_password_button = (By.CSS_SELECTOR, "[value='Reset password']")
    logout_my_account = (By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link--customer-logout > a")
    not_reset_email = (By.CSS_SELECTOR, ".woocommerce-message")
    breadcrumbs_my_account = (By.CSS_SELECTOR, "[rel='home']")

class MainPageLocators(object):

    go_to_shop = (By.XPATH, "//ul[@id='topbar-menu']/li[@class='menu-item menu-item-type-post_type menu-item-object-page menu-item-21']//span[@class='nav__title']")
    go_to_cart_main_menu = (By.XPATH, "//ul[@id='topbar-menu']/li[@class='menu-item menu-item-type-post_type menu-item-object-page menu-item-20']//span[@class='nav__title']")
    go_to_cart_icon = (By.CSS_SELECTOR, "[data-toggle='czr-dropdown'] > .icn-shoppingcart")
    go_to_search = (By.CSS_SELECTOR, ".regular-nav.utils .search-toggle_btn")
    search_describe = (By.XPATH, "//div[@class='search__wrapper']//div[@class='form-group czr-focus']")
    search_field = (By.XPATH, "//div[@class='search__wrapper']//input[@name='s']")
    search_results = (By.CSS_SELECTOR, ".czr-title")
    button_shop_banner = (By.XPATH, "//div[@class='sektion-wrapper']//a[.='Shop']")
    second_post_icon = (By.CSS_SELECTOR, ".post-41 > .grid__item")
    hello_world_icon = (By.CSS_SELECTOR, ".post-39 .bg-link")

class ShopPageLocators(object):
    button_add_to_cart_bdd = (By.XPATH, "//li[@class='post-29 product type-product status-publish has-post-thumbnail product_cat-courses first instock shipping-taxable purchasable product-type-simple']/a[.='Add to cart']")
    button_after_adding_to_cart = (By.CSS_SELECTOR, ".added")
    number_in_icon_basket = (By.CSS_SELECTOR, "[data-toggle='czr-dropdown'] > .count")

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass

